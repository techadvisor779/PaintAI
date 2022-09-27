import turtle
still_going=True
screen_helper=turtle.Turtle()
screen_helper.hideturtle()

#function to set properties of helper turtle
def set_screen_helper():
  screen_helper.color("red")
  screen_helper.speed(9)
  screen_helper.hideturtle()

#function to draw sides of box
def box(side,angle):
  screen_helper.pendown()
  screen_helper.forward(side)
  screen_helper.right(angle)
  screen_helper.penup()

# function to go to a coordinate and write prompts
def write(x,y,w,f):
  screen_helper.penup()
  screen_helper.goto(x,y)
  screen_helper.write(w,font=("Arial",f, "normal"))

#function of prompt screen
def prompt_screen(screen):
  screen_helper.tracer(0)
  set_screen_helper()
  # function to draw check box
  def choice():
    for i in range(4):
      box(15,90)
  write(-150,150,"Choose your modern art drawing mode",15)
  
  # Go to position to draw box and 1st choice
  screen_helper.goto(-50,0)
  choice()
  write(-30,-15,"Pollock",15)
  
  # Go to position to draw box and 2nd choice
  screen_helper.goto(-50,0)
  screen_helper.left(90)
  screen_helper.forward(50)
  choice()
  write(-30,50,"Mondrian",15)
  screen_helper.tracer(1)

#function to clear prompt screen after choosing drawing mode
def clear_screen_helper():
  screen_helper.clear()