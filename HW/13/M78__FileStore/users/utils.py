import re
from users.exception import *

from core.managers import db1


class Validator:
    @staticmethod
    def username_validator(value):
        reg = re.compile(r'[a-zA-Z0-9_]')
        if reg.match(value):
            return value
        else:
            raise UsernameError("invalid username")

    @staticmethod
    def userfamily_validator(value: str):
        if value.isalpha():
            return value

        else:
            raise UserfamilyError("invalid userfamily")

    @staticmethod
    def password_validator(value):
        reg = re.compile(r'[a-zA-Z0-9_]{4,}')
        if reg.match(value):
            return value
        else:
            raise PasswordError("invalid password")
        



