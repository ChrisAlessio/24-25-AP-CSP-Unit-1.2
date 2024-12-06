import turtle as trtl
import random as rand

#Initialize variable
wn = trtl.Screen()
maze_painter = trtl.Turtle()
wall_len = 35
path_width = 30

# Setup turtle
maze_painter.speed(0)
maze_painter.left(90)
maze_painter.pensize(5)

# Draw Maze
# Process:
# Draw a line
# Turn left
# Increment length
# Repeat
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

for wall in range(21):
    gap = rand.randint(0, wall_len - path_width)
    barrier = 0
    maze_painter.forward(gap)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if(wall > 5):
        barrier = rand.randint(0, wall_len - gap - path_width)
        maze_painter.forward(barrier)
        draw_barrier()
    maze_painter.forward(wall_len - gap - path_width - barrier)
    maze_painter.left(90)
    wall_len  += 15








wn.listen()
wn.mainloop()
