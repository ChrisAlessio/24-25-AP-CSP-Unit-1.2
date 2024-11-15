#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
ground_height = -200
apple_letter_x_offset = -10
apple_letter_y_offset = -25

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
writer = trtl.Turtle()
'''pear = trtl.Turtle()'''
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  write_A()
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def drop_apple():
  writer.clear()
  apple.goto(apple.xcor(), ground_height)


def write_A():
  writer.penup()
  writer.hideturtle()
  writer.goto(apple.xcor() + apple_letter_x_offset, apple.ycor() + apple_letter_y_offset)
  writer.color("white")
  writer.write("A", font=("Arial", 24, "normal"))

#-----function calls-----
'''pear.hideturtle()'''
apple.penup()
draw_apple(apple)

wn.onkeypress(drop_apple, "a")

wn.listen()
'''draw_pear(pear)
pear.forward(100)'''

wn.mainloop()