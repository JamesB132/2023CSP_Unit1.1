import turtle as trtl
painter = trtl.Turtle()

color = input("What color would you like the circle to be? ")

painter.pencolor(color)
painter.fillcolor(color)
painter.begin_fill()
painter.circle(40, 360, 4)
painter.end_fill()
