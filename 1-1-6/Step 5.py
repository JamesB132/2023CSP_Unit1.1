import turtle as trtl
spider = trtl.Turtle()

#Create a spider body

spider.pensize(40)
spider.circle(20)

#Configure legs

legs = 6
legs_length = 30
spacing = 380 / legs
spider.pensize(5)
n = 0

#Draw legs

while (n < legs):
  spider.goto(0, 0)
  spider.setheading(spacing * n)
  spider.forward(legs_length)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()