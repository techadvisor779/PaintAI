import turtle
from screen import box
from screen import write

mondrian=turtle.Turtle()
mondrian.hideturtle()
#set up the mondrian drawing pen
def set_mondrian():
  mondrian.pencolor("black")
  mondrian.hideturtle()
  mondrian.pensize(6)
  mondrian.speed(9)
  mondrian.penup()

#draw the first 2 sides of the shape
def side_rectangle(side1,side2):
  mondrian.pendown()
  mondrian.forward(side1)
  mondrian.right(90)
  mondrian.forward(side2)
  mondrian.right(90)
  mondrian.penup()

#the length of first side of the shape
shape1 = [120,170,70]  
#the length of second side of the shape
shape2 = [120,70,170] 

#function to increase/decrease shape
def change_sizeup():
  for i in range(len(shape1)):
    shape1[i] += 5
    shape2[i] += 5
def change_sizedown():
  for i in range(len(shape1)):
    shape1[i] -= 5
    shape2[i] -= 5

#list of the colors of the shape
colors = ['blue','yellow','red','black','white']

#create index and function to cycle through shape
shape_index=0
def change_shape():
  global shape_index
  shape_index = shape_index+1

#create index and function to cycle through colors
color_index=0
def change_color():
  global color_index
  color_index = color_index+1

#function to draw squares or rectangles:
def draw_mondrian(x,y):
  mondrian.tracer(0)
  set_mondrian()
  # write(-90,-90,"s=change shape, c=change color, u=size up, d=size down, r=reset, q=quit")
  mondrian.goto(x,y)
  colorindex = color_index % len(colors)
  mondrian.fillcolor(colors[colorindex])    #take the value from color index
  mondrian.fill(True)
  for i in range(2):   #draw the shape
    shapeindex = shape_index % len(shape1)  #shape1 and shape2 should always have the same number of items
    side_rectangle(shape1[shapeindex],shape2[shapeindex])   #take the values from the shape1 and shape2 lists to draw shape
  mondrian.fill(False)  
  mondrian.tracer(1)

#function to reset mondrian drawing template
def reset():
  mondrian.clear()
  
