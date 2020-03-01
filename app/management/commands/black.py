from typing import List
import sys
from subprocess import call
from django.core.management.base import BaseCommand

from app.management.common import RegexFileCommand


class Command(RegexFileCommand, BaseCommand):
    help = "Formats the codebase using black"
    DEFAULT_BLACK_COMMAND = ["black", "--config", "pyproject.toml"]

    @classmethod
    def add_arguments(cls, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "-c",
            "--check",
            action="store_true",
            help="Check the current formatting",
        )

    # pylint: disable=arguments-differ
    @classmethod
    def run_command(cls, file_list: List[str], check: bool = False, **__):
        additional_opts = []
        if check:
            additional_opts.append("--check")

        sys.exit(call(cls.DEFAULT_BLACK_COMMAND + additional_opts + file_list))
