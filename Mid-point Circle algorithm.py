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
        p += 2 * x + 1
    else:
        x=x+1
        y=y-1
        p += 2 * (x - y) + 1

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
plt.title("Mid-point Circle algorithm")
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
r = 10
x = 0
y = r
p = 1 - r
xcor=[]
ycor=[]
while x <= y:

    if p < 0:
        x=x+1
        y=y
        p += 2 * x + 1
    else:
        x=x+1
        y=y-1
        p += 2 * (x - y) + 1

    xcor.append(x)
    ycor.append(y)
    xcor.append(y)
    ycor.append(x)
    xcor.append(x)
    ycor.append(-y)
    xcor.append(y)
    ycor.append(-x)
    xcor.append(-x)
    ycor.append(-y)
    xcor.append(-y)
    ycor.append(-x)
    xcor.append(-x)
    ycor.append(y)
    xcor.append(-y)
    ycor.append(x)

plt.scatter(xcor,ycor)
#plt.gca().set_aspect('equal')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Mid-point Circle algorithm")
plt.grid(True)
plt.show()
