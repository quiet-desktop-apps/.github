# Quiet

**Useful desktop apps. Less browser overhead.**

Quiet builds focused, open-source Linux applications for things we use every day.
The aim is simple: keep the features that matter, use native interfaces, and make
memory consumption visible and measurable.

YouTube is usually watched in a browser. Some Linux WhatsApp clients bring a
Chromium runtime of their own. That is convenient, but a full browser stack can be
more machinery than a focused video queue or messaging window needs. Quiet explores
a different approach: GTK4 interfaces, bounded caches, local state, and media
players or service workers that run only when needed.

## The apps

| Project | What it does | Technology |
|---|---|---|
| [QuietTube](https://github.com/quiet-desktop-apps/QuietTube) | YouTube feeds, search and a persistent editable playback queue | Python, GTK4, yt-dlp, SQLite, mpv |
| [QuietChat](https://github.com/quiet-desktop-apps/QuietChat) | Essential WhatsApp messaging, images, videos, replies and notifications; also a terminal UI | Python/GTK4, TypeScript/Node.js, Baileys, SQLite, mpv |

Both are MIT licensed, independently versioned projects. Neither embeds Chromium,
Electron or a webview. Browser-assisted account connection and clicked links can
still use your existing browser. These are unofficial clients, with service and
account limitations documented in each repository.

[See QuietTube screenshots](https://github.com/quiet-desktop-apps/QuietTube#quiettube)
· [See QuietChat desktop and terminal screenshots](https://github.com/quiet-desktop-apps/QuietChat#quietchat)

## What we have measured

| Development observation | Memory and scope |
|---|---|
| QuietChat GTK, live snapshot | ~244 MiB combined app RSS / ~132 MiB PSS |
| Chromium-based WhatsApp client, same workstation snapshot | ~1,536 MiB RSS / ~1,110 MiB PSS |
| QuietChat terminal, everyday observation | Around 170 MiB app RSS; excludes terminal emulator/media viewer |
| QuietTube repeated 30-card feed replacements | ~199–203 MiB UI RSS after warm-up, stable across 200 replacements |
| QuietTube separate short 720p playback checks | ~253–265 MiB mpv RSS; UI/extractor excluded |

The captured QuietChat desktop snapshot was about **84% lower RSS** than that
particular Chromium client. This is an observation from one development machine,
not a controlled equal-workload benchmark or a universal promise. QuietTube has
**no controlled browser comparison yet**. Its separate UI/player measurements must
not be presented as one measured total. RSS can double-count shared pages; PSS
apportions them. Read the complete
[QuietChat evidence](https://github.com/quiet-desktop-apps/QuietChat/blob/master/docs/memory.md)
and [QuietTube evidence](https://github.com/quiet-desktop-apps/QuietTube/blob/master/docs/memory.md).

Lower memory is a product constraint, not the only one. Reliability, privacy,
accessibility and familiar workflows matter too. QuietChat's terminal version
trades native desktop integration for a smaller interface; its major limitation is
**no built-in desktop notifications or system tray**. The GTK version supplies both.

## Human direction, agent implementation

Quiet follows **Agentic Engineering**. A human maintains the idea, high-level
requirements, acceptance criteria and important technical decisions. Coding agents
implement, test and document within that direction. Humans own acceptance and merge authority;
agents may execute an explicitly authorized release through reviewed PRs and
passing checks. An agent review is not represented as independent human approval. Agent involvement is disclosed, and failures
or untested assumptions are recorded rather than hidden.

Our [engineering process](https://github.com/quiet-desktop-apps/.github/blob/master/docs/agentic-engineering.md)
explains the responsibilities. All changes to the default branch go through pull
requests and required CI checks. No bypass actors are configured. With one initial
maintainer, independent approval is not yet required; administrators retain the
ability to edit GitHub settings.

## Why an organization?

Quiet gives these applications a shared home, design language and engineering
standard while letting each app keep its own repository and release cycle.
Contributors can improve one app or help establish reusable native patterns,
measurement practices and accessibility improvements across the family.

Try the offline demos, report reproducible problems, propose a focused feature or
share a memory measurement with clear scope. Contributors using coding agents are
welcome; human responsibility and review still apply. See each repository's
contribution and security guides. Linux is the current target; we do not claim
Windows/macOS packages or full parity with the underlying services.

Founded and maintained by [Paulo Aboim Pinto](https://github.com/aboimpinto).
