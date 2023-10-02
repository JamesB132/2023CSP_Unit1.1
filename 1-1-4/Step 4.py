#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

start_loop = "y"
painter.color("blue")

# Add a loop with a zero-iteration condition
while (start_loop == "n"):
    painter.forward(100)
# Add an infinite loop
while (start_loop == "y"):
    painter.forward(100)
    painter.right(90)
    painter.forward(100)
    painter.right(90)
    painter.forward(100)
    painter.right(90)
    painter.forward(100)
    painter.right(100)

wn = trtl.Screen()
wn.mainloop()