from tkinter import *
from tkinter import Scale
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import PIL.ImageGrab as ImageGrab

class DrawingProgram():
    def __init__(self,root):
        self.root = root
        self.root.title("Drawing Program")
        self.root.geometry("800x520")
        self.root.configure(background='white')
        self.root.resizable(0,0)

        self.pen_color = "black"
        self.eraser_color="white"
        self.drawing_tool="pen"

        # Tracks whether left mouse is down
        self.left_but = "up"
        # Tracks x & y when the mouse is clicked and released
        self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt = None, None, None, None

        #Color Menu to make colors selectable for the User
        self.color_frame = LabelFrame(self.root,text='Colors',font=('arial',13),bd=5,relief=RIDGE,bg="white")
        self.color_frame.place(x=0,y=0,width=70,height=185)

        #Color section for easy access to the most common colors
        popularcolors = ['#000000','#FFFFFF','#FF0000','#00FF00','#0000FF','#FFFF00','#FF00FF','#808080','#00FBFF','#FF9B00','#FF0059','#6800FF']
        i=0
        j=0

        #Placing popular color buttons with using a for loop
        for color in popularcolors:
            Button(self.color_frame,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col = color:self.select_color(col)).grid(row=i,column=j)
            i = i+1
            if i == 6:
                i=0
                j=1

        #More Colors options menu
        menu = Menu(self.root)
        self.root.config(menu=menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='More Colors', menu=colormenu)
        colormenu.add_command(label='Brush Colors', command=self.more_color)

        #Shapes Menu
        shapes = Menu(menu)
        menu.add_cascade(label='Shapes', menu=shapes)
        shapes.add_command(label='Rectangle', command=self.drawing_tool_rectangle)
        shapes.add_command(label='Circle', command=self.drawing_tool_circle)
        shapes.add_command(label='Line',command=self.drawing_tool_line)

        #Select Pen
        menu.add_command(label="Pen",command=self.drawing_tool_pen)

        #Upload Image
        menu.add_command(label="Upload", command=self.upload_Img)

        #Buttons----------------------------
        self.save_button = Button(self.root,text='Save as jpg',bd=4,bg='white',command=self.save_canvas,width=8,relief=RIDGE)
        self.save_button.place(x=0,y=187)

        self.clear_button = Button(self.root,text='Clear',bd=4,bg='white',command=lambda : self.canvas.delete("all"),width=8,relief=RIDGE)
        self.clear_button.place(x=0,y=217)

        self.bgcolor_button = Button(self.root,text='Background',bd=4,bg='white',command=self.canvas_color,width=8,relief=RIDGE)
        self.bgcolor_button.place(x=0,y=247)

        self.eraser_button = Button(self.root,text='Eraser',bd=4,bg='white',command=self.eraser,width=8,relief=RIDGE)
        self.eraser_button.place(x=0,y=277)
        #------------------------------------

        #Pen Thickness
        self.pen_size_scale_frame=LabelFrame(self.root,text=" Pen ",bd=5,bg='white',font=('arial',15,'bold'),relief=RIDGE)
        self.pen_size_scale_frame.place(x=0,y=310,height=200,width=70)

        self.pen_size = Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=50,to=0,length=160)
        self.pen_size.set(1)
        self.pen_size.grid(row=0,column=1,padx=5)


        #Canvas
        self.canvas=Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=500, width=700)
        self.canvas.place(x=80,y=0)

        #Bind the Canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.left_but_down)
        self.canvas.bind("<ButtonRelease-1>", self.left_but_up)


    #Functions

    # ---------- CATCH MOUSE UP ----------

    def left_but_down(self, event=None):
        self.left_but = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

        # ---------- CATCH MOUSE UP ----------

    def left_but_up(self, event=None):
        self.left_but = "up"

        # Reset the line
        self.x_pos = None
        self.y_pos = None

        # Set x & y when mouse is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        # If mouse is released and line tool is selected
        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool =="pen":
            self.paint(event)

    #Drawing Tool Functions
    def drawing_tool_circle(self):
        self.drawing_tool = "oval"
    def drawing_tool_rectangle(self):
        self.drawing_tool = "rectangle"
    def drawing_tool_line(self):
        self.drawing_tool = "line"
    def drawing_tool_pen(self):
        self.drawing_tool = "pen"

    #DRAW RECTANGLE
    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                          fill=self.pen_color,
                                          outline=self.pen_color,
                                          width=self.pen_size.get())
    #DRAW Circle
    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt,
                                     fill=None,
                                     outline=self.pen_color,
                                     width=self.pen_size.get())

    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE,
                                     fill=self.pen_color,width=self.pen_size.get())

    #Painting the canvas
    def paint(self, event):
        if self.drawing_tool =="pen":
            x1, y1 = (event.x-2), (event.y-2)
            x2, y2 = (event.x+2), (event.y+2)
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color , width=self.pen_size.get())

    #Eraser Mod
    def eraser(self):
        self.drawing_tool ="pen"
        self.pen_color=self.eraser_color

    #Color Select Function
    def select_color(self,col):
        self.pen_color=col

    #More Colors option with colorchooser
    def more_color(self):
        self.pen_color=colorchooser.askcolor(color=self.pen_color)[1]

    #Background Color Function
    def canvas_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]

    #Save Function
    def save_canvas(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension='.jpeg',filetypes=[("JPG", ".jpeg")])
            x=self.root.winfo_rootx()+self.canvas.winfo_x()
            y=self.root.winfo_rooty()+self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            messagebox.showinfo('Drawing Program','Image is saved as '+str(filename))

        except:
            messagebox.showerror("Drawing Program","Unable to save image,\n some thing went wrong")

    def upload_Img(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                              filetype=[("jpeg files", ".jpg")])
        image = Image.open(filename)
        image = image.resize((800,520),Image.ANTIALIAS)
        self.canvas.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0,0,image=self.canvas.image, anchor='nw')

root = Tk()
p = DrawingProgram(root)
root.mainloop()