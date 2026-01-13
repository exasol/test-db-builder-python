import tomllib


class TddbConfig:
    host = "localhost"
    port = 8653
    user = "sys"
    password = None

    @classmethod
    def from_env(cls, path: str) -> "TddbConfig":
        with open(path, "rb") as config_file:
            config = tomllib.load(config_file)
        return cls(**config.get("database", {}))
