from core.models import DBModel
from core.managers import db1
from users.utils import Validator
from core.utils import logger
from users.exception import *
from datetime import datetime


class User(DBModel):
    TABLE = 'users'
    PK = 'id'

    def __init__(self, username, userfamily, password, manager: bool = False, salesman: bool = False, id=None) -> None:
        self.username = Validator.username_validator(username)
        self.userfamily = Validator.userfamily_validator(userfamily)
        self.password = Validator.password_validator(password)
        self.manager = manager
        self.salesman = salesman

        if id:
            self.id = id

    def register(self, dbmanager):
        print( dbmanager.create(self))

    @classmethod
    def login(cls, dbmanager, id, password):
        user = dbmanager.read(cls, id)
        if password == user.password:
            print("you logged in system ")
            return user
        else:
            raise NormalUserError("password is worng")
    #
    # def buy_file(self):


def create_user(dbmanager=db1):
    username = input("ent your username:")
    userfamily = input("ent your userfamily:")
    password = input("ent your password:")
    manager = bool(input("manager: if yes enter somethings else just press enter:"))
    salesman = bool(input(" salesman:  if yes enter somethings else just press enter :"))
    user1 = User(username, userfamily, password, manager, salesman)
    user1.register(dbmanager)



def delete_user(dbmanager=db1):
    pk = input("enter your id for delete:")
    db1.delete(User, pk)


def log_in(dbmanager=db1):
    id = int(input("ent your id :"))
    password = input("ent your password:")
    user = User.login(dbmanager, id, password)
    logger.name = "users"
    logger.info(f"read a {user.__class__} with this information :{user.__dict__} ")
    return user


def log_in_salesman(dbmanager=db1):
    user = log_in(dbmanager)
    if user.salesman:
        print(f"wellcome {user.username}")
        return user
    else:
        raise SalesmanError("you not manager ")


def log_in_manager(dbmanager=db1):
    user = log_in(dbmanager)
    if user.manager:
        print(f"wellcome {user.username}")
        return user

    else:
        raise ManagerError("you not manager")


class ShopItem(DBModel):
    TABLE = 'order_item'
    PK = 'id'

    def __init__(self, id_user, id_file, payment_status, id_order=None, id=None):
        self.id_user = id_user
        self.id_file = id_file
        self.payment_status = payment_status
        self.id_order = id_order
        if id:
            self.id = id


class Order(DBModel):
    TABLE = 'orders'
    PK = 'id'

    def __init__(self, id_user, date, id=None):
        self.id_user = id_user
        self.date = date
        if id:
            self.id = id


def add_order(item: ShopItem, id_user):
    if item.payment_status:
        date = datetime.now().date()
        order1 = Order(id_user, date)
        db1.create(order1)
        return order1.id
    else:
        raise ValueError("order is not defind")


def buy_files():
    iduser = int(input("enter your id:"))
    idfile = int(input("enter your id_file:"))
    payment_status = bool(input("enter your status :"))
    item1 = ShopItem(iduser, idfile, payment_status)
    db1.create(item1)
    item1.id_order = add_order(item1, iduser)

    db1.update(item1)
