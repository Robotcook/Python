from datetime import datetime

class Person(object):
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def full_name(self):
        return self.first_name + " " + self.last_name

    def age(self):
        return datetime.today().year - self.birth_year

class Customer(Person):
    def __init__(self, first_name, last_name, phone_number, birth_year, email, customer_number):
        Person.__init__(self, first_name, last_name, phone_number, birth_year, email)
        self.customer_number = customer_number

robert = Customer(first_name="Robert", last_name="Barabas", phone_number="1234591", birth_year=1986, email="rb@gmx.at", customer_number="1234")

marissa = Person(first_name="Marissa", last_name="Mayer", phone_number="83483204032", birth_year="1978", email="marissa@yahoo.com")

bruce = Person(first_name="Bruce", last_name="Wayne", phone_number="902432309443", birth_year="1939", email="bruce@batman.com")

print robert.first_name
print marissa.email

contact_book = [robert, marissa, bruce]

for person in contact_book:
    if type(person) is Customer:
        print person.full_name()
        print person.birth_year
        print person.age()
        print person.email
        print ""