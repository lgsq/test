class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + "is now sitting.")
    def roll_over(self):
        print(self.name.title() + "rolled over!")

class Dog:
    my_dog = Dog('willie', 6)
    your_dog = Dog('luck', 3)


    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + "yeras old.")
    my_dog.sit()
    my_dog.roll_over()


    print("\nYour_dog's name is " + your_dog.name.title() + ".")
    print("Your_dog is" + str(your_dog.age) + "years old.")
    your_dog.sit()
    your_dog.roll_over()

