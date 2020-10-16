class Restaurant():
    def __init__(self, restuarant_name, cuisine_type):
        self.name = restuarant_name
        self.type = cuisine_type
    def describe_restuarant(self):
        print("The Restuarant name is" + self.name.title())
        print("Cuisine type is" + self.type.title())
    def open_restuarant(self):
        print("In operation")

my_restuarant = Restaurant('金拱门','快餐')
my_restuarant.describe_restuarant()
my_restuarant.open_restuarant()

    