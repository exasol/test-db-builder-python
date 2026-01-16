from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from exasol.toolbox.config import BaseConfig


class Config(BaseConfig):
    root: Path = Path(__file__).parent
    doc: Path = Path(__file__).parent / "doc"
    source: Path = Path("exasol/tdbp")
    version_file: Path = Path(__file__).parent / "exasol" / "tdbp" / "version.py"
    path_filters: Iterable[str] = (
        "dist",
        ".eggs",
        "venv",
        ".venv",
        "build",
    )
    plugins: Iterable[object] = ()


PROJECT_CONFIG = BaseConfig(
    project_name="tdbp",
    root_path=Path(__file__).parent,
    python_versions=("3.12", "3.13"),
    exasol_versions=("2025.1.8",),
)
