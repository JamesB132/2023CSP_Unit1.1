import turtle as trtl
spider = trtl.Turtle()

#Create a spider body

spider.pensize(40)
spider.circle(20)

#Configure legs

legs = 8
legs_length = 70
spacing = 360 / legs
spider.pensize(5)
n = 0

#Draw legs

while (n < legs):
  if (n < 4):
    spider.goto(0, 20)
    spider.setheading(spacing * n * .5)
    spider.forward(legs_length)
  if (n > 3):
    spider.goto(0, 20)
    spider.setheading(spacing * -n * .5)
    spider.forward(legs_length)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()