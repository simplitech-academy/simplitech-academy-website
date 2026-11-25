# Simplitech Academy website

Static site served by GitHub Pages.

- `index.html` holds the whole site (home, about and blog views, switched by the URL hash).
- `posts.json` holds the blog posts, newest first. The daily blog task adds a post here.
- `favicon.svg` is the brand icon.
- `CNAME` holds the custom domain (academy.simplitechglobal.com).

## Daily automation

A scheduled task adds one tech brief to `posts.json` and two cue cards to `simplibytes.json` every morning.
`node tools/render-bytes.js` then renders each new card to `bytes/<id>.png` (1080 x 1350, the same picture as the
"Save image" button). `social-log.json` records which cards were posted to Instagram and LinkedIn.

## Course pages and syllabi

Every course has its own landing page at `#course-<slug>` (for example
`#course-kubernetes-in-practice`). The pages are drawn from `courses.json`, so
to change a title, duration, module, tool or certification you edit that file
and nothing else.

Each course in `courses.json` has: `slug`, `title`, `group`, `type`
(`short` or `long`), `level`, `weeks`, `sessions`, `hours`, `tagline`, `who`,
`prereq`, `outcomes`, `modules` (title, topics, lab, and optionally `w` for
weeks and `course` to link another course), `tools`, `projects`, `prepares` and
`next`. For long programs the module weeks must add up to `weeks`.

The downloadable syllabus for each course is `syllabi/<slug>.pdf`. After
changing `courses.json`, rebuild the PDFs and commit them:

    node tools/build-syllabi.js            # all courses
    node tools/build-syllabi.js sre-program # one course

This needs Playwright with Chromium, like `tools/render-bytes.js`.

The durations are drafts: they assume two one-hour live sessions a week, so
`sessions` is `weeks x 2`. Change `weeks` and `sessions` together.

## Learner accounts

The Log in button opens `#account`: sign up, log in, password reset, and a dashboard
with My courses (with material), Invoices, Messages and Profile. Data lives in Supabase.
Until `SUPA_URL` and `SUPA_KEY` are filled in at the top of the script, the page shows
"coming soon". Setup steps and the database schema are in `supabase/`.
