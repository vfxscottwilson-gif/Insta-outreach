"""Loads settings.toml and templates.toml from the project config folder."""
import hashlib
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"


def load(config_dir=None):
    d = Path(config_dir) if config_dir else CONFIG_DIR
    with open(d / "settings.toml", "rb") as f:
        settings = tomllib.load(f)
    with open(d / "templates.toml", "rb") as f:
        templates = tomllib.load(f)
    return settings, templates


def fingerprint(config_dir=None):
    d = Path(config_dir) if config_dir else CONFIG_DIR
    h = hashlib.sha256()
    for name in ("settings.toml", "templates.toml"):
        h.update((d / name).read_bytes())
    return h.hexdigest()[:16]
