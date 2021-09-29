from tkinter import*

current_x,current_y = 0,0
color = 'black'
def locate_xy(event):
    global current_x,current_y
    current_x,current_y = event.x,event.y
    print(current_x,current_y)

def addline(event):
    global current_x,current_y
    print(current_x,current_y,event.x,event.y)
    Canvas.create_line((current_x,current_y,event.x,event.y),fill = color)    
    current_x,current_y = event.x,event.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    Canvas.delete('all')
    display_pallete()


 window = Tk() #by this we can make gui
window.title('paint apk')
 window.state('zoomed')#by this our gui sed zoomed
window.config(bg='red')

 window.rowconfigure(0, weight=1)
window.columnconfigure(0,weight=1)

menubar = Menu(window)
window.config(menu = menubar)
submenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label = 'file', menu=submenu)
submenu.add_command(label='newcanavas',command=new_canvas)

Canvas=Canvas(window,background='white')
Canvas.grid(row=0,column=0,sticky='nsew')
Canvas.bind('<Button-1>',locate_xy)
Canvas.bind('<B1-Motion>',addline) #it can create line
#making colour box to select colour
def display_pallete():
    id=Canvas.create_rectangle((10,10,30,30),fill='black')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('black'))

    id=Canvas.create_rectangle((10,40,30,60),fill='gray')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('gray'))

    id=Canvas.create_rectangle((10,70,30,90),fill='brown4')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('brown4'))

    id=Canvas.create_rectangle((10,100,30,120),fill='red')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('red'))

   id=Canvas.create_rectangle((10,130,30,150),fill='orange')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('orange'))

    id=Canvas.create_rectangle((10,160,30,180),fill='yellow')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('yellow'))

    id=Canvas.create_rectangle((10,190,30,210),fill='green')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('green'))

    id=Canvas.create_rectangle((10,220,30,240),fill='blue')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('blue'))

    id=Canvas.create_rectangle((10,250,30,270),fill='purple')
    Canvas.tag_bind(id,'<Button-1>', lambda x:show_color('purple'))

 display_pallete()
 Canvas.create_line(20,20,60,20) # here in the manner (x,y,x,y) so here two point one is(20,20)and another is (60,20)
 window.mainloop() #by this we can check the work properly
