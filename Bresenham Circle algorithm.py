import matplotlib.pyplot as plt

r = 10
x = 0
y = r
p = 1 - r

points = []

while x <= y:

    if p < 0:
        x=x+1
        y=y
        p=p+4*x+6
    else:
        x=x+1
        y=y-1
        p=p+4*(x-y)+10

    points.append((x, y))
    points.append((y, x))
    points.append((-x, y))
    points.append((-y, x))
    points.append((-x, -y))
    points.append((-y, -x))
    points.append((x, -y))
    points.append((y, -x))

# Separate x and y coordinates
x_vals, y_vals = zip(*points)

plt.scatter(x_vals, y_vals)
#plt.gca().set_aspect('equal')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Bresenham Circle algorithm")
plt.grid(True)
plt.show()
