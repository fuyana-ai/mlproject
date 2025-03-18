import sys

def error_message_detail(error, error_detail: sys):
    """
    Constructs a detailed error message including the script name, line number, and error message.
    
    Args:
        error: The error/exception object.
        error_detail: sys.exc_info() object containing exception details.
    
    Returns:
        str: A formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get exception traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    line_number = exc_tb.tb_lineno  # Get the line number where the error occurred
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    """
    Custom exception class to include detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Args:
            error_message: The error message.
            error_detail: sys.exc_info() object containing exception details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the custom error message.
        """
        return self.error_message