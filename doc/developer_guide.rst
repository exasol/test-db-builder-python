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

.. _ITDE: https://github.com/exasol/integration-test-docker-environment