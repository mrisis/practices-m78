from user import User
from bank import BankAccount
from cards import *
from datetime import datetime
from admin import *
from tripe import Tripe

users = []

while True:
    print("User registration ---> 1")
    print("Bank account management ---> 2")
    print("Metro travel registration ---> 3")
    print("Exit ---> 0")
    num = int(input("Select your item : "))
    if num == 1:
        print("User ---> 1")
        print("Admin ---> 2")
        number = int(input("Select your item : "))
        if number == 1:
            name = input("Enter your name")
            family = input("Enter your family")
            bank_name = input("Enter your bank")
            balance = int(input("Enter your balance"))
            b = BankAccount(bank_name, balance)
            user12 = User(name, family, b)
            users.append(user12)
            new_list = []


            while True:
                print('''
                SingleTicket ---> 1
                CreditCart ---> 2
                Card_expiration_date ---> 3
                Exit ---> 0
                ''')
                num = int(input("Select your Card : "))
                if num == 1:
                    single = SingleTicket()
                    new_list.append(single)
                    break
                elif num == 2:
                    balance = int(input("Enter your Balance : "))
                    credit = CreditCard(balance)
                    new_list.append(credit)
                    break

                elif num == 3:
                    balance = int(input("Enter your Balance : "))
                    expiration_date = datetime(*eval(input("Enter your date : ")))
                    card_ed = Card_expiration_date(balance, expiration_date)
                    new_list.append(card_ed)
                    # create new user
                    user1 = User(name, family, b, new_list)

                    break
                elif num == 0:
                    break

        elif number == 2:
            name = input("Enter your Admin Name : ")
            family = input("Enter your Admin Family : ")
            username = input("Enter your Username : ")
            password = input("Enter your Password : ")

            admin1 = Admin(name, family, username, password)
            break
    elif num == 2:
        bank_name = input("Enter your bank : ")
        balance = int(input("Enter your balance : "))

        bank_acc = BankAccount(bank_name, balance)
       #####

    elif num == 3:
        origin = input("Enter your origin : ")
        destination = input("Enter your destination : ")
        cost = int(input("Enter your cost of trip : "))
        traveller = users[0]
        ticket = input("Enter your ticket : ")

        tripe1 = Tripe(origin, destination, cost, traveller, ticket)

    elif num == 0:
        break

    else:
        raise ValueError("Invalid number")
