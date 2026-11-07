# Quiet organization profile and governance

This is the source for [Quiet's GitHub organization page](profile/README.md), shared
engineering guidance and the PR-only ruleset configuration for the Quiet projects.
Application source lives in separate [QuietChat](https://github.com/quiet-desktop-apps/QuietChat)
and [QuietTube](https://github.com/quiet-desktop-apps/QuietTube) repositories.

- [Organization profile](profile/README.md)
- [Agentic Engineering](docs/agentic-engineering.md)
- [Publishing and repository governance](docs/publishing.md)
- [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [MIT license](LICENSE)

## Checks

```bash
python3 -m py_compile scripts/measure-memory.py
python3 scripts/check-profile.py
```

The organization `.github` repository has the same PR-only default-branch policy
as the applications. This repository does not contain app sessions or private data.
