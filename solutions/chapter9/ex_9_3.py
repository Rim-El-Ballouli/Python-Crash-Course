class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print('User ' + self.first_name  + ' ' + self.last_name + ' is ' + str(self.age) +' years old')

    def greet_user(self):
        print('Hello ' + self.first_name)

user1 = User('Thomas','Dazly', 20)
user1.describe_user()
user1.greet_user()

user2 = User('Mathieu','Doglas', 40)
user2.describe_user()
user2.greet_user()
