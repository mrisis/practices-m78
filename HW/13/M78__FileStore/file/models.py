from core.models import DBModel
from core.managers import db1
from file.utils import Validator


class File(DBModel):
    TABLE = 'files'
    PK = 'id'

    def __init__(self, filename, path, id=None):
        self.filename = Validator.name_validation(filename)
        self.path = Validator.path_validation(path)

        if id:
            self.id = id

    def register_file(self, dbmanger=db1):
        return dbmanger.create(self)


# def create_file(dbmanager=db1):
#     filename = input("enter your file name :")
#     path = input("enetr yuor path file :")
#     file1 = File(filename, path)
#     file1.register_file(dbmanager)

class Comments(DBModel):
    TABLE = 'comments'
    PK = 'id'

    def __init__(self, id_file, text, id=None):
        self.id_file = id_file
        self.text = text
        if id:
            self.id = id

    def register_comment(self, dbmanger=db1):
        return dbmanger.create(self)


def create_comments(dbmanager=db1):
    id_file = input("enter your id_file :")
    text = input("enetr your text for file :")
    comment1 = Comments(id_file, text)
    comment1.register_comment(dbmanager)


def create_file(dbmanager=db1):
    filename = input("enter your file name :")
    path = input("enetr yuor path file :")
    file1 = File(filename, path)
    file1.register_file(dbmanager)


def show_file():
    files = db1.read_all(File)
    for file in files:
        print(file)
    return files

# show_file(db1, File)
