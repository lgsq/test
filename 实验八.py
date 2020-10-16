class user():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describr_user(self):
        print("Your First name is" + self.first_name.title())
        print("Your Last name is" + self.last_name.title())
    def greet_user(self):
        print("Hello" + self.first_name.title() + self.last_name.title())
    usera = ('mx' 'a')
    userb = ('cd' 'n')

    usera.describr_user()
    usera.greet_user()
    userb.describr_user()
    userb.greet_user()