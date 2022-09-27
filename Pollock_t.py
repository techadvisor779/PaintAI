# paint application using Tkinter .....
from itertools import count
import time
import urllib
from random import randint
from tkinter import *
from tkinter.ttk import Scale
from tkinter import  colorchooser,messagebox
from tkinter.filedialog import asksaveasfilename
import PIL.ImageGrab as ImageGrab # pip install pillow
color= 'white'
i = 1

global my_count
my_count = 0

current_pallet0 = ['#FFFFFF',			#white  0
    '#70704A',			                #tan   1
    '#F5C677',							#orange 2
    '#F2E5C2',				            #tan    3
    '#D75A22',							#orange 4
    '#736A61',							#brown  5     
    '#EB3D00',							#red    6
    '#000000']		                    #black  7

current_pallet1 = ['#FFFFFF',			#white  0
    '828A8D',							#grey   1
    '9D3900',			                #red/brn2
    'D4AD44',			                #tan    3
    'D966F1',	 		                #orange 4
    '736A61',			                #brown  5     
    '0A14C8',			                #blue   6
    '#000000']							#black  7

current_pallet2 = ['#FFFFFF',			#white  0
    '993C30',			                #rust   1
    'E84C36',			                #red    2
    'D75A22',			                #orange 3
    'BFA461',			                #tan    4    
    '736A61',			                #brown  5     
    '5AE6D2',			                #teal   6
    '#000000']				            #black  7

COLORS = []
COLORS = current_pallet0
WIDTH=1200
WIDTH=750

class Paint():
	def __init__(self,root):
		self.root = root
		self.root.title("Paint")
		self.root.geometry("1350x750")
		self.root.configure(background="white")
		self.root.resizable(0,0)

		self.pen_color = "#000000"
		self.paint_size = 10
		self.pen_size = 0
		self.last_x =0
		self.last_y = 0

		self.color_frame = LabelFrame(self.root,text ="Color",font =('arial',15,'bold'),bd=5,relief=RIDGE,bg='white')
		self.color_frame.place(x=0,y=0,width=100,height=740)

		Colors = ['#ff0000','#ff4dd2','#ffff33','#000000','#0066ff','#660033','#4dff4d','#b300b3','#00ffff','#808080','#99ffcc','#336600','#ff9966','#ff99ff','#00cc99',]
		i =j= 0
		for color in Colors:
			Button(self.color_frame,bg=color,command=lambda col = color:self.select_color(col),width=3,bd=2,relief=RIDGE).grid(row=i,column=j)
			i+=1
			if i== 6:
				i=0
				j=1

		self.erase_button = Button(self.root,text="Eraser",bd=4,relief=RIDGE,width=8,command=self.eraser,bg="white")
		self.erase_button.place(x=0,y=187)

		self.clear_sreen_button =Button(self.root,text="Clear",bd=4,relief=RIDGE,width=8,command=lambda : self.canvas.delete("all"),bg="white")
		self.clear_sreen_button.place(x=0,y=217)

		self.save_button =Button(self.root,text="Save",bd=4,relief=RIDGE,width=8,command=self.save_paint,bg="white")
		self.save_button.place(x=0,y=247)

		self.canvas_color_button =Button(self.root,text="Canvas",bd=4,relief=RIDGE,width=8,command=self.canvas_color,bg="white")
		self.canvas_color_button.place(x=0,y=277)
		self.dabble_color = '#ff0000'

		self.pen_size_scale_frame = LabelFrame(self.root,text="Size",bd=5,relief=RIDGE,bg="white",font =('arial',15,'bold'))
		self.pen_size_scale_frame.place(x=0,y=310,height=200,width=70)

		self.pen_size = Scale(self.pen_size_scale_frame,orient='vertical', from_=50, to=0, command=None,length=170)
		self.pen_size.set(10)
		self.pen_size.grid(row=0,column=1,padx=15)

		self.canvas = Canvas(self.root,bg='white',bd=5,relief='groove',height=720, width=1200)
		self.canvas.place(x=105,y=10)

		# Blind mouse dragging event to canvas
		self.canvas.bind("<B1-Motion>",self.paint)

		self.seconds = time.time()

	def create_circle(self, x, y, r, canvasName): #center coordinates, radius
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		return canvasName.create_oval(x0, y0, x1, y1, fill = self.dabble_color)

	def paint(self,event):
		print(event)
		global pen_color
		self.seconds += 1
		global my_count

		my_count += 1
		if my_count>400:
			my_count = 0

		my_size = self.pen_size.get()
		self.pen_size.set(my_size-1)
		if event.x-self.last_x>10 or event.y-self.last_y>10:
			x1,y1 = ( event.x-4), ( event.y-4)
			x2,y2 = ( event.x+4), ( event.y+4)
		else:
			x1,y1 = ( event.x), ( event.y)
			x2,y2 = (self.last_x), ( self.last_y)
		if(i):
			self.canvas.config(cursor = 'plus')
		self.canvas.create_oval( x1, y1, x2, y2, fill = self.pen_color, outline=self.pen_color, width=self.pen_size.get())
		self.canvas.create_oval(1150-x1+100,750-y1, 1150-x2+100,750-y2,fill = self.pen_color,outline=self.pen_color,width=self.pen_size.get())
		if my_count % 25:
			self.dabble_color=COLORS[randint(1,7)]
			self.create_circle( x1+randint(-80,80), y1+randint(-80,80), randint(1,12), self.canvas)
			self.create_circle( 1150-x1+randint(-80,80), 750-y1+randint(-80,80), randint(1,12), self.canvas)
		self.last_x = x1
		self.last_y = y1

	def select_color(self,col):
		global i
		i = 1
		self.pen_color = col

	def eraser(self):
		global color
		global i
		self.pen_color = color
		self.canvas.config(cursor = 'dot')
		i = 0

	def canvas_color(self):
		global color
		color = colorchooser.askcolor()
		color = color[1]
		self.canvas.config(background=color)

	def save_paint(self):
		try:
			self.canvas.update()
			filename = asksaveasfilename(defaultextension='.jpg')
			print(filename)
			x = self.root.winfo_rootx() + self.canvas.winfo_x()
			#print(x)
			y = self.root.winfo_rooty() + self.canvas.winfo_y()
			#print(y)
			x1 = x + self.canvas.winfo_width()
			#print(x1)
			y1 = y + self.canvas.winfo_height()
			#print(y1)
			ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
			messagebox.showinfo('paint says ','image is saved as '+str(filename))

		except:
			pass


if __name__ == "__main__":
	root = Tk()
	Paint(root)
	root.mainloop()