# 1.0.1 - 2026-07-17

## Summary

In this release we fixed integration test and therefore code coverage reporting in CI. The switch `--backend onprem` was missing from slow tests, causing integration tests to be skipped.

## Security Issues

This release fixes vulnerabilities by updating dependencies:

| Dependency | Vulnerability | Affected | Fixed in |
|------------|---------------|----------|----------|
| black | PYSEC-2026-2121 | 25.12.0 | 26.3.1 |
| black | PYSEC-2026-2120 | 25.12.0 | 26.3.0 |
| click | PYSEC-2026-2132 | 8.3.1 | 8.3.3 |
| cryptography | PYSEC-2026-35 | 46.0.5 | 46.0.6 |
| cryptography | PYSEC-2026-36 | 46.0.5 | 46.0.7 |
| cryptography | PYSEC-2026-36 | 46.0.5 | 46.0.7 |
| cryptography | PYSEC-2026-35 | 46.0.5 | 46.0.6 |
| cryptography | GHSA-537c-gmf6-5ccf | 46.0.5 | 48.0.1 |
| gitpython | PYSEC-2026-2161 | 3.1.46 | 3.1.47 |
| gitpython | PYSEC-2026-2160 | 3.1.46 | 3.1.47 |
| gitpython | PYSEC-2026-2162 | 3.1.46 | 3.1.48 |
| gitpython | PYSEC-2026-2163 | 3.1.46 | 3.1.49 |
| gitpython | GHSA-mv93-w799-cj2w | 3.1.46 | 3.1.50 |
| idna | PYSEC-2026-215 | 3.11 | 3.15 |
| idna | PYSEC-2026-215 | 3.11 | 3.15 |
| msgpack | GHSA-6v7p-g79w-8964 | 1.1.2 | 1.2.1 |
| pip | PYSEC-2026-196 | 26.0.1 | 26.1.2 |
| pip | PYSEC-2026-196 | 26.0.1 | 26.1.2 |
| pip | PYSEC-2026-2875 | 26.0.1 | 26.1 |
| pip | PYSEC-2026-2876 | 26.0.1 | 26.1 |
| pygments | PYSEC-2026-2987 | 2.19.2 | 2.20.0 |
| pytest | PYSEC-2026-1845 | 8.4.2 | 9.0.3 |
| requests | PYSEC-2026-2275 | 2.32.5 | 2.33.0 |
| soupsieve | PYSEC-2026-3072 | 2.8.3 | 2.8.4 |
| soupsieve | PYSEC-2026-3071 | 2.8.3 | 2.8.4 |
| starlette | PYSEC-2026-161 | 0.52.1 | 1.0.1 |
| starlette | PYSEC-2026-161 | 0.52.1 | 1.0.1 |
| starlette | PYSEC-2026-248 | 0.52.1 | 1.3.0 |
| starlette | PYSEC-2026-249 | 0.52.1 | 1.3.1 |
| starlette | PYSEC-2026-248 | 0.52.1 | 1.3.0 |
| starlette | PYSEC-2026-2281 | 0.52.1 | 1.1.0 |
| starlette | PYSEC-2026-2280 | 0.52.1 | 1.1.0 |
| tornado | PYSEC-2026-140 | 6.5.4 | 6.5.5 |
| tornado | PYSEC-2026-140 | 6.5.4 | 6.5.5 |
| tornado | PYSEC-2026-2287 | 6.5.4 | 6.5.5 |
| tornado | PYSEC-2026-3387 | 6.5.4 | 6.5.6 |
| tornado | PYSEC-2026-3388 | 6.5.4 | 6.5.6 |
| tornado | PYSEC-2026-3389 | 6.5.4 | 6.5.6 |
| tornado | GHSA-pw6j-qg29-8w7f | 6.5.4 | 6.5.7 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-141 | 2.6.3 | 2.7.0 |

* #23: Fixed security issues by updating dependencies
* #25: Fixed vulnerabilities by updating dependencies

## Refactoring

* #27: Updated to exasol-toolbox 8.2.0
* #30: Updated to exasol-toolbox 10.0.0

## Dependency Updates

### `main`

* Updated dependency `pyexasol:2.0.0` to `2.2.2`
* Updated dependency `regex:2026.2.28` to `2026.5.9`

### `dev`

* Updated dependency `exasol-integration-test-docker-environment:5.0.0` to `6.2.0`
* Updated dependency `exasol-toolbox:6.0.0` to `10.0.0`
* Removed dependency `nox:2026.2.9`
* Updated dependency `pytest:8.4.2` to `9.1.1`
* Updated dependency `pytest-exasol-backend:1.3.0` to `1.4.1`
* Added dependency `toml:0.10.2`
* Updated dependency `types-regex:2026.2.28.20260301` to `2026.5.9.20260518`