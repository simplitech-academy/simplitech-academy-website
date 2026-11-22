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
