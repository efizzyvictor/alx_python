import random
number = random.randint(-10, 10)
if  number > 0:
    print("{} is positive" .format(number), "\n" )
elif number == 0:
    print("{} is zero" .format(number), "\n")
elif number < 0:
    print("{} is negative" .format(number), "\n")
print()