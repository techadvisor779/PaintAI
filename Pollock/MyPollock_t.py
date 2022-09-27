
from tkinter import *
from tkinter.ttk import Button, Label
import math
from random import randint
import HtmlFrame
   
WIDTH = 1200
HEIGHT = 750
BACK = False
NEXT = False

current_pallet0 = [(255,255,255),       #white  0
    (112, 112, 74, 150),                #grey   1
    (245, 198, 119, 150),               #orange 2
    (242, 229, 194, 150),               #tan    3
    (215, 90, 34, 150),                 #orange 4
    (115, 106, 97, 150),                #brown  5     
    (235, 61, 0, 150),                  #red    6
    ( 0, 0, 0, 0)]                      #black  7

current_pallet1 = [(255,255,255, 0),    #white  0
    (130, 138, 141, 150),               #grey   1
    (157, 57, 0, 150),                  #red/brn2
    (212, 173, 68, 150),                #tan    3
    (217, 102, 241, 150),               #orange 4
    (115, 106, 97, 150),                #brown  5     
    (10, 20, 200, 150),                 #blue   6
    ( 0, 0, 0, 0)]                      #black  7

current_pallet2 = [(255,255,255, 0),    #white  0
    (153, 60, 48, 150),                 #rust   1
    (232, 76, 54, 150),                 #red    2
    (215, 90, 34, 150),                 #orange 3
    (191, 164, 97, 150),                #tan    4    
    (115, 106, 97, 150),                #brown  5     
    (90, 230, 210, 150),                #teal   6
    ( 0, 0, 0, 0)]                      #black  7

COLORS = []
COLORS = current_pallet0
brush_size = 10
color_active = COLORS[0]
color_passive = pygame.Color('grey')
x = 0
y = 0
z = 0
global px
global py
global this_image
px = 0
py = 0
imagecount = 0
again = False
active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
active6 = False
global user_text1
global user_text2
global user_text3 
global user_text4
global user_text5
global artist_name
 
sale_button = 2
arrow_fwd = PhotoImage(file="assets/forward.png")
arrow_back = PhotoImage(file="assets/back.png")
style_0_image = PhotoImage(file="assets/style_pallet00.png")
style_1_image = PhotoImage(file="assets/style_pallet11.png")
style_2_image = PhotoImage(file="assets/style_pallet22.png")
brush_img = PhotoImage(file="assets/brush_white.png")
brush_image2 = PhotoImage(file="assets/brush_black.png")
font = tkFont.Font('candara',18,weight="bold")
font2 = tkFont.Font('candara',48,weight="bold")
font4 = tkFont.Font('candara',24)
font3 = tkFont.Font('Comic Sans',20,weight="bold")

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()
bb = Button(root, text = 'Back!', image = arrow_back).pack(side = TOP)
bb.place(x=50, y=50)

def draw(x, y, px, py, z, color_index, brush_size, bg_color):        
    if z and x > (200 + brush_size):
        delta = math.sqrt(abs(x-px)+abs(y-py))
        while color_index == bg_color:
            color_index += 1
            if color_index > 7:
                color_index = 0
        if delta > 3 or brush_size > 2:
            ell = canvas.create_rectangle(x,y,abs(px-x)+brush_size,abs(py-y)+brush_size)
            
            canvas.create_oval( screen, COLORS[color_index], ell) 
            canvas.pack()

            ell = canvas.create_rectangle(WIDTH-x+200,HEIGHT-y,abs(px-x)+brush_size,abs(py-y)+brush_size)
            canvas.create_oval( screen, COLORS[abs(7-color_index)], ell) 
            canvas.pack()
        else:
            canvas.create_circle(screen, COLORS[color_index], (x,y), brush_size) 
            canvas.create_circle(screen, COLORS[7-color_index], (WIDTH-x+200,HEIGHT-y), brush_size)
            canvas.pack()
    return x, y

