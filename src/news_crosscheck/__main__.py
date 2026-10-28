"""Offline configuration check, not an application entry point."""
from pathlib import Path
from .config import load_config


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    config = load_config(root / "config.toml")
    print(f"Harness config loaded: {config['name']}")
    print(f"API enabled: {config['api_enabled']}")
    print("News analysis: not implemented")


if __name__ == "__main__":
    main()
