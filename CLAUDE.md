# Project notes for Claude

## Preferences

- **Previewing pushed work:** After pushing changes that affect a viewable file
  (e.g. an HTML page), always share a preview URL that pins the **full commit
  SHA** — not the branch name — so the user never sees a stale, CDN-cached
  version. Format:

  ```
  https://htmlpreview.github.io/?https://raw.githubusercontent.com/<owner>/<repo>/<FULL_COMMIT_SHA>/<path>
  ```

  Use the full 40-character SHA from `git rev-parse HEAD`.
