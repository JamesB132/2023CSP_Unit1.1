#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors
color1 = "lime"
color2 = "blue"

wn = trtl.Screen()
height = 360 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle = 230
# experiment with the shape
seg = int(200/angle)

while (painter.ycor() < height):
  if (space % 5 == 0):
    painter.fillcolor(color1)
    painter.color(color1)
  else:
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(angle)
  painter.forward(4*space + 10) # experiment
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1

wn.mainloop()