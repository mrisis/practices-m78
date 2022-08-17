import sys
option=sys.argv[1::]

print(option)
sum=0
if option:
    for i in option:
        sum += int(i)

avg = sum / len(option)
print(avg)

