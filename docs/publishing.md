# Publication and repository governance

Quiet's GitHub organization is `quiet-desktop-apps`. The application repositories
are `QuietChat` and `QuietTube`; `.github` holds the public organization profile.
All are public MIT-licensed source repositories. Default branch: `master`.

## Bootstrap and pull requests

A new GitHub repository needs a first commit before a pull request has a base.
The initial server-generated README/LICENSE is the only initialization commit.
Immediately after creation, install an active default-branch ruleset before
pushing application source. Import all application files on a feature branch and
open a PR. Do not push application changes directly to `master`.

The checked-in `ruleset.json` requires:

- A pull request for changes to the default branch and `master`.
- The GitHub Actions `checks` result, with the branch up to date.
- Resolution of review conversations.
- No deletion or force pushes.
- No bypass actors, including administrators or automation accounts.
- Squash merging through a PR.

At initial release there is one maintainer. Independent approval count is zero
because GitHub disallows self-approval; this must not be described as an enforced
two-person review policy. The human maintainer owns merge authority and may
authorize an agent to publish through PRs after required checks pass.
When a second maintainer joins, raise the required approving review count to one
and consider code-owner approval. Repository owners can edit or remove rules;
GitHub cannot make them irreversible against the owner.

Feature branches accept commits so contributors can open PRs. “PR only” protects
the integration branch, not every branch in the repository. Do not add broad bypass
permissions to fix a failing check. Fix the check, rerun it and merge normally.

## Release essentials

The first public source release includes licensing, installation instructions,
architecture, memory evidence with scope, synthetic-data screenshots, contribution
and agent guidance, issue/PR templates, private security reporting, CODEOWNERS,
required CI and dependency-update PRs. Automated tests do not access real accounts.

Do not publish auth/session databases, cookie exports, pairing codes, private logs,
real conversation screenshots, virtual environments, dependency directories or
build output. Review the Git index before every initial import. Keep third-party
notices; an MIT source license does not relicense mpv, GTK or bundled dependencies.

Before a versioned binary release, still do:

1. Validate a clean installation on the documented supported distributions.
2. Agree a supported-version policy, changelog and release cadence.
3. Audit the exact bundled dependency licenses and generate an SBOM if packaging.
4. Produce reproducible packages, checksums and signing/provenance where supported.
5. Test accessibility, keyboard navigation and high-DPI/desktop differences.
6. Gather a longer-duration, equal-workload memory comparison.
7. Add another human maintainer if enforcing independent approvals is a goal.

These are future release tasks, not features falsely claimed by the initial source
publication. There are no signed binary packages, warranty, official service
endorsements or response-time promises at launch.
