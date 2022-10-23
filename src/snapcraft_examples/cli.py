"""CLI interface for snapcraft_examples."""

import argparse
import logging

from . import applications

logger = logging.getLogger(__name__)


def main():
    """Main entry point."""
    args = parse_args()
    args.func(args)


def parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser(description="Manage snapcraft applications")
    subparsers = parser.add_subparsers(help="sub-command help")

    list_instances_parser = subparsers.add_parser("list", help="list applications")
    list_instances_parser.set_defaults(func=applications.list_all)

    update_instances_parser = subparsers.add_parser("update", help="update applications")
    update_instances_group = list_instances_parser.add_mutually_exclusive_group()
    update_instances_parser.set_defaults(func=applications.update_all)
    update_instances_group.add_argument(
        "--all",
        help="update all applications",
        action="store_true",
        required=False,
    )
    update_instances_group.add_argument(
        "--name",
        help="update one or more applications",
        metavar="name",
        nargs="+",
        required=False,
        type=str,
    )

    args = parser.parse_args()
    logger.info("Parsed %s", vars(args))
    return args
