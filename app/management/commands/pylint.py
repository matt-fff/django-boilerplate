from typing import List

import pylint.lint
from django.core.management.base import BaseCommand

from app.management.common import RegexFileCommand


class Command(RegexFileCommand, BaseCommand):
    help = "Lints the codebase using pylint"
    DEFAULT_PYLINT_OPTS = [
        "--rcfile=.pylintrc",
        "--disable=fixme",
        "--load-plugins=pylint_django",
    ]

    @classmethod
    def run_command(cls, file_list: List[str], **__):
        pylint.lint.Run(cls.DEFAULT_PYLINT_OPTS + file_list)
