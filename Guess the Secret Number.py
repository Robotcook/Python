import random

print ("Welcome to the Guess the secret Number game!")

def main():
    secret = random.randint(1, 30)

    for x in range(5, 0, -1):
        print ("You have %s tries!" % x)
        guess = int(raw_input("Guess the secret number between 1 and 30: "))

        if guess == secret:
            print("CONGRATULATIONS, you got it!!!! It is %s!" % secret)
            print("It only took you %s tries!" % x)
            break
        elif guess > secret:
            print("Your guess is wrong, your number is too high!")
        else:
            print("Your guess is wrong, your number is too low!")

    if guess != secret:
        print ("Sorry, you reached the maximum tries!")
        print ("The secret number was %s." % secret)

if __name__ == "__main__":
    main()