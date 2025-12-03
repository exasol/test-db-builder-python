from tdbp.dialects.exasol.exasol_object_factory import ExasolObjectFactory

def test_create_schema():
    dialect = ExasolObjectFactory()
    schema = dialect.create_schema("ONLINE_SHOP")
    assert schema.name == "ONLINE_SHOP"