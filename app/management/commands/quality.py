from typing import List

from django.core.management.base import BaseCommand

from app.management.common import RegexFileCommand
from .black import Command as black
from .pycodestyle import Command as pycodestyle
from .pylint import Command as pylint


class Command(RegexFileCommand, BaseCommand):
    help = "Runs all code quality checks against the codebase"

    @classmethod
    def run_command(cls, file_list: List[str], **_):
        pycodestyle.run_command(file_list)
        black.run_command(file_list, check=True)
        pylint.run_command(file_list)
