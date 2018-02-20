print ("Welcome to the Restaurant Menu Program!")

menu = {}

while True:
    input_dish = raw_input ("Please enter the name of the new dish: ")
    input_price = raw_input ("Please enter the price for '%s': " % input_dish)
    menu[input_dish] = input_price

    new = ""
    while new != "y" and new != "n":
        new = raw_input ("Would you like to add another dish? (y/n) ").lower()

    if new == "n":
        break

print "Menu: %s" % menu

with open("menu.txt", "w+") as menu_file:
    for dish in menu:
        menu_file.write("%s, %s EUR\n " % (dish.capitalize(), menu[dish]))

print "Thank you! Goodbye!"