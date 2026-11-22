# Daily project factory

Two scheduled ChatGPT workers use this repository to plan, build and verify independent public portfolio projects. The model and authenticated GitHub browser session are supplied by the worker environment. No external model billing or stored GitHub token is configured.

## Running a track

Read the dated records in history and run `python factory.py plan A YYYY-MM-DD` or substitute B. Use the current Kolkata date. Each line is an outstanding slot, oldest first. Use the category as a starting point and compare proposed ideas with the account repository list and index. Read FACTORY_SPEC.md for the project requirements.

Reserve one slot with a new file named reservations/YYYY-MM-DD-TRACK.json containing the selected repository name, purpose and status. Create it against the current central branch head before creating any repository. On conflict re-read the reservation. If a matching record already exists, verify its publication and skip. Resume an existing reservation only after verifying repo ownership and its recorded initial commit or verified project commit. Escalate ambiguous collisions and keep other repositories untouched.

Generate the source in an independent checkout. Use a supported runtime, meaningful sample data and automated tests. Run the documented installation and sample, language checks, tests and FAQ validator. For other languages use the relevant native build and test commands. Run project code in an isolated environment without publishing credentials. Review results before publishing. Create a public repository through the authenticated GitHub interface and publish all files with a single commit. Check its default branch commit and file manifest. Include the actual test output and commit in the completion report.

## Recording results

Write one history/YYYY-MM-DD-TRACK.json per verified slot following the two initial records. Rebuild PROJECT_INDEX.md with `python factory.py index > PROJECT_INDEX.md`. Commit both together against the latest central head. Retry a rejected update after reading the latest files. Record failed attempts under attempts/ with slot, time, stage and sanitized error. Leave failed slots outstanding. On retry check the remote commit before publishing again.

## Recovery

A separately scheduled recovery worker checks both tracks through yesterday and retries missing work. Each track also checks prior dates. If permissions expire, retain the reservation and report the exact failed step. A worker interruption before initial commit recording may need operator reconciliation. The scheduler and recovery worker share a service, so a service-wide outage can delay both. Check the index after service returns.

## Local checks

Run `python -m unittest discover -s tests -v`, `python factory.py validate PATH_TO_PROJECT` and `python factory.py plan B 2026-11-23`. The validator checks required documentation and FAQ numbering. Review answer accuracy and the implementation separately.
