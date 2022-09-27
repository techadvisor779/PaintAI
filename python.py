import turtle
from screen import box

#set up the pollock drawing pen
pollock=turtle.Turtle()
pollock.hideturtle()
turn_speed=9
def set_pollock():
  pollock.showturtle()
  pollock.penup()

#import pen images
# image1="pollock1.png"
image2="pollock2.png"
image3="pollock3.png"
image_list = [image2,image3]
image_index=0

#list of the colors of the shape
colorsp = ['dark khaki','pale goldenrod','firebrick','beige','light gray']
color_indexp=0

#function to change background color
def change_colorp():
  global color_indexp
  color_indexp = color_indexp+1
  colorindexp = color_indexp % len(colorsp)
  global screen
  screen = turtle.Screen()
  screen.bgcolor(colorsp[colorindexp])

#function to turn shape left and right  
def turn_left():
  pollock.left(turn_speed)
def turn_right():
  pollock.right(turn_speed)

#function to change pen image
def image():
  screen = turtle.Screen()
  screen.addshape(image3)
  pollock.shape(image3)
#function to switch between pen shapes
def change_image():
  global screen
  screen = turtle.Screen()
  global image_index
  image_index = image_index +1
  image_index = image_index % len(image_list)
  screen.addshape(image_list[image_index])
  pollock.shape(image_list[image_index])

#function to draw in pollock mode
def draw_pollock(x,y):
  set_pollock()
  pollock.tracer(0)
  pollock.goto(x,y)
  pollock.stamp()
  pollock.tracer(1)

#function to reset pollock drawing template
def resetp():
  pollock.clear()


