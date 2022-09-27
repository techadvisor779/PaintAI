import turtle
from screen import *
from constants import *
from mondrian import *
from pollock import *

#function to set properties of turtle
def set_turtle():
  turtle.color("green")
  turtle.hideturtle()

#function to set up screen
def set_screen():
  set_turtle()
  mondrian.hideturtle()
  pollock.hideturtle()
  prompt_screen(myscreen)
  myscreen.onclick(clicky)

#function to quit to main prompt screen
def quit():
  myscreen.reset()
  set_screen()

#function to click on screen to go into drawing mode
def clicky(x, y):
  turtle.penup()
  turtle.goto(x,y)
  global dist1
  dist1 = turtle.distance(center1x,center1y)
  global dist2
  dist2 = turtle.distance(center2x,center2y)
  if dist1<10:     #mondrian drawing mode
    clear_screen_helper()
    write(-190,-190,"s=change shape, c=change color, u=size up, d=size down, r=reset, q=quit",8)
    myscreen.onclick(draw_mondrian)   
    # code to change shape, color and size
    myscreen.onkey(change_shape,"s")
    myscreen.onkey(change_color,"c")
    myscreen.onkey(change_sizeup,"u")
    myscreen.onkey(change_sizedown,"d")
    myscreen.onkey(reset, "r")
    myscreen.onkey(quit, 'q')
  elif dist2<10:   #pollock drawing mode
    clear_screen_helper()
    write(-190,-190,"s=change shape, c=change background color, left/right=turn shape left/right, r=reset, q=quit",7)
    image()
    myscreen.onclick(draw_pollock)
    myscreen.onkey(change_colorp,"c")
    myscreen.onkey(change_image, "s")
    myscreen.onkey(turn_left, 'left')
    myscreen.onkey(turn_right, 'right')
    myscreen.onkey(resetp, "r")
    myscreen.onkey(quit, 'q')


#go to prompt screen and drawing mode
myscreen=turtle.Screen()
set_screen()


myscreen.listen()
