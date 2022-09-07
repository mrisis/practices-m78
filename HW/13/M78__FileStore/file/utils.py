import re
from file.exception import *



class Validator:
    @staticmethod
    def name_validation(value):
        reg = re.compile(r'[a-zA-Z_0-9]')
        if reg.match(value):
            return value
        else:
            raise FilnameError("file name is not valid")

    @staticmethod
    def path_validation(value):
        reg = re.compile(r'[A-Za-z]')
        if reg.match(value):
            return value
        else:
            raise PathError("path file is not valid")







