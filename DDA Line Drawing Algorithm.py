import matplotlib.pyplot as plt
x1=int(input("Enter the value of X1:"))
y1=int(input("Enter the value of Y1:"))
x2=int(input("Enter the value of X2:"))
y2=int(input("Enter the value of Y2:"))
dy=y2-y1
dx=x2-x1
m=dy/dx
if dy>dx:
  steps=dy
else:
  steps=dx
xcor=[]
ycor=[]

i=0
while i<steps:
  i=i+1
  if m<1:
    x1=x1+1
    y1=y1+m
  elif m>1:
    x1=x1+1/m
    y1=y1+1
  else:
    x1=x1+1
    y1=y1+1
  xcor.append(x1)
  ycor.append(y1)
  print("X1:",x1,"Y1:",y1)
plt.plot(xcor,ycor,marker="o",color="red")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("DDA Algorithm")
plt.show()
