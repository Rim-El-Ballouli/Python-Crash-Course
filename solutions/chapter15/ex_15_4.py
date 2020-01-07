import matplotlib.pyplot as plt
from modified_random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, lineWidth=1)

    # Remove the axes.
    plt.axis('off')

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break