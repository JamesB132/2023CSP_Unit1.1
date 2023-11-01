import turtle as trtl

"""
Set up turtle
Set up the Scale
Draw the Outline of the House
    Create a loop to draw the lower and upper level of the house
        Then, set the scale to be smaller (for upper level)
    Fill Color
Create the Windows
    Go to a specific value
        Use loops to create horizontal lines, shutters
        Use an if statement (if # of horizontal lines is enough, goto next spot)
Create the garage
    Same method as windows, create loops for the lines. 
    If amount of lines is enough, then create the windows above
    
"""
trtl.penup()
trtl.goto(0, -150)
trtl.pendown()
theta = 0
iteration = 0
scale = 1
for frame in range (2):
    trtl.forward(200)
    trtl.left(90 - theta)
    trtl.forward(150)
    trtl.right(90 - theta)
    trtl.forward(35)
    if (iteration == 1):
        trtl.right(180)
        trtl.forward(440)
        trtl.left(180)
        trtl.forward(440)
        trtl.right(145)
        trtl.forward(80)
        trtl.right(35)
        trtl.forward(325.6)
    else:
        trtl.left(145)
        trtl.forward(80)
        trtl.left(35 - theta)
        trtl.forward(325.6)
        
    trtl.penup()
    trtl.goto(0, -150)
    trtl.pendown()
    theta = 180
    iteration = 1


scale = 0.6
trtl.penup()
trtl.goto(0, 45.886)
trtl.pendown()
theta = 0
iteration = 0

for frame in range (2):
    trtl.forward(200 * scale)
    trtl.left(90 - theta)
    trtl.forward(150 * scale)
    trtl.right(90 - theta)
    trtl.forward(35 * scale)
    if (iteration == 1):
        trtl.right(145)
        trtl.forward(80 * scale)
        trtl.right(35)
        trtl.forward(325.6 * scale)
    else:
        trtl.left(145)
        trtl.forward(80 * scale)
        trtl.left(35 - theta)
        trtl.forward(325.6 * scale)
    trtl.penup()
    trtl.goto(0, 45.886)
    trtl.pendown()
    theta = 180
    iteration = 1

wn = trtl.Screen()
wn.mainloop()