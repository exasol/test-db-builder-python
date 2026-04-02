# Unreleased

## Summary

In this release we fixed the following security issues by updating dependencies in the `poetry.lock` file.

| Name         | Version | ID                  | Fix Versions |
|--------------|---------|---------------------|--------------|
| black        | 25.12.0 | CVE-2026-32274      | 26.3.1       |
| cryptography | 46.0.5  | CVE-2026-34073      | 46.0.6       |
| pygments     | 2.19.2  | CVE-2026-4539       | 2.20.0       |
| requests     | 2.32.5  | CVE-2026-25645      | 2.33.0       |
| tornado      | 6.5.4   | GHSA-78cv-mqj4-43f7 | 6.5.5        |
| tornado      | 6.5.4   | CVE-2026-31958      | 6.5.5        |

Please note that the situation on the user's machine can differ, since they have their own poetry lock.

## Security

* # Fixed security issues in by updating the dependencies listed above.