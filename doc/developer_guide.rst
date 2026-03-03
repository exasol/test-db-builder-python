.. _developer_guide:

Developer Guide
===============

Prerequisites
-------------

This project is tested with Python 3.12.

As test environment uses the the  ITDE_.

.code-block: shell::
    pip install exasol-integration-test-docker-environment

Running the Integration Tests
-----------------------------

Exasol Integration Tests
~~~~~~~~~~~~~~~~~~~~~~~~

For the Exasol dialect, the project uses the `integration-test-docker-environment` (ITDE_) which starts Exasol in a docker container and creates a docker network with a second docker container in which the tests run.

The `pytest-exasol-backend` serves as an abstraction, so that we do not have to start the ITDE by hand. This project only tests against the on-prem backend (read: `docker-db`).

.. _ITDE: https://github.com/exasol/integration-test-docker-environment/
.. _PEB: https://github.com/exasol/pytest-backend/
