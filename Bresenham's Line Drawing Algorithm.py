import matplotlib.pyplot as plt
import numpy as np


x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
x2 = int(input("Enter the value of x2: "))
y2 = int(input("Enter the value of y2: "))

dy = y2 - y1
dx = x2 - x1

p0 = 2 * dy - dx

if abs(dy) > abs(dx):
    steps = abs(dx)
else:
    steps = abs(dy)

xcor = []
ycor = []
i = 0

while i < steps:
    i = i + 1
    xcor.append(x1)
    ycor.append(y1)
    if p0 >= 0:
        x1 = x1 + 1
        y1 = y1 + 1
        p0 = p0 + 2 * dy - 2 * dx
    else:
        x1 = x1 + 1
        p0 = p0 + 2 * dy

print("x1:", x1, "y1:", y1)
plt.plot(xcor, ycor, marker="D", color="green")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Bresenham's Line Drawing Algorithm")
plt.show()
