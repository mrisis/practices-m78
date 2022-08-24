import re
import json


class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        reg = re.compile(r'[a-zA-Z_]{4,14}')
        if reg.match(value):
            self._name = value
        else:
            raise ValueError("name is not valid")


    @property
    def email(self):
        return self._email


    # [a-z0-9]+@[a-z]+\.edu\.[a-z]{2,3}‏

    @email.setter
    def email(self, value):
        reg = re.compile(r'[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA-Z]{2,3}')
        if reg.match(value):
            self._email = value
        else:
            raise ValueError("email address is not valid")


    @property
    def phone(self):
        return self._phone


    @phone.setter
    def phone(self, value):
        reg = re.compile(r'((09\d{9}$)|(\+989\d{9}$))')
        if reg.match(value):
            self._phone = value
        else:
            raise ValueError("phone number is not valid")


p1 = User("reZa", "rezaamin@gmail.com", "09130075401")
