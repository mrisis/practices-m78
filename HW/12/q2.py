import re
import json


class User:
    list_of_user = []

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.__class__.list_of_user.append(self)

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

    # [a-z0-9]+@[a-z]+\.[a-z]{2,3}

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



    @classmethod
    def dump_json(cls):
        with open("users.json", 'w') as f:
            users_in_list = {'user': []}
            for i in cls.list_of_user:
                user = {'name': i.name,'email': i.email,'phone': i.phone}
                users_in_list.get('user').append(user)
            json.dump(users_in_list,f,indent=2)
    @classmethod
    def load_json(cls):
        with open("users.json",'r') as f :
            text=json.load(f)
        return text





p2 = User("reza", "rezaamin8889@gmail.com", "09130075401")
p3 = User("mamad mahdi", "mamadmahdi@gmail.com", "09130075402")

User.dump_json()
print(User.load_json()['user'])



