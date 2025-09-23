import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    Build a descriptive error message that captures the script name, line number,
    and the original error string for easier debugging.
    """
    _, _, exc_tb = error_detail.exc_info()  # Unpack the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # File where the exception originated
    error_message = (
        "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    )

    return error_message


class CustomException(Exception):
    """Exception type that enriches messages with file name and line details."""

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Store the detailed error string so __str__ exposes contextual information
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



