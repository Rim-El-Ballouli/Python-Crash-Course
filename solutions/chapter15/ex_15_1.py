import matplotlib.pyplot as plt

x_values = range(1,5)
y_values = [x**3 for x in range(1,5)]
plt.plot(x_values, y_values)
plt.title('Cubes Of Numbers')
plt.xlabel('number')
plt.ylabel('cube value')
plt.show()

x_values = range(1,5000)
y_values = [x**3 for x in range(1,5000)]
plt.plot(x_values, y_values)
plt.title('Cubes Of Numbers')
plt.xlabel('number')
plt.ylabel('cube value')
plt.show()
