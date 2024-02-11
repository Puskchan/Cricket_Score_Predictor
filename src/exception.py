import sys
from src.logger import logging


def error_msg_detail(error, error_detail:sys):
    _,_, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = (f"Error occured in python script [{file_name}] at line [{exc_tb.tb_lineno}] | Error -> [{str(error)}]")

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys) -> None:
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg, error_detail=error_detail)
    
    def __str__(self):
        return self.error_msg