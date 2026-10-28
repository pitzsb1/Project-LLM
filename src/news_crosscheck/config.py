"""Load non-secret local harness configuration (Python 3.11+)."""
from pathlib import Path
import tomllib


def load_config(path: Path) -> dict:
    """Read a local TOML file without environment access or external calls."""
    with path.open("rb") as stream:
        return tomllib.load(stream)["project"]
