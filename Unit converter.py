print "Hello User! I convert kilometers into miles!"

while True:
    print "Please enter kilometers!"
    km = float(raw_input("Kilometers: "))

    miles = km * 0.621371

    print "{} kilometers are {} miles.".format(km, miles)

    wh = raw_input ("Do you want another conversion? (y/n) ")
    if wh == "y":
        continue
    else:
        print "Goodbye!"
        break