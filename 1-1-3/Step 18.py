#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 21

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    rem = floor % 6
    if (rem == 0):
        painter.color("blue")
    if (rem == 1):
        painter.color("blue")
    if (rem == 2):
        painter.color("blue")
    painter.pendown()
    painter.forward(50)

    # location of next floor
    y = y + 5

x = -90
y = -150

    # iterate
for floor in range(num_floors):
        # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    rem = floor % 6
    if (rem == 0):
            painter.color("blue")
    if (rem == 1):
            painter.color("blue")
    if (rem == 2):
            painter.color("blue")
    painter.pendown()
    painter.forward(50)
        # location of next floor
    y = y + 5


x = -30
y = -150
for floor in range(num_floors):
            # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    rem = floor % 6
    if (rem == 0):
        painter.color("blue")
    if (rem == 1):
        painter.color("blue")
    if (rem == 2):
        painter.color("blue")

            # location of next floor
    y = y + 5
    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()