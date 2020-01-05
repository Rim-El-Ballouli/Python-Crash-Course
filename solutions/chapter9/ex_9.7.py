class User():
    def __init__(self, first_name, last_name, *privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.privileges = privileges

    def describe_user(self):
        print('User ' + self.first_name  + ' ' + self.last_name)

    def greet_user(self):
        print('Hello ' + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def show_privileges()


class Admin(User):
    def __init__(self, firstN, lastN, *privileges):
        super().__init__(firstN,lastN)
        self.privileges = Privileges(privileges)

usrAdmin = Admin('fn', 'ln', "can add post", "can delete post", "can ban user")
usrAdmin.privileges.show_privileges()