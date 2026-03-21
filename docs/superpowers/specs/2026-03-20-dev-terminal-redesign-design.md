# Dev Terminal — Site Redesign Spec

## Context

The LeetCode 75 site currently uses a generic light minimalist design (gobyexample-inspired). The goal is to give it a distinctive dark, techy, terminal-inspired aesthetic that feels personal and memorable — like a developer's own tool.

## Design Direction: "Dev Terminal"

Dark IDE/terminal aesthetic with cyan/teal accents, embedded terminal windows for code, and file-tree-style navigation.

## Color Palette

| Token | Value | Usage |
|-------|-------|-------|
| `--bg` | `#0d1117` | Page background |
| `--surface` | `#161b22` | Cards, terminal window, panels |
| `--border` | `#30363d` | Subtle borders |
| `--fg` | `#e6edf3` | Primary text |
| `--fg-muted` | `#7d8590` | Secondary text, labels |
| `--accent` | `#58a6ff` | Links, highlights, active states |
| `--accent-hover` | `#79c0ff` | Hover state for links |
| `--terminal-green` | `#3fb950` | Green dot, success |
| `--terminal-yellow` | `#d29922` | Yellow dot |
| `--terminal-red` | `#f85149` | Red dot |

Syntax highlighting: Shiki `github-dark` theme.

## Typography

- **Body:** System sans-serif stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`)
- **Code & monospace accents:** `'JetBrains Mono', 'Fira Code', 'Consolas', monospace` — loaded via Google Fonts (JetBrains Mono, weights 400/600)
- **Headings:** Monospace bold (same as code font)

## Components

### Header

- Full-width bar with `--surface` background and bottom border
- Left: site title as terminal prompt `~/leetcode75 $` in monospace
- Right: language toggle `EN | ES` in muted text, active state with `--surface` pill background

### Index Page

- Centered container (max-width 700px) on `--bg` background
- Categories as uppercase muted headings (like directory names)
- Problems as list items with:
  - `>` prefix in accent color (cyan)
  - Number in muted monospace
  - Title as link in primary text color
  - `(wip)` badge for problems without solutions
- Hover: line background shifts to `--surface`, `>` brightens
- Progress bar at bottom: block characters `█░` in monospace, accent color for filled portion

### Problem Page

Two-column grid layout (1fr 1fr on desktop, stacked on mobile).

**Left column (Statement):**
- `--bg` background
- Category badge at top in uppercase muted
- Statement rendered as HTML with styled markdown elements
- Text in `--fg`, code spans with `--surface` background

**Right column (Terminal Window):**
- `--surface` background
- Title bar with:
  - Three dots: red (`#f85149`), yellow (`#d29922`), green (`#3fb950`) — 12px circles
  - File name in muted monospace text
  - Thin bottom border `--border`
- Code area below with syntax-highlighted Python (Shiki `github-dark`)
- If no solution: italic muted placeholder "Solution coming soon."

**Navigation bar (bottom):**
- Full-width bar with top border
- Left: `← prev` link (or empty)
- Right: `next →` link (or empty)
- Styled as simple text links, not terminal commands

### Language Toggle

- Two buttons `EN` and `ES` separated by `|`
- Active button: accent color text, `--surface` background pill
- Inactive: muted text, no background
- Uses `localStorage` to persist preference
- Toggles `data-lang="en"` / `data-lang="es"` divs on problem pages

## Micro-interactions

- Links: color transition 150ms ease on hover
- Problem list items: background-color transition 150ms on hover
- Terminal dots: no animation (keep it clean)
- `>` prefix: color brightens on hover

## Responsive (< 768px)

- Two columns stack vertically (statement on top, terminal below)
- Terminal window takes full width
- Header stays single row (title left, lang toggle right)
- Index container gets smaller padding

## Files to Modify

| File | Changes |
|------|---------|
| `site/src/styles/global.css` | Complete rewrite with dark theme, new color tokens, terminal components |
| `site/src/layouts/Base.astro` | Update header to terminal prompt style, add JetBrains Mono font link |
| `site/src/pages/index.astro` | Add `>` prefixes, progress bar, hover styles |
| `site/src/pages/[slug].astro` | Add terminal window markup (dots, title bar), restructure code column |

## Verification

1. `npm run build` builds without errors
2. Index page shows dark theme with file-tree style listing
3. Problem pages show terminal window with dots and syntax-highlighted code
4. Language toggle works and persists across navigation
5. Responsive layout stacks correctly on mobile
6. All text is readable (sufficient contrast on dark backgrounds)
