import pytest
from exasol.tdbp.schema import Schema


def test_prevent_sql_injection_via_schema_identifier():
    with pytest.raises(ValueError):
        Schema(None, "THE_TABLE;SELECT * FROM SYS.EXA_ALL_USERS;")
