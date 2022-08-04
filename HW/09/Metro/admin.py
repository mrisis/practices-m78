from user import BaseUser
from uuid import uuid4
import pickle
from log import logger


class Admin(BaseUser):
    def __init__(self, name, family, username, password):
        super().__init__(name, family)
        self.id = uuid4().int % 10000
        self.username = username
        self.__password = password
        logger.name = __name__
        logger.info(f"admin user was created with name= {self.username}")
        self.add_to_file(f"ID :{self.id} your Username is : {self.username}")
        print(f"ID :{self.id} your Username is : {self.username}")


    def show_password(self):
        return self.__password
        
        
    def add_to_file(self, value):
        with open("admins.pickle", "ab") as f:
            pickle.dump(value, f)
            f.write(b"\n")

    def __repr__(self):
        return f"Family : {self.family} your Username is : {self.username}"
            
            

# m1 = Admin("ali", "ahmadi", "ali789", "aliali")


