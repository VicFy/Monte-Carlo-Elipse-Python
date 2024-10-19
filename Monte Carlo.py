import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Ellipse
import numpy as np

n = 100000  # Number of points.

# Parameters for the rectangle
xi, xf, yi, yf = -3, 3, -1.5, 1.5  # Start and end values.
l, h = 6, 3  # Length and height.

# Parameters for the ellipse
a, b = 4, 2  # Axes lengths.
x_c, y_c = 0, 0  # Center coordinates of the ellipse.

# Plot the graph
fig, ax = plt.subplots()

ellipse = Ellipse((x_c, y_c), a, b, angle=0, ec='blue', fc='none')
rectangle = Rectangle((xi, yi), l, h, angle=0, ec='blue', fc='none')

ax.add_patch(ellipse)
ax.add_patch(rectangle)

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

points = np.zeros((n, 2))  # Matrix to store the coordinates of the points.

def generate_x(xi, xf, n):
    return np.random.uniform(xi, xf, n)

def generate_y(yi, yf, n):
    return np.random.uniform(yi, yf, n)

# Generate the numbers
x = generate_x(xi, xf, n)
y = generate_y(yi, yf, n)

points[:, 0] = x
points[:, 1] = y

rect_count = n
ellipse_count = 0

# Count how many points are inside the ellipse
x_h = (points[:, 0] - x_c)**2 / (a / 2)**2
y_g = (points[:, 1] - y_c)**2 / (b / 2)**2
ellipse_count = ((x_h + y_g) <= 1).sum()

rect_area = l * h
ellipse_area = (ellipse_count / rect_count) * rect_area

# Plot the points
for i in range(n):
    ax.plot(x[i], y[i], marker='o', markersize=0.25, color='red')

analy_ellipse = np.pi * (a / 2) * (b / 2)  # Analytical solution for the area of the ellipse

rel_error = round(((ellipse_area - analy_ellipse) / analy_ellipse) * 100, 2)  # Calculate the relative error for the area of the ellipse

# Add text annotations
plt.figtext(0.35, 0.825, "Points in the rectangle: {}".format(rect_count), ha='left')
plt.figtext(0.35, 0.785, "Points in the ellipse: {}".format(ellipse_count), ha='left')
plt.figtext(0.35, 0.745, "Rectangle area: {}".format(rect_area), ha='left')
plt.figtext(0.35, 0.705, "Ellipse area: {:.2f}".format(ellipse_area), ha='left')
plt.figtext(0.35, 0.275, "Relative error: {}%".format(rel_error), ha='left')
plt.figtext(0.35, 0.235, "Analytical ellipse area: {:.2f}".format(analy_ellipse), ha='left')

plt.gca().set_aspect('equal', adjustable='box')  # Keep the aspect ratio.

plt.show()