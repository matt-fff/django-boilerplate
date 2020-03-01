import sys
from typing import List

from django.core.management.base import BaseCommand
from pycodestyle import StyleGuide

from app.management.common import RegexFileCommand


class Command(RegexFileCommand, BaseCommand):
    help = "Lints the codebase using pycodestyle"

    @classmethod
    def run_command(cls, file_list: List[str], **__):
        style_guide = StyleGuide(paths=file_list, config_file=".pycodestyle")
        report = style_guide.check_files()

        if report.total_errors:
            sys.stderr.write(str(report.total_errors) + "\n")
            sys.exit(1)
