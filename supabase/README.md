# Learner accounts setup

The site is static, so sign up, login, courses, invoices and messages are stored in a Supabase project.

1. Create a project at supabase.com. Choose an EU region.
2. Open the SQL editor, paste `schema.sql` and run it.
3. Authentication, URL configuration: set Site URL to `https://simplitechacademy.com` and add `https://simplitechacademy.com/**` to the redirect URLs.
4. Authentication, Providers: keep Email on and "Confirm email" on.
5. Project settings, API: copy the Project URL and the `anon` public key into `SUPA_URL` and `SUPA_KEY` at the top of the script in `index.html`. The anon key is public by design; the row level security rules in `schema.sql` protect the data. Never put the `service_role` key in the site.
6. Sign up on the site once, then run the admin statement at the bottom of `schema.sql` with your own email.

## Day to day (Table editor)

- **Enroll a learner:** in `enrollments`, set the learner's row to `active` (or add one).
- **Release material:** add rows to `materials` for the course (`kind` is `elearning`, `github`, `lab` or `other`, `url` must start with https). Learners see them only once their enrollment is active.
- **Invoice:** add a row to `invoices` and, optionally, upload the PDF to the private `invoices` bucket under `<user id>/<file>.pdf` and put that path in `pdf_path`.
- **Reply to a message:** add a row to `messages` with `sender` = `academy` and the learner's `user_id`. New learner messages also arrive in your inbox through the contact form service.
