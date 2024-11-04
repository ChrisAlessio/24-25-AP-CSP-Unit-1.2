# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0

font_setup = ("Arial", 20, "normal")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white",]
sizes = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.speed(5)

score_writer = trtl.Turtle()

counter =  trtl.Turtle()

#-----game functions--------
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-350,350)

counter.penup()
counter.hideturtle()
counter.goto(350,350)

def adding_colors():
    spot.color(rand.choice(colors))
    spot.stamp()
    spot.color("pink")
def changing_size():
    spot.shapesize(rand.choice(sizes))
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score,font=font_setup)
def change_position():
    spot.penup()
    trtl.hideturtle()
    new_xpos = rand.randint(-250,250)
    new_ypos = rand.randint(-250,250)
    spot.goto(new_xpos,new_ypos)
def spot_clicked(x,y):
    if timer_up == False:
        changing_size()
        adding_colors()
        update_score()
        change_position()
    else:
        timer_up == True
        spot.hideturtle()
#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("skyblue")
wn.ontimer(countdown, counter_interval)
wn.mainloop()