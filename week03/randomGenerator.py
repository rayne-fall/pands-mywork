# random generator
# author: Sylvia Chapman Kent
# prints a random number within a range chosen by the user

import random

x = int(input("Enter the lower end of your range (eg. if range is between 1 and 10, enter 1): "))
y = int(input("Enter the upper end of your range (eg. if range is between 1 and 10, enter 10): "))

number = random.randint(x,y)
print(f"Here is a random number: {number}")
