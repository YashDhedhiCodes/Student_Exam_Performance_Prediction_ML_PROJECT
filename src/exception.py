import sys

def error_message_detail(error, error_detail):
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script: [{0}], line: [{1}], error message: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(str(error))  # Pass the original error message to base class
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message
