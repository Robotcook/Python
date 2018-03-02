class Vehicles(object):
    def __init__(self, brand, model, kilometers, service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service_date = service_date
        self.in_use = False

    def vehicles_full_name(self):
        return self.brand + " " + self.model

def show_list(list_vehicles):
    for index, vehicles in enumerate(list_vehicles):
        print ("ID:") + str(index)
        print vehicles_full_name()
        print vehicles.kilometers()
        print vehicles.service_date()


def check_out_vehicle(list_vehicles):

    print ("Select the number of the cat you would like to check out:")

    for index, car in enumerate(list_vehicles):
        if not car.in_use:
            print ("str(index) + " + car.get_full_name()

def main():
    print ("Welcome to the Vehicles Manager Program!")

    list_vehicles = []

    with open("vehicles.txt", "r") as v_file:


    while True:
        print ("")
        print ("Please choose one of the options below!")
        print ("")
        print ("a) Show me all vehicles")
        print ("b) Edit kilometers")
        print ("c) Edit service date")
        print ("d) Add new vehicle")
        print ("e) Check out vehicle")
        print ("f) Quit")
        print ("")

        pick = raw_input("Which option would you like to choose? (a, b, c, d, e)")

        print("")

        if pick.lower() == "a":
            show_list(list_vehicles)
        elif pick.lower() == "b":
            edit_km(list_vehicles)
        elif pick.lower() == "c":
            edit_date(list_vehicles)
        elif pick.lower() == "d":
            add_new_vehicle(list_vehicles)
        elif pick.lower() == "e":
            check_out_vehicle(list_vehicles)
        elif pick.lower() == "f":
            print("Thanks for using VMP. Good bye!")
            save(list_vehicles)
            break
        else:
            print ("Sorry something is wrong with your input. Please enter a, b, c, d or e!")

if __name__ == main():
    print main