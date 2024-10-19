# Monte-Carlo-Elipse-Python


This Python script uses a Monte Carlo method to estimate the area of an ellipse by randomly generating points within a bounding rectangle. The ellipse is defined by its semi-major axis (a) and semi-minor axis (b), while the rectangle encloses the ellipse, and its dimensions (length and height) match the extreme coordinates of the ellipse.

First, the script randomly generates n points inside the rectangle using uniform distributions for the x and y coordinates. These points are then tested to determine whether they fall inside the ellipse using the ellipse equation, normalizing the x and y coordinates by the semi-major and semi-minor axes. If a point satisfies the ellipse equation, it's counted as being within the ellipse.

The area of the rectangle is calculated by multiplying its length and height. The estimated area of the ellipse is then determined by multiplying the fraction of points inside the ellipse by the area of the rectangle. This Monte Carlo estimate is compared to the analytical solution for the area of the ellipse, given by 
𝜋
⋅
𝑎/2
⋅
𝑏/2
 .

Finally, the relative error is computed as the percentage difference between the estimated area and the analytical area. The results, including the number of points in both the rectangle and ellipse, the estimated and analytical areas, and the relative error, are displayed alongside the plot. The plot itself shows the rectangle and ellipse, as well as the randomly generated points. To better understand the estimation, look at the generated plot below, which visually demonstrates the method.

![Monte_carlo](https://github.com/user-attachments/assets/079e526d-dfa0-48e7-8436-7d752168f72a)
