import random
number = random.randint(-10000, 10000)
output=str(number)[-1]
if number > 0:
    f_output= int(output) * 1
else:
    f_output = int(output) * (-1)
if (f_output) > 5: 
    print(f"last digit of {number} is {f_output} and is greater than 5", "\n")
elif int(f_output) == 0: 
    print(f"last digit of {number} is {f_output} and is 0", "\n")
elif (f_output) < 6 and output !=0:
     print(f"last digit of {number} is {f_output} and is less than 6 and not 0","\n")
