"""
config.py
---------
Read vex.toml project configuration from the current project folder.
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

from vex.errors import VexConfigError

CONFIG_FILENAME = "vex.toml"
REQUIRED_FIELDS = ("name", "version", "mode", "entry")


@dataclass(frozen=True)
class VexConfig:
    name: str
    version: str
    mode: str
    entry: str


def format_config(
    name: str,
    version: str = "0.1.0",
    mode: str = "hinglish",
    entry: str = "main.vex",
) -> str:
    return (
        f'name = "{name}"\n'
        f'version = "{version}"\n'
        f'mode = "{mode}"\n'
        f'entry = "{entry}"\n'
    )


def _parse_simple_toml(content: str) -> Dict[str, str]:
    values: Dict[str, str] = {}
    pattern = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"([^"]*)"\s*$')

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = pattern.match(stripped)
        if match:
            values[match.group(1)] = match.group(2)

    return values


def _parse_toml_content(content: str) -> Dict[str, str]:
    if sys.version_info >= (3, 11):
        import tomllib

        data = tomllib.loads(content)
        return {key: str(value) for key, value in data.items()}

    return _parse_simple_toml(content)


def parse_config(content: str) -> VexConfig:
    data = _parse_toml_content(content)
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise VexConfigError(
            f"vex.toml mein fields missing hain: {', '.join(missing)}"
        )

    return VexConfig(
        name=data["name"],
        version=data["version"],
        mode=data["mode"],
        entry=data["entry"],
    )


def find_config_file(directory: Path) -> Optional[Path]:
    config_path = directory / CONFIG_FILENAME
    if config_path.is_file():
        return config_path
    return None


def load_config(config_path: Path) -> VexConfig:
    content = config_path.read_text(encoding="utf-8")
    return parse_config(content)


def load_project_config(
    start_dir: Optional[Path] = None,
) -> Optional[Tuple[VexConfig, Path]]:
    project_dir = (start_dir or Path.cwd()).resolve()
    config_path = find_config_file(project_dir)
    if config_path is None:
        return None

    return load_config(config_path), project_dir


def resolve_entry_file(
    start_dir: Optional[Path] = None,
) -> Optional[Path]:
    loaded = load_project_config(start_dir)
    if loaded is None:
        return None

    config, project_dir = loaded
    return project_dir / config.entry
