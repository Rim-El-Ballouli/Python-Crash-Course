from user import User

class Admin(User):
    def __init__(self, firstN, lastN, *privileges):
        super().__init__(firstN, lastN)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

usrAdmin = Admin('Adrean', 'Park', "can add post", "can delete post", "can ban user")
usrAdmin.show_privileges()