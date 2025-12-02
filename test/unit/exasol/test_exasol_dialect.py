import pytest


from dbbuilder.dialects.exasol import Exasol

def test_create_schema():
    dialect = Exasol()
    schema = dialect.create_schema("ONLINE_SHOP")
    assert schema.name == "ONLINE_SHOP"