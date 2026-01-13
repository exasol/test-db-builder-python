from test.conftest import PROJECT_ROOT
from exasol.tdbp.tdbp_config import TddbConfig


def test_config_defaults():
    config = TddbConfig.from_toml(PROJECT_ROOT / ".env.example/tddb.toml")
    assert config.host == "localhost"


def test_config_secret():
    config = TddbConfig.from_toml(PROJECT_ROOT / ".env.example/tddb.toml")
    assert config.password == "exasol"
