def is_armstrong(num):
    #Convert to string for scrollable
    number= str(num)

    num=len(number)
    counter=0
    for i in number:
        counter += int(i) ** num

    if counter == int(number):
        yield True
    else:
        yield False


s=is_armstrong(153)
print(next(s))  # true

s1=is_armstrong(987)
print(next(s1)) # false


