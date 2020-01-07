from ex_15_6 import Die
import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for x in range(1000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(x) for x in range(3, max_result+1)]

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [x for x in range(3,18)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')