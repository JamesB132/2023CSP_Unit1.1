import turtle as trtl

ryan = trtl.Turtle()
jack = trtl.Turtle()
quandale = trtl.Turtle()
james = trtl.Turtle()
josh = trtl.Turtle()
zach = trtl.Turtle()

turtleList = [ryan, jack, quandale, james, josh, zach]

x = -100
y = 0

for turtle in turtleList:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    x = x + 20

for turtle in turtleList:
    turtle.left(90)
    turtle.forward(300)

wn = trtl.Screen()
wn.mainloop()
