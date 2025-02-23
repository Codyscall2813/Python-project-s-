import turtle as tu

# Initialize turtle and screen
t = tu.Turtle()
s = tu.Screen()
s.bgcolor("black")
t.speed(2)

# Draw a filled quadrilateral
t.penup()
t.goto(-50, 60)
t.pendown()
t.color("#00adef")
t.begin_fill()
for point in [(-50, 60), (100, 100), (100, -100), (-50, -60)]:
    t.goto(point)
t.end_fill()

# Draw vertical line
t.color("black")
t.width(10)
t.penup()
t.goto(15, 100)
t.pendown()
t.goto(15, -100)

# Draw horizontal line
t.penup()
t.goto(100, 0)
t.pendown()
t.goto(-100, 0)

# Keep the window open until closed by the user
s.mainloop()
