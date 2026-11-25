-- Simplitech Academy learner accounts. Run once in the Supabase SQL editor.
-- Every table has row level security: learners see only their own rows.

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  full_name text,
  is_admin boolean not null default false,
  created_at timestamptz not null default now()
);

create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, full_name)
  values (new.id, nullif(trim(coalesce(new.raw_user_meta_data->>'full_name','')), ''));
  return new;
end $$;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

create or replace function public.is_admin() returns boolean
language sql security definer stable set search_path = public as $$
  select coalesce((select is_admin from public.profiles where id = auth.uid()), false)
$$;

create table public.enrollments (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  course_slug text not null,
  status text not null default 'requested' check (status in ('requested','active','completed','cancelled')),
  start_date date,
  created_at timestamptz not null default now(),
  unique (user_id, course_slug)
);

create table public.materials (
  id bigint generated always as identity primary key,
  course_slug text not null,
  title text not null,
  kind text not null default 'other' check (kind in ('elearning','github','lab','other')),
  url text not null check (url ~ '^https://'),
  sort int not null default 0
);

create table public.invoices (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  number text not null unique,
  course_slug text,
  description text,
  amount_cents int not null,
  currency text not null default 'EUR',
  status text not null default 'open' check (status in ('open','paid','void')),
  issued_at date not null default current_date,
  pdf_path text
);

create table public.messages (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  sender text not null check (sender in ('learner','academy')),
  body text not null check (char_length(body) between 1 and 4000),
  created_at timestamptz not null default now()
);
create index on public.messages (user_id, created_at);

alter table public.profiles    enable row level security;
alter table public.enrollments enable row level security;
alter table public.materials   enable row level security;
alter table public.invoices    enable row level security;
alter table public.messages    enable row level security;

-- profiles: read own, edit own name only (is_admin cannot be changed by users)
create policy "own profile read"   on public.profiles for select using (id = auth.uid() or public.is_admin());
create policy "own profile update" on public.profiles for update using (id = auth.uid()) with check (id = auth.uid());
revoke update on public.profiles from authenticated;
grant update (full_name) on public.profiles to authenticated;

-- enrollments: learners may request, only admins activate
create policy "own enrollments read"    on public.enrollments for select using (user_id = auth.uid() or public.is_admin());
create policy "request enrollment"      on public.enrollments for insert with check (user_id = auth.uid() and status = 'requested');
create policy "admin manage enrollments" on public.enrollments for all using (public.is_admin()) with check (public.is_admin());

-- materials: visible only to learners with an active or completed enrollment in that course
create policy "enrolled read materials" on public.materials for select using (
  public.is_admin() or exists (
    select 1 from public.enrollments e
    where e.user_id = auth.uid() and e.course_slug = materials.course_slug and e.status in ('active','completed')
  )
);
create policy "admin manage materials" on public.materials for all using (public.is_admin()) with check (public.is_admin());

-- invoices: own only, written by admins
create policy "own invoices read"     on public.invoices for select using (user_id = auth.uid() or public.is_admin());
create policy "admin manage invoices" on public.invoices for all using (public.is_admin()) with check (public.is_admin());

-- messages: learners write as themselves, admins reply
create policy "own messages read"   on public.messages for select using (user_id = auth.uid() or public.is_admin());
create policy "learner sends"       on public.messages for insert with check (user_id = auth.uid() and sender = 'learner');
create policy "admin replies"       on public.messages for insert with check (public.is_admin() and sender = 'academy');

-- private bucket for invoice PDFs, stored as <user id>/<file>.pdf
insert into storage.buckets (id, name, public) values ('invoices', 'invoices', false) on conflict do nothing;
create policy "own invoice files read" on storage.objects for select using (
  bucket_id = 'invoices' and ((storage.foldername(name))[1] = auth.uid()::text or public.is_admin())
);
create policy "admin invoice files write" on storage.objects for all using (bucket_id = 'invoices' and public.is_admin())
  with check (bucket_id = 'invoices' and public.is_admin());

-- After you sign up once yourself, make that account the admin:
--   update public.profiles set is_admin = true
--   where id = (select id from auth.users where email = 'YOUR_ADMIN_EMAIL');
