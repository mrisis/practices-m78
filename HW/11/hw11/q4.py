import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument('-s', help='enter your number of start', type=int)
parser.add_argument('-e', help='enter your number of to end', type=int)
parser.add_argument('-g', help='number of guesses', type=int)

args = parser.parse_args()
number_of_random = 0
if args.s and args.e:
    number_of_random = random.randint(args.s, args.e)

random1 = number_of_random
print(random1)

for i in range(args.g):
    number_user = int(input("enter your number:"))
    if number_user == random1:
        print("you got")
        break
    elif number_user < random1:
        print("Enter Higher Number")
    elif number_user > random1:
        print("Enter Lower Number")

