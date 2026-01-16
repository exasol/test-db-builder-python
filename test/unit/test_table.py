import pytest

from exasol.tdbp.table import Table


def test_prevent_sql_injection_via_table_identifier():
    with pytest.raises(ValueError):
        Table(None, "THE_TABLE;SELECT * FROM SYS.EXA_ALL_USERS;", None)
