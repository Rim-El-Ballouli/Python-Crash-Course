from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,int(self.sides)))


die1 = Die()
for i in range(1, 10):
    die1.roll_die()

die2 = Die(10)
for i in range(1, 10):
    die2.roll_die()
