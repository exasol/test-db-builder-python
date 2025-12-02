import pyexasol
from pyexasol import ExaConnection

from tdbp.dialects.exasol.exasol_fingerprint_provider import ExasolFingerprintProvider


def connect() -> ExaConnection:
    return pyexasol.connect(dsn=f"localhost/{ExasolFingerprintProvider().fingerprint()}:8563", user="sys",
                            password="exasol",
                            autocommit=False)


class ExasolConnectionFactory:
    pass