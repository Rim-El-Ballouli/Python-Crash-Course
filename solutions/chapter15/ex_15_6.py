from random import randint
import pygal

class Die():
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)




die_1 = Die()
die_2 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for x in range(1000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(x) for x in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [x for x in range(2,13)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')


