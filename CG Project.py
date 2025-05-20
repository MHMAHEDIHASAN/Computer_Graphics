import turtle
t = turtle.Turtle()
t.speed()
turtle.bgcolor("light blue")

# 🌸 প্রতিটা পাপড়ি (no loop)
t.color("Purple")

# পাপড়ি ১+++++
t.penup()
t.goto(35, -35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# পাপড়ি 2+++
t.penup()
t.goto(50, 0)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# পাপড়ি 3+++
t.penup()
t.goto(35, 35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 4+++
t.penup()
t.goto(0, 50)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 5++++
t.penup()
t.goto(-35, 35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# পাপড়ি 6
t.penup()
t.goto(-50, 0)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 7
t.penup()
t.goto(-35, -35)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# পাপড়ি 8
t.penup()
t.goto(0, -45)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()


# 🌼 ফুলের কেন্দ্র
t.penup()
t.goto(0, 0)
t.color("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# 🌱 ডাঁটা (লাঠি) - এখন ঠিক পাপড়ির নিচে
t.penup()
t.goto(0, -46)
t.setheading(-90)
t.pendown()
t.color("green")
t.pensize(6)
t.forward(160)

# 🌿 বড় পাতা (ডাঁটার সাথে লাগানো)
t.penup()
t.goto(0, -110)
t.setheading(-25)
t.pendown()
t.color("forest green")
t.begin_fill()
t.circle(65, 90)
t.left(90)
t.circle(65, 90)
t.end_fill()


t.penup()
t.goto(0, -80)
t.setheading(135)
t.pendown()
t.color("forest green")
t.begin_fill()
t.circle(65, 90)
t.left(90)
t.circle(65, 90)
t.end_fill()



# 🪴 টব (ডাঁটার নিচে)
t.penup()
t.goto(-30, -210)  # টবের অবস্থান
t.setheading(0)
t.color("saddlebrown")
t.begin_fill()
t.pendown()
t.forward(60)      # নিচের অংশ
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.end_fill()

# টবের উপরের রিম (বাঁকা অংশ)
t.penup()
t.goto(-40, -190)
t.setheading(0)
t.color("peru")
t.begin_fill()
t.pendown()
t.forward(80)
t.left(90)
t.forward(10)
t.left(90)
t.forward(80)
t.left(90)
t.forward(10)
t.end_fill()

t.penup()
t.goto(100, 150) # Moved sun to top right
t.pendown()
t.color("orange") # Changed sun color to orange
t.begin_fill()
t.circle(40)     # Slightly smaller sun
t.end_fill()

t.hideturtle()
turtle.done()
