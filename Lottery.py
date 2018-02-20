import random

def generate_lottery_numbers(quantity):
    lottery_numbers = []

    while True:

        if len(lottery_numbers) == quantity:
            break

        numbers = random.randint(1, 45)

        if numbers not in lottery_numbers:
            lottery_numbers.append(numbers)

        lottery_numbers.sort()

    print ("Here are your lottery numbers:")
    return lottery_numbers

def main():
    print "Welcome to the Lottery numbers generator!"

    quantity_question = raw_input("Please enter how many random numbers would you like to have: ")

    try:
        quantity_num = int(quantity_question)
        print generate_lottery_numbers(quantity_num)
    except ValueError:
        print "Please enter a number."

    print "Good Luck!"

if __name__ == "__main__":
    main()