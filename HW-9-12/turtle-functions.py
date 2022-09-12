import turtle

def turtle_position(t, x, y, w, color):
  t.penup()
  t.goto(x,y)
  t.width(w)
  t.color(color)
  t.pendown()


def square(t, x, y, w, color, sidelen):
# set the location, color, width and side liength ( this comment gets removed once it gets pushed to git)
  turtle_position(t,x, y, w, color)
  for i in range(4):
    t.forward(sidelen)
    t.right(90)


def triangle(t, x, y, w, color, sidelen):
  turtle_position(t,x, y, w, color)
  for i in range(3):
    t.forward(sidelen)
    t.left(120)

def hexagon(t, x, y, w, color, sidelen):
  turtle_position(t,x, y, w, color)
  for i in range(6):
    t.forward(sidelen)
    t.left(60)

def ngon(t,sides,x,y,color,width,sidelen):
  turtle_position(t,x, y, width, color)
  for i in range(sides):
    t.forward(sidelen)
    t.left(360/sides)
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
triangle(squirt, 10,10,8, "green", 50)
hexagon(crush, 15,15, 9, "orange", 70)
ngon(crush,10, 40,40, "red",10, 70)
wn.exitonclick()
wn.mainloop()

# draw a square
