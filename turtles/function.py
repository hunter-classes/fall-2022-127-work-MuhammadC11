import turtle

def square(t, x, y, w, color, sidelen):
# set the location, color, width and side liength
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range(4):
    t.forward(sidelen)
    t.right(90)


wn = turtle.Screen()
crush = turtle.Turtle()
squirt = turtle.Turtle()
squirt.penup()
squirt.goto(100,100)
squirt.pendown()
squirt.color("red")
squirt.width(5)

square(crush, 20, 30, 5, "blue", 100)
square(squirt , 40, 50, 5, "red", 100)
wn.exitonclick()
wn.mainloop()

# draw a square
