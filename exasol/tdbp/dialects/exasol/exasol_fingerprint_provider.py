import re

import pyexasol


class ExasolFingerprintProvider:
    _instance = None
    _fingerprint = None

    def __init__(self):
        if ExasolFingerprintProvider._instance is not None:
            raise RuntimeError("Use get_instance() instead")
        self._extract_fingerprint()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _extract_fingerprint(self):
        """This is a crude way of extracting the fingerprint by first connecting to the Exasol
        database with an intentionally wrong fingerprint and then extracting the actual fingerprint
        from the error message.

        It needs to be replaced by a more robust solution as soon as the ITDE supports extracting
        the fingerprint.
        """
        try:
            pyexasol.connect(
                dsn="localhost/0000000000000000000000000000000000000000000000000000000000000000:8563",
                user="sys",
                password="exasol",
                autocommit=False,
            )
        except pyexasol.ExaConnectionFailedError as error:
            # Extract fingerprint from error message
            error_str = str(error)
            print(f"Error message: {error_str}")
            fingerprint_search = re.search(
                "server fingerprint \[([A-F0-9]+)\]", error_str, re.MULTILINE
            )
            if fingerprint_search:
                self._fingerprint = fingerprint_search.group(1)
                print(f"Extracted fingerprint: {self._fingerprint}")
            else:
                raise error

    def fingerprint(self):
        return self._fingerprint
