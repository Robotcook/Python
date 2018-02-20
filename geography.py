import random
country_capital_dict = {"Slovenia": "Ljubljana", "Austria": "Vienna", "Hungary": "Budapest", "Germany": "Berlin"}

def main():

    while True:
        selected_country = country_capital_dict.keys()[random.randint(0,2)]

        guess = raw_input("What is the capital of %s? " % selected_country)

        check_guess(guess, selected_country)

        again = raw_input("Would you like to continue this game? (yes/no)")

        if again == "no":
            break

    print ("END")
    print ("_________________________________________________________________")

def check_guess(guess, country):
    correct_answer = country_capital_dict[country]

    if guess == correct_answer:
        print("You are right!")
        return True
    else:
        print ("You are wrong! The capital of %s is %s." % (country, correct_answer))
        return False

if __name__=="__main__":
    main()