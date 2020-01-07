from ex_15_6 import Die
import pygal

die_1 = Die()
die_2 = Die()
# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for x in range(1000)]

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