import glob
import sys
from typing import List
from abc import ABC
from loguru import logger


def get_file_list(
    filename: str = None, directory: str = None, extension: str = None, **_
) -> List[str]:

    # Because of the way we call this function alongside Django's
    # argument handling means that we can't rely on defaults, above.
    # They can get None'd out; so we set all the defaults here.
    filename = filename if filename else "*"
    directory = directory if directory else ""
    extension = extension if extension else ".py"

    # Clean our inputs
    if filename.endswith(extension):
        filename = filename[:-3]
    if directory and not directory.endswith("/"):
        directory += "/"

    file_list = glob.glob(
        "{0}**/{1}{2}".format(directory, filename, extension), recursive=True
    )

    if not file_list:
        logger.info(
            "No files found matching parameters: filename=%s, directory=%s",
            filename,
            directory,
        )

    return file_list


class RegexFileCommand(ABC):
    @classmethod
    def add_arguments(cls, parser):
        parser.add_argument(
            "-f",
            "--filename",
            type=str,
            help="The name or glob regex for the file(s) to run against.",
        )
        parser.add_argument(
            "-d",
            "--directory",
            type=str,
            help="The directory for the file(s) to run against.",
        )

    def handle(self, *_, **kwargs):
        file_list = get_file_list(**kwargs)
        if not file_list:
            logger.info("No files to process. Exiting...")
            sys.exit(0)

        logger.info(f"Processing {len(file_list)} files...")
        self.run_command(file_list, **kwargs)

    @classmethod
    def run_command(cls, file_list: List[str], **_):
        raise NotImplementedError("run_command has not been implemented")
