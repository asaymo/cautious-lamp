#author: Adri
#date: 11/3/25
#description: A practice script to refresh my python skills
from matplotlib import pyplot as plt

# example values
x_values = [1, 2, 3, 4]
y_values = [5, 4, 6, 2]

# plt.plot(x_values, y_values)
# 
plt.scatter(x_values, y_values)

more_x_vals = [1, 2, 3, 4, 5]
more_y_vals = [6, 7, 8, 9, 10]

plt.plot(more_x_vals, more_y_vals, color="lavender")
plt.title("Sample Plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()