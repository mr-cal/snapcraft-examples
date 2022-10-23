"""Python tooling to fetch and update applications."""

from argparse import Namespace
from pathlib import Path
from typing import List
import toml

def get_directories() -> List[Path]:
    """Get local application directories"""
    directories: List = []
    applications_directory = Path("applications")

    if not applications_directory.is_dir():
        raise Exception("could not find applications directory")

    for path in applications_directory.iterdir():
        if path.is_dir():
            directories.append(path)

    if directories == []:
        raise Exception("could not find any applications in the application directory")

    return directories

def update_all():
    """Update snapcraft configurations for all applications."""
    directories = get_directories()
    print(directories)


def list_all(parsed_args: Namespace):
    """Update snapcraft configurations for all applications."""
    directories = get_directories()
    applications = {}

    for directory in directories:
        config_file = directory / "config.toml"
        if not config_file.exists():
            raise Exception(f"cannot find config file {config_file}")

        application_data = toml.load(config_file)
        application_name = application_data["info"]["name"]
        applications[application_name] = application_data

    for application in applications:
        print(application)
