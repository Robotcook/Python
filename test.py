
import random

number_list = []

print "Welcome to the Lottery Numbers Generator"

numbers = int(raw_input("Please enter how many random numbers would you like to have: "))

for x in range(numbers):

    rand_number = random.randint(1, 10)

    while rand_number in number_list:
        rand_number = random.randint(1, 10)

    if rand_number not in number_list:
        number_list.append(rand_number)

print number_list