def drizzle(x, y, z, bg_color):
    if z and x > (200 + brush_size):
        rand_color = randint(0,7)
        rand_color2 = randint(0,7)
        while rand_color == bg_color:
            rand_color = randint(0,7)
        while rand_color2 == bg_color:
            rand_color2 = randint(0,7)
        rectx_adj = randint(-100,100)
        recty_adj = randint(-100,100) 
        rand_rad = randint(1,8)
        rand_rad2 = randint(1,8)
        x = x + rectx_adj
        y = y + recty_adj
        if x > 200:
            canvas.create_circle(screen, COLORS[rand_color], (x,y), rand_rad) 
        if WIDTH - x + 200 > 200:
            canvas.create_circle(screen, COLORS[rand_color2], (WIDTH - x + 200,HEIGHT - y), rand_rad2)  

if __name__ == '__main__':             
    clock = time.clock()
    color_index = 0
    pallet_choice = 0
    pallet_flag = 0
    push = 1
    count = 0
    reset = True
    reset_rect = ( 20, 605, 150, 30)
    back_rect = canvas.create_rectangle(50, 50, 130, 130)
    next_rect = canvas.create_rectangle( 20, 650, 150, 30)
    next2_rect = canvas.create_rectangle( 1130, 660, 80, 80)
    style0_rect = canvas.create_rectangle(58, 220, 80, 80)
    style1_rect = canvas.create_rectangle(48, 308, 104, 76)
    style2_rect = canvas.create_rectangle(48, 398, 104, 76)
    frame_rect = canvas.create_rectangle(0,0,200, HEIGHT) 
    init_p = True
    master_loop = True    

    while master_loop:
        root.mainloop()
        if again:
            this_image = PhotoImage(file="PollockImage0.png")
            screen.blit(this_image, (200,0))
        pygame.display.update() 
        while push:        
            clock.tick(100)
            x, y = pygame.mouse.get_pos()    
            if init_p:
                px, py = x, y
                init_p = False
            delta = math.sqrt((abs(x-px)*abs(x-px)+(abs(y-py)*abs(y-py))))
            count += delta + 1
            if count > 100: count =0
            screen.blit(style_0_image, (58,220))
            if pallet_flag == 0:
                canvas.create_rectangle(screen, COLORS[0], style0_rect, 3, 1)
                canvas.create_rectangle(screen, COLORS[0], style1_rect, 1, 1)
                canvas.create_rectangle(screen, COLORS[0], style2_rect, 1, 1)
        
            screen.blit(style_1_image, (50,310))
            if pallet_flag == 1:
                canvas.create_rectangle(screen, COLORS[0], style0_rect, 1, 1)
                canvas.create_rectangle(screen, COLORS[0], style1_rect, 3, 1)
                canvas.create_rectangle(screen, COLORS[0], style2_rect, 1, 1)
        
            screen.blit(style_2_image, (50,400))
            if pallet_flag == 2:
                canvas.create_rectangle(screen, COLORS[0], style0_rect, 1, 1)
                canvas.create_rectangle(screen, COLORS[0], style1_rect, 1, 1)
                canvas.create_rectangle(screen, COLORS[0], style2_rect, 3, 1)
            pygame.display.update()
            canvas.create_rectangle(screen, COLORS[0], frame_rect, 3, 1)
            pygame.display.update()
            clr_text = font.render("Pallet", True, COLORS[0])
            screen.blit(clr_text, ( 70, 190))
            pygame.display.update()

            Reset_button = canvas.create_rectangle(screen, COLORS[0], reset_rect, 3, 5)
            clr_text = font.render("Reset", True, COLORS[0])
            screen.blit(clr_text, ( 70, 612))
            pygame.display.update()

            canvas.create_rectangle(screen, (47,86,223), next_rect)
            Next_button = canvas.create_rectangle(screen, (136,206,236), next_rect, 3, 7)
            next_text = font.render("Next", True, (0,0,0))
            screen.blit(next_text, ( 70, 658))
            pygame.display.update()

            if reset:
                bg_color = randint(0,7)
                bg = screen.fill(COLORS[bg_color])
                bg = pygame.transform.scale(screen, (WIDTH-200, HEIGHT)) 
                surface = pygame.display.set_mode((WIDTH,HEIGHT))
                screen.blit(bg, (200,0))
                screen.blit(arrow_back, (50,50))
                pygame.display.update()           
                reset = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()    
                if event.type == pygame.MOUSEBUTTONDOWN:                  
                    count += 1
                    if Reset_button.collidepoint(pygame.mouse.get_pos()):
                        init_p = True
                        reset = True
                    elif style0_rect.collidepoint(pygame.mouse.get_pos()):
                        COLORS = current_pallet0
                        pallet_flag = 0
                    elif style1_rect.collidepoint(pygame.mouse.get_pos()):
                        COLORS = current_pallet1
                        pallet_flag = 1
                    elif style2_rect.collidepoint(pygame.mouse.get_pos()):
                        COLORS = current_pallet2
                        pallet_flag = 2
                    elif next_rect.collidepoint(pygame.mouse.get_pos()):
                        push = False
                    if x > 200: z = 1                  
                elif event.type == pygame.MOUSEBUTTONUP:
                    color_index += 1
                    if color_index > 7:
                        color_index = 0
                    z = 0 
                    brush_size = 14
            if z:
                if count % 4 == 0:
                    if brush_size > 0:
                        brush_size -= .6
            if brush_size > 0:
                px, py = draw(x, y, px, py, z, color_index, brush_size, bg_color)  
                if count % 2 == 0 and z:
                    drizzle(x, y, z, bg_color)
            pygame.display.flip()
        
        input_qty1 = canvas.create_rectangle(383, 270, 35, 25)
        input_qty2 = canvas.create_rectangle(383, 418, 35, 25)
        input_qty3 = canvas.create_rectangle(383, 566, 35, 25)
        input_qty4 = canvas.create_rectangle(755, 268, 35, 25)
        input_qty5 = canvas.create_rectangle(1044, 530, 35, 25)
        artist_rect = canvas.create_rectangle(750, 655, 250, 35)
        
        sm_rect = canvas.create_rectangle((180, 200), (80, 100))        
        med_rect = canvas.create_rectangle((125, 340), (140, 100))
        lg_rect = canvas.create_rectangle((700, 100), (200, 240))
        xlg_rect = canvas.create_rectangle((700, 440), (360, 240))
        screen = canvas.(canvas, 200, 0, WIDTH-200, HEIGHT)
        this_image = image.save(screen, "PollockImage0.png".format(imagecount))
        imagecount += 1
        push2 = True

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        bg = screen.fill((212, 173, 68, 150))
        bg = pygame.transform.scale(screen, (WIDTH, HEIGHT)) 
        surface = pygame.display.set_mode((WIDTH,HEIGHT))
        environment_view.blit()
        screen.update()
        
        clr_text = font2.render("Pick a Canvas Size and Quantity", True, COLORS[7])
        screen.blit(clr_text, ( WIDTH/2 - 200, 30))

        screen.blit(arrow_back, (50,50))       
        screen.blit(arrow_fwd, (WIDTH-100,HEIGHT-100))
        canvas.create_circle(screen, COLORS[7], (310, 278), 10, 2)    
        canvas.create_circle(screen, COLORS[0], (310, 278), 8, 8)  
        canvas.create_circle(screen, COLORS[7], (310, 428), 10, 2) 
        canvas.create_circle(screen, COLORS[0], (310, 428), 8, 8) 
        canvas.create_circle(screen, COLORS[7], (310, 578), 10, 2) 
        canvas.create_circle(screen, COLORS[0], (310, 578), 8, 8) 
        canvas.create_circle(screen, COLORS[7], (680, 278), 10, 2) 
        canvas.create_circle(screen, COLORS[0], (680, 278), 8, 8) 
        canvas.create_circle(screen, COLORS[7], (970, 538), 10, 2) 
        canvas.create_circle(screen, COLORS[0], (970, 538), 8, 8) 
         
        image = pygame.transform.rotate(pygame.transform.scale( pygame.image.load("PollockImage0.png"), (80, 100)), 0)        
        screen.blit(image, (180,200))
        clr_text = font.render(" 8.5 x 11 in. Print", True, COLORS[7])        
        screen.blit(clr_text, (280,220))
        price0_text = font.render("$9.95", True, COLORS[7])        
        screen.blit(price0_text, (280,240))
        price1_text = font.render("Qty", True, COLORS[7])        
        screen.blit(price1_text, (334,270))
        pygame.display.update() 

        image = pygame.transform.rotate(pygame.transform.scale( pygame.image.load("PollockImage0.png"), (80, 100)), 0)        
        screen.blit(image, (550,200))
        text = font3.render(" Best Value", True, COLORS[7])        
        screen.blit(text, (676,190))
        text = font3.render(" Best Value", True, (235, 61, 0, 150))        
        screen.blit(text, (677,191))
        clr_text = font.render(" 8.5 x 11 in. Canvas", True, COLORS[7])        
        screen.blit(clr_text, (650,220))
        price0_text = font.render("$49.95", True, COLORS[7])        
        screen.blit(price0_text, (650,240))
        price1_text = font.render("Sale $39.95", True, COLORS[7])        
        screen.blit(price1_text, (724,240))
        price1_text = font.render("Qty", True, COLORS[7])        
        screen.blit(price1_text, (704,270))
        pygame.draw.line(screen, (194, 24, 7), (650,256), (710,247), 2) 
        pygame.display.update() 

        image = pygame.transform.rotate(pygame.transform.scale( pygame.image.load("PollockImage0.png"), (140, 100)), 0)        
        screen.blit(image, (125,340))
        clr_text = font.render(" 14 x 10 in. Canvas", True, COLORS[7])        
        screen.blit(clr_text, (280,370))
        price0_text = font.render("$69.95", True, COLORS[7])        
        screen.blit(price0_text, (280,390))
        price1_text = font.render("Sale $59.95", True, COLORS[7])        
        screen.blit(price1_text, (360,390))        
        price1_text = font.render("Qty", True, COLORS[7])        
        screen.blit(price1_text, (334,420))
        pygame.draw.line(screen, (194, 24, 7), (280,405),(338,395), 2) 
        pygame.display.update()  

        image = pygame.transform.rotate(pygame.transform.scale( pygame.image.load("PollockImage0.png"), (200, 160)), 0)        
        screen.blit(image, (70,490))
        pygame.display.update() 
        clr_text = font.render(" 20 x 16 in. Canvas", True, COLORS[7])        
        screen.blit(clr_text, (280,520))
        price0_text = font.render("$79.95", True, COLORS[7])        
        screen.blit(price0_text, (280,540))
        price1_text = font.render("Sale $69.95", True, COLORS[7])        
        screen.blit(price1_text, (360,540))
        price1_text = font.render("Qty", True, COLORS[7])        
        screen.blit(price1_text, (334,570))        
        pygame.draw.line(screen, (194, 24, 7), (280,555),(338,545), 2) 
        pygame.display.update()  

        image = pygame.transform.rotate(pygame.transform.scale( pygame.image.load("PollockImage0.png"), (360, 240)), 0)        
        screen.blit(image, (550,350))
        pygame.display.update() 
        clr_text = font3.render(" Family Heirloom", True, COLORS[7])        
        screen.blit(clr_text, (940,395))
        clr_text = font3.render("Edition", True, COLORS[7])        
        screen.blit(clr_text, (970,425))
        clr_text = font3.render(" Family Heirloom", True, (235, 61, 0, 150))        
        screen.blit(clr_text, (941,396))
        clr_text = font3.render("Edition", True, (235, 61, 0, 150))        
        screen.blit(clr_text, (971,426))        
        clr_text = font.render(" 36 x 24 in. Canvas", True, COLORS[7])        
        screen.blit(clr_text, (930,480))
        price0_text = font.render("  Real Value at $79.95", True, COLORS[7])        
        screen.blit(price0_text, (930,502))     
        price1_text = font.render("Qty", True, COLORS[7])        
        screen.blit(price1_text, (1000,530))
        pygame.display.update()   
        
        canvas.create_rectangle(screen, color_passive, input_qty1)
        canvas.create_rectangle(screen, COLORS[7], input_qty1, 1, 1)
        canvas.create_rectangle(screen, color_passive, input_qty2)
        canvas.create_rectangle(screen, COLORS[7], input_qty2, 1, 1)
        canvas.create_rectangle(screen, color_passive, input_qty3)
        canvas.create_rectangle(screen, COLORS[7], input_qty3, 1, 1)
        canvas.create_rectangle(screen, color_passive, input_qty4)
        canvas.create_rectangle(screen, COLORS[7], input_qty4, 1, 1)
        canvas.create_rectangle(screen, color_passive, input_qty5)
        canvas.create_rectangle(screen, COLORS[7], input_qty5, 1, 1)   
        canvas.create_rectangle(screen, color_passive, artist_rect)
        canvas.create_rectangle(screen, COLORS[7], artist_rect, 1, 1)   
        pygame.display.update()  

        sm_rect = canvas.create_rectangle((180, 200), (80, 100))        
        med_rect = canvas.create_rectangle((125, 340), (140, 100))
        lg_rect = canvas.create_rectangle((700, 470), (200, 240))
        xlg_rect = canvas.create_rectangle((700, 440), (360, 240))
        button_rect1 = canvas.create_rectangle(300, 270, 80, 80)
        button_rect2 = canvas.create_rectangle(300, 419, 80, 80)
        button_rect3 = canvas.create_rectangle(300, 569, 80, 80)
        button_rect4 = canvas.create_rectangle(670, 268, 80, 80)
        button_rect5 = canvas.create_rectangle(960, 527, 80, 80)    
        user_text1 = ''
        user_text2 = ''
        user_text3 = ''
        user_text4 = ''
        user_text5 = ''
        artist_name = ''
        color = color_passive

        while push2:
            clock.tick(60)            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    print(pygame.mouse.get_pos())
                    if back_rect.collidepoint(pygame.mouse.get_pos()):
                        push = True
                        push2 = False
                        again = True

                    if button_rect1.collidepoint(pygame.mouse.get_pos()):                            
                        if screen.get_at((310, 278)) == COLORS[0]:  
                            active1 = True
                            active2 = False
                            active3 = False
                            active4 = False
                            active5 = False
                            active6 = False
                            color = color_active
                            canvas.create_circle(screen, COLORS[7], (310, 278), 10, 10)                              
                        else:
                            active1 = False
                            color = color_passive
                            canvas.create_circle(screen, COLORS[7], (310, 278), 10, 2)  
                            canvas.create_circle(screen, COLORS[0], (310, 278), 8, 8)                              
                            user_text1 = '' 
                        canvas.create_rectangle(screen, color, input_qty1)
                        canvas.create_rectangle(screen, COLORS[7], input_qty1, 1, 1)
                        pygame.display.update()

                    if input_qty1.collidepoint(pygame.mouse.get_pos()):
                        active1 = True
                        color = color_active
                        canvas.create_circle(screen, COLORS[7], (310, 278), 10, 10) 
                        canvas.create_rectangle(screen, color, input_qty1)
                        canvas.create_rectangle(screen, COLORS[7], input_qty1, 1, 1)
                        pygame.display.update()
                        
                    if button_rect2.collidepoint(pygame.mouse.get_pos()):
                        active1 = False
                        active2 = True
                        active3 = False
                        active4 = False
                        active5 = False
                        active6 = False
                        if screen.get_at((310, 430)) == COLORS[0]:
                            canvas.create_circle(screen, COLORS[7], (310, 428), 10, 10)
                            color = color_active
                        else:
                            active2 = False
                            color = color_passive
                            canvas.create_circle(screen, COLORS[7], (310, 428), 10, 2)  
                            canvas.create_circle(screen, COLORS[0], (310, 428), 8, 8)                            
                            user_text2 = ''
                        canvas.create_rectangle(screen, color, input_qty2)
                        canvas.create_rectangle(screen, COLORS[7], input_qty2, 1, 1)

                    if input_qty2.collidepoint(pygame.mouse.get_pos()):
                        active2 = True
                        color = color_active
                        canvas.create_circle(screen, COLORS[7], (310, 428), 10, 10) 
                        canvas.create_rectangle(screen, color, input_qty2)
                        canvas.create_rectangle(screen, COLORS[7], input_qty2, 1, 1)
                        pygame.display.update()

                    if button_rect3.collidepoint(pygame.mouse.get_pos()):
                        active1 = False
                        active2 = False
                        active3 = True
                        active4 = False
                        active5 = False
                        active6 = False
                        if screen.get_at((310, 578)) == COLORS[0]:
                            canvas.create_circle(screen, COLORS[7], (310, 578), 10, 10)
                            color = color_active
                        else:
                            active3 = False
                            color = color_passive
                            canvas.create_circle(screen, COLORS[7], (310, 578), 10, 2)  
                            canvas.create_circle(screen, COLORS[0], (310, 578), 8, 8)
                        canvas.create_rectangle(screen, color_passive, input_qty3)
                        canvas.create_rectangle(screen, COLORS[7], input_qty3, 1, 1)
                        user_text3 = ''

                    if input_qty3.collidepoint(pygame.mouse.get_pos()):
                        active3 = True
                        color = color_active
                        canvas.create_circle(screen, COLORS[7], (310, 578), 10, 10) 
                        canvas.create_rectangle(screen, color, input_qty3)
                        canvas.create_rectangle(screen, COLORS[7], input_qty3, 1, 1)
                        pygame.display.update()

                    if button_rect4.collidepoint(pygame.mouse.get_pos()):
                        active1 = False
                        active2 = False
                        active3 = False
                        active4 = True
                        active5 = False
                        active6 = False
                        if screen.get_at((678, 278)) == COLORS[0]:
                            canvas.create_circle(screen, COLORS[7], (680, 278), 10, 10)                            
                            canvas.create_rectangle(screen, COLORS[7], input_qty4, 1, 1)
                            color = color_active
                        else:
                            canvas.create_circle(screen, COLORS[7], (680, 278), 10, 2)  
                            canvas.create_circle(screen, COLORS[0], (680, 278), 8, 8)
                            color = color_passive
                        canvas.create_rectangle(screen, color, input_qty4)
                        canvas.create_rectangle(screen, COLORS[7], input_qty4, 1, 1)
                        user_text4 = ''

                    if input_qty4.collidepoint(pygame.mouse.get_pos()):
                        active4 = True
                        color = color_active
                        canvas.create_circle(screen, COLORS[7], (680, 278), 10, 10) 
                        canvas.create_rectangle(screen, color, input_qty4)
                        canvas.create_rectangle(screen, COLORS[7], input_qty4, 1, 1)
                        pygame.display.update()

                    if button_rect5.collidepoint(pygame.mouse.get_pos()):
                        active1 = False
                        active2 = False
                        active3 = False
                        active4 = False
                        active5 = True
                        active6 = False
                        if screen.get_at((970, 538)) == COLORS[0]:
                            canvas.create_circle(screen, COLORS[7], (970, 538), 10, 10)
                            color = color_active
                        else:
                            canvas.create_circle(screen, COLORS[7], (970, 538), 10, 2)  
                            canvas.create_circle(screen, COLORS[0], (970, 538), 8, 8) 
                            color = color_passive
                        canvas.create_rectangle(screen, color, input_qty5)
                        canvas.create_rectangle(screen, COLORS[7], input_qty5, 1, 1)
                        user_text5 = ''

                    if input_qty5.collidepoint(pygame.mouse.get_pos()):
                        active5 = True
                        color = color_active
                        canvas.create_circle(screen, COLORS[7], (970, 538), 10, 10) 
                        canvas.create_rectangle(screen, color, input_qty5)
                        canvas.create_rectangle(screen, COLORS[7], input_qty5, 1, 1)
                        pygame.display.update()

                    if artist_rect.collidepoint(pygame.mouse.get_pos()):
                        active6 = True
                        color = color_active
                        canvas.create_rectangle(screen, color, artist_rect)
                        canvas.create_rectangle(screen, COLORS[7], artist_rect, 1, 1)
                        pygame.display.update()

                    if next2_rect.collidepoint(pygame.mouse.get_pos()):
                        push2 = False

                str_text = font4.render("Type your name to sign the painting", True, (194, 24, 7))        
                screen.blit(str_text, (305,660))
                str2_text = font4.render("Type your name to sign the painting", True, COLORS[7])        
                screen.blit(str_text, (306,661))
                
                if event.type == pygame.KEYDOWN:   
                    if active1:  
                        color = color_active
                        if event.key == 8:
                            if len(user_text1) > 0:
                                user_text1 = user_text1[:-1]
                        elif event.unicode.isdigit():
                            user_text1 += event.unicode
                        text_surface1 = font.render(user_text1, True, (0,0,0))
                        screen.blit(text_surface1, (input_qty1.x+5, input_qty1.y+2))
                            
                    if active2:
                        if event.key == pygame.K_BACKSPACE:
                            user_text2 = user_text2[:-1]                            
                            pygame.display.update()
                        elif event.unicode.isdigit():
                            user_text2 += event.unicode  
                    if active3:
                        if event.key == pygame.K_BACKSPACE:
                            user_text3 = user_text3[:-1]
                            pygame.display.update()
                        elif event.unicode.isdigit():
                            user_text3 += event.unicode
                    if active4:
                        if event.key == pygame.K_BACKSPACE:
                            user_text4 = user_text4[:-1]
                            pygame.display.update()
                        elif event.unicode.isdigit():
                            user_text4 += event.unicode
                    if active5:
                        if event.key == pygame.K_BACKSPACE:
                            user_text5 = user_text5[:-1]
                            pygame.display.update()
                        elif event.unicode.isdigit():
                            user_text5 += event.unicode   
                    if active6:
                        if event.key == pygame.K_BACKSPACE:
                            artist_name = artist_name[:-1]
                            pygame.display.update()
                        else:
                            artist_name += event.unicode                     
                            
            if active1:
                canvas.create_rectangle(screen, color, input_qty1)   
                canvas.create_rectangle(screen, COLORS[7], input_qty1, 1, 1)
            if active2:
                canvas.create_rectangle(screen, color, input_qty2)   
                canvas.create_rectangle(screen, COLORS[7], input_qty2, 1, 1)
            if active3:
                canvas.create_rectangle(screen, color, input_qty3)   
                canvas.create_rectangle(screen, COLORS[7], input_qty3, 1, 1)
            if active4:
                canvas.create_rectangle(screen, color, input_qty4)   
                canvas.create_rectangle(screen, COLORS[7], input_qty4, 1, 1)
            if active5:
                canvas.create_rectangle(screen, color, input_qty5)   
                canvas.create_rectangle(screen, COLORS[7], input_qty5, 1, 1)
            if active6:
                canvas.create_rectangle(screen, color, artist_rect)   
                canvas.create_rectangle(screen, COLORS[7], artist_rect, 1, 1)
            text_surface1 = font.render(user_text1, True, COLORS[7])
            screen.blit(text_surface1, (input_qty1.x+5, input_qty1.y+2))
            text_surface2 = font.render(user_text2, True, COLORS[7])
            screen.blit(text_surface2, (input_qty2.x+5, input_qty2.y+2))
            text_surface3 = font.render(user_text3, True, (0,0,0))
            screen.blit(text_surface3, (input_qty3.x+5, input_qty3.y+2))
            text_surface4 = font.render(user_text4, True, (0,0,0))
            screen.blit(text_surface4, (input_qty4.x+5, input_qty4.y+2))
            text_surface5 = font.render(user_text5, True, (0,0,0))
            screen.blit(text_surface5, (input_qty5.x+5, input_qty5.y+2))
            text_surface6 = font.render(artist_name, True, (0,0,0))
            screen.blit(text_surface6, (artist_rect.x+10, artist_rect.y+10))
            pygame.display.update()
        
        screen = pygame.display.set_mode((WIDTH-200, HEIGHT))
        bg = screen.fill((212, 173, 68, 150))
        bg = pygame.transform.scale(screen, (WIDTH-200, HEIGHT)) 
        screen.blit(bg, (0,0))
        push3 = True
        while push3:
            clock.tick(30) 
            image = PhotoImage(file="PollockImage0.png")      
            screen.blit(image, (0,0))
            text = font3.render( artist_name + "'22", True, COLORS[7])        
            screen.blit(text, (WIDTH-300,HEIGHT-80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    print(pygame.mouse.get_pos())
   
            pygame.display.update() 
