"""Python tooling to fetch and update applications."""

from pathlib import Path
from typing import List
import toml

def get_directories() -> List[Path]:
    """Get local application directories"""
    directories: List = []
    applications_directory = Path("applications")
    for path in applications_directory.iterdir():
        if path.is_dir():
            directories.append(path)

    return directories

def update_all():
    """Update snapcraft configurations for all applications."""
    directories = get_directories()
    print(directories)


def list_all():
    """Update snapcraft configurations for all applications."""
    directories = get_directories()
    print(directories)

    # iterate through each directory
        # check for config.toml
        # parse each toml to a dictionary
        # fetch updates
