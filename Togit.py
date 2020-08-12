from tkinter import *
#===============master window property====================
window = Tk()
window.geometry('660x485')
window.resizable(width=False, height=False)
window.title('Togit') 
window.configure(bg='cadetblue') 
#===============master window property#closed#=============

window.iconbitmap('C:\\Users\\SUCCESS\\Desktop\\build-up\\inffo.ico')

#C:\Users\SUCCESS\Desktop\build-up
#========create main window frames=========================
def maxy(my_frame):
    my_frame.tkraise()

root = Frame(window)
root2 = Frame(window)
root.configure(bg='cadetblue')
#root2.configure(bg='cadetblue')

for frames in (root, root2):
    frames.place(x=0, y=0, width= 660, height=485)

#=========create main window frames #closed#==============


#==========window1 (root) content==========================
m1 = Frame(root, bg="cadetblue")
m1.place(x=0,y=0, width=660, height=80)

#label1 = Label(root, text='WELCOME', bg='powderblue',fg='black', font='family 8')
#label1.place(x=0, y=5, height=20, width=50)

label1 = Label(root, text='Complete your projects UI quickly with easy access to \n all-Fonts and Colors',
             bg='cadetblue', fg="black", font='times 16')
label1.place(x=105, y=70, height=50, width=450)

label1 = Label(m1, text='Togit Automation', bg='cadetblue', fg='black', font='times 25 bold')
label1.place(x=155, y=5, height=60, width=300)
#==============================================================

frrame = Frame(m1, bg='blue')
frrame2 = Frame(m1, bg='red')
frrame3 = Frame(m1, bg='orange')
frrame4 = Frame(m1, bg='green')
frrame5 = Frame(root, bg='black')
frrame6 = Frame(root, bg='orange')


frrame.place(x=480, y=15, height=50, width=50)
frrame2.place(x=485, y=20, height=40, width=40)
frrame3.place(x=490, y=25, height=30, width=30)
frrame4.place(x=495, y=30, height=20, width=20)
frrame5.place(x=500, y=35, height=10, width=10)




#=====================My Canvas================================
fm1 = Frame(root, bg='black')
fm1.place(x=60, y=140, height=280, width=540)
fm2 = Frame(fm1, bg='cadetblue')
fm2.place(x=5, y=5, height=270, width=530)

w = Canvas(fm2, bg='cadetblue')
w.place(x=118, y=37, height=200, width=300)

b = Button(w, text='Launch Program!', bg='orange', font='verdana 13 bold',
 command= lambda: maxy(root2))
b.place(x=66, y=76, height=60, width=170)

w.create_rectangle(50, 60, 250, 150, fill="#476042")
#w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 60, fill="#476042", width=3)
w.create_line(250, 150, 296, 0, fill="#476042", width=3)
w.create_line(180,150, 296, 0, fill="#476042", width=3)
w.create_line(0, 0,50, 150, fill="#476042", width=3)
#=====================My Canvas #closed#==============================
#==========window1 (root) content #closed#============================


#===================window2 (root2) property=========================
def maxy2(map_raise):
    map_raise.tkraise()

label1 = Label(root2,  text='Welcome User,',
               font='times 14')
label1.place(x=150, y=0, width=250, height=30)

label2 = Label(root2,  text='Togit', fg='blue4',
               font='times 14 bold')
label2.place(x=334, y=0, width=45, height=30)

label2 = Label(root2,  text='got your back!',
               font='times 14')
label2.place(x=380, y=0, width=125, height=30)


label1 = Label(root2,  text='''kindly click any of the button with the preferred COLOR you like,
the Name will be copied to clickboard and you
can paste it where ever u wanna use it.''',
               font='times 12 ')
label1.place(x=100, y=26, width=500, height=80)

#=============color program property=============================
frame1 = Frame().pack()

frame11 = Frame(root2)
frame2 = Frame(root2)
frame3 = Frame(root2)

frame11.configure(bg='gray')
frame2.configure(bg='slategray')
frame3.configure(bg='cadetblue')

#frame1.place(x=0, y=150, width=600, height=370)
#frame2.place(x=0, y=150, width=600, height=370)
#frame3.place(x=0, y=150, width=600, height=370)

for my_frames in (frame11, frame2, frame3):
    my_frames.place(x=0, y=150, width=660, height=385)


button1 = Button(root2, text='Primary Colors', fg= 'black', bg='gray',
 font='times 12', command= lambda: maxy2(frame11))
button1.place(x=50, y=110, width=150, height=40)

button2 = Button(root2, text='Secondary Colors', fg= 'black', bg='slategray',
 font='times 12', command= lambda: maxy2(frame2))
button2.place(x=255, y=110, width=150, height=40)

button3 = Button(root2, text='All Colors', fg= 'black', bg='cadetblue',
 font='times 12', command= lambda: maxy2(frame3))
button3.place(x=460, y=110, width=150, height=40)
#=============color program property #closed#===================

#=============create side menu bar widget==========================
3#=================About-page for color_frame=======================================
about_frame = Frame()
about_frame.place(x=0,y=0,width=660, height=485)

back_button_about = Button(about_frame, text='<Back',  command= lambda: maxy(root2))
back_button_about.place(x=3, y=460, width=40, height=20)

text_about= Label(about_frame, text='Togit is a GUI application that helps programmers access all supported colors and fonts',
                   font='times 12')
text_about.place(x=10, y=47, width=530, height=30)

tx = Label(about_frame, text='in python and other major languegues, also it helps you out with spelling and typing,',
           font='times 12')
tx.place(x=2, y=71, width=510, height=30)

tx = Label(about_frame, text='therefore it copies the colors or font name to clickboard once clicked, and all the pro-',
           font='times 12')  
tx.place(x=5, y=95, width=518, height=30)

tx = Label(about_frame, text='grammer or user needs to do is just paste the element where he needs to use it.',
           font='times 12')
tx.place(x=1, y=119, width=485, height=30)


text_about3 = Label(about_frame,  text='What is Togit?',font='times 16')
text_about3.place(x=5, y=2, width=129, height=30)

text_about2 = Label(about_frame,  text='Why Togit?', font='times 16')
text_about2.place(x=5, y=164, width=120, height=30)



tx = Label(about_frame, text='1. It helps you to make the right color choice when designing a UI of an app or website.',
           font='times 12')
tx.place(x=2, y=209, width=530, height=30)

tx = Label(about_frame, text='2. The click-and-copy feature helps save you time and energy.',
           font='times 12')
tx.place(x=5, y=233, width=375, height=30)

#====================Made with love===========================================

bwl_frame2 = Frame(about_frame)
bwl_frame2.place(x=440, y=410, width=213, height=70)
bwl_frame2.configure(background='white')

labi = Label(bwl_frame2, text="Made with", fg="gray", bg="white", font="times 9")
labi.place(x=0, y=10, width=60, height=15)

labi2 = Label(bwl_frame2, text="by GetbusyHub", fg="gray", bg="white", font="times 9")
labi2.place(x=114, y=10, width=80, height=15)

labi3 = Label(bwl_frame2, text="Founder:", fg="gray", bg="white", font="times 9 bold")
labi3.place(x=0, y=34, width=53, height=15)

labi3 = Label(bwl_frame2, text="Okonkwo Success E.", fg="gray", bg="white", font="times 9")
labi3.place(x=53, y=34, width=110, height=15)

labi4 = Label(bwl_frame2, text="Website :", fg="gray", bg="white", font="times 9 bold")
labi4.place(x=0, y=53, width=52, height=15)

labi4 = Label(bwl_frame2, text="www.getbusyhub.com", fg="gray", bg="white", font="times 9")
labi4.place(x=59, y=53, width=111, height=15)

loveimage2 = PhotoImage(file="C:\\Users\\SUCCESS\\Desktop\\New folder\\imagees.png")
love22 = Label(bwl_frame2, image=loveimage2)
love22.place(x=62, y=0, width=50, height=30)
#===============================About, closed==============================


# =============================close button================================
font_frame = Frame( bg='cadetblue')
font_frame.place(x=0, y=0, width=660, height=485)

def my_func():
        maxy(root)
        
closebutton = Button(root2, text='Home', fg= 'black', bg='orange',
 font='times 10 bold', command= my_func)
closebutton.place(x=0, y=0, width=50, height=20)

#=========================close button #closed#========================


def explore(ex_raise):
    ex_raise.tkraise()

explore_frame = Frame()
exp = Frame()

#explore_frame.config(bg='white')

for m in (explore_frame, exp):
    m.place(x=0, y=0, width=80, height=110)

#===============================
def my_func2():
    maxy(root2)

new_canvas = Canvas(explore_frame)
new_canvas.place(x=0, y=0, height=110, width=100)

closebutton = Button(new_canvas, text='About', fg= 'black',
 bg='powderblue',bd= 0, font='times 12 bold', command= lambda: maxy(about_frame))
closebutton.place(x=10, y=38, width=60, height=32)


#new_canvas.create_circle(50, 60, 150, 50, fill="#476042")
new_canvas.create_rectangle(10, 38, 70, 70, fill="cadetblue")
new_canvas.create_line(35,38, 20, 15, fill="black", width=3)
new_canvas.create_line(40, 38, 61, 10, fill="black", width=3)
new_canvas.create_line(35,70, 20, 95, fill="black", width=3)
new_canvas.create_line(40, 70, 59, 95, fill="black", width=3)

#=======================closed============================================
def ctr(cost):
    cost.tkraise()

def gold():
    ctr(root2)
    ctr(frame11)
def andy():
    ctr(root2)
    ctr(font_frame)
    
optionbutton = Button(root2, text='Explore',fg= 'black', bg='orange', 
 font='times 10 bold', command= lambda: explore(explore_frame))
optionbutton.place(x=0, y=26, width=50, height=20)

colorbutton = Button(explore_frame, text='Colors',
 font='times 10 bold', bg='powderblue', bd=1, command= gold)
colorbutton.place(x=15, y=2, width=50, height=15)

colorbutton1 = Button(explore_frame, text='Fonts',
                      font='times 10 bold', bg='powderblue', bd=1,
                      command= andy)
colorbutton1.place(x=15, y=93, width=50, height=15)



#=============create side menu bar widget #closed#=======================
#===================window2 (root2) property #closed#=========================



#================frame11 content============================
label = Label(frame11, text='Primar colors are colours that cannot be created',bg='gray', font='times 13')
label.place(x=4, y=3, width=340, height=29)

labelA = Label(frame11, text="through the mixing of other colours.",bg='gray',font='times 13')
labelA.place(x=340, y=3, width=260, height=29)

labelB = Label(frame11, text='They are colours in their own right.',bg='gray',font='times 13')
labelB.place(x=4, y=27, width=250, height=30)

labelC = Label(frame11, text='The three primary colours can be seen below:',bg='gray',font='times 13')
labelC.place(x=250, y=27, width=320, height=30)

def copy_button3BB():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('blue')  

def copy_button4BB():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("yellow")

def copy_button5BB():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("red")

lb1 = Button(frame11, bd=0, text = "Blue",
 font='times 14 bold', fg='black', bg='blue', command= copy_button3BB)
lb1.place(x=2, y=57, width=218, height=92)

lb2 = Button(frame11, bd=0, text = "Yellow", 
font='times 14 bold', fg='black', bg='yellow', command=copy_button4BB)
lb2.place(x=220, y=149, width=218, height=92)

lb3 = Button(frame11, bd=0, text = "Red",
 font='times 14 bold',  fg='black', bg='red',command=copy_button5BB)
lb3.place(x=438, y=241, width=218, height=92)


#===============frame2 content===================

label = Label(frame2, text='A secondary color is a color made by mixing',bg='slategray', font='times 13')
label.place(x=4, y=3, width=310, height=30) 

labelA = Label(frame2, text="of two primary colors in a given color space.",bg='slategray',font='times 13')
labelA.place(x=315, y=3, width=310, height=30)

labelC = Label(frame2, text='The three secondary colours can be seen below:',bg='slategray',font='times 13')
labelC.place(x=4, y=27, width=340, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('green')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("purple")

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("orange")

lb1 = Button(frame2, bd=0, text = "Green",
 font='times 14 bold', fg='black', bg='green', command= copy_button_maxy1)
lb1.place(x=2, y=57, width=218, height=92)

lb2 = Button(frame2, bd=0, text = "Purple", 
font='times 14 bold', fg='black', bg='purple', command=copy_button_maxy2)
lb2.place(x=220, y=149, width=218, height=92)

lb3 = Button(frame2, bd=0, text = "Orange",
 font='times 14 bold',  fg='black', bg='orange',command=copy_button_maxy3)
lb3.place(x=438, y=241, width=218, height=92)


#=================frame3 content==================
def new_frame(many):
    many.tkraise()

frame4 = Frame(root2)
frame5 = Frame(root2)
frame6 = Frame(root2)
frame7 = Frame(root2)
frame8 = Frame(root2)
frame9 = Frame(root2)
frame10 = Frame(root2)

frame4.configure(bg='cadetblue')
frame5.configure(bg='cadetblue')
frame6.configure(bg='cadetblue')
frame7.configure(bg='cadetblue')
frame8.configure(bg='cadetblue')
frame9.configure(bg='cadetblue')
frame10.configure(bg='cadetblue')

for my_frames in (frame4, frame5, frame6,frame7,frame8,frame9,frame10):
    my_frames.place(x=0, y=150, width=660, height=385)

label_color = Label(frame3, text="This collection consit of all the available",
font="times 13",bg='cadetblue').place(x=5, y=3, width=280, height=30)
label_color2 = Label(frame3, text="and recogniced colors in tkinter and python.",
font='times 13',bg='cadetblue').place(x=288, y=3, width=300, height=30)

control1 = Button(frame3, text= '>',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame4))
control1.place(x=625, y=3, width=30, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('blue')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("yellow")

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("red")

lb1 = Button(frame3, bd=0, text = "Blue",
 font='times 12 bold', fg='black', bg= 'Blue', command= copy_button_maxy1)
lb1.place(x=2, y=37, width=80, height=35)

lb2 = Button(frame3, bd=0, text = "Yellow", 
font='times 12 bold', fg='black', bg='yellow', command=copy_button_maxy2)
lb2.place(x=84, y=37, width=80, height=35)

lb3 = Button(frame3, bd=0, text = "Red",
 font='times 12 bold',  fg='black', bg='red',command=copy_button_maxy3)
lb3.place(x=166, y=37, width=80, height=35)

def copy_button_maxy4():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('green')  

def copy_button_maxy5():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("orange")

def copy_button_maxy6():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("purple")

lb1 = Button(frame3, bd=0, text = "Green",
 font='times 12 bold', fg='black', bg='green', command= copy_button_maxy4)
lb1.place(x=248, y=37, width=80, height=35)

lb2 = Button(frame3, bd=0, text = "Orange", 
font='times 12 bold', fg='black', bg='orange', command=copy_button_maxy5)
lb2.place(x=330, y=37, width=80, height=35)

lb3 = Button(frame3, bd=0, text = "Purple",
 font='times 12 bold',  fg='black', bg='purple',command=copy_button_maxy6)
lb3.place(x=412, y=37, width=80, height=35)


def copy_button_maxy7():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("snow")

def copy_button_maxy8():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('ghost white')

lb1 = Button(frame3, bd=0, text = 'Snow',
 font='times 12 bold', fg='black', bg='snow', command= copy_button_maxy7)
lb1.place(x=494, y=37, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Ghost\nWhite',font='times 12 bold',
             fg='black', bg='ghost white', command=copy_button_maxy8)
lb2.place(x=576, y=37, width=80, height=35)

#=====================row2_frame3=================================
def copy_button_maxy9():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('whitesmoke')  

def copy_button_maxy10():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('gainsboro')

def copy_button_maxy11():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('floralwhite')

lb1 = Button(frame3, bd=0, text = 'White\nSmoke',
 font='times 12 bold', fg='black', bg='whitesmoke', command= copy_button_maxy9)
lb1.place(x=2, y=74, width=80, height=35)

lb2 = Button(frame3, bd=0, text = "Gainsboro", 
font='times 12 bold', fg='black', bg='gainsboro', command=copy_button_maxy10)
lb2.place(x=84, y=74, width=80, height=35)

lb3 = Button(frame3, bd=0, text = "Floral\nWhite",
 font='times 12 bold',  fg='black', bg='floralwhite',command=copy_button_maxy11)
lb3.place(x=166, y=74, width=80, height=35)

def copy_button_maxy12():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('oldlace')  

def copy_button_maxy13():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("linen")

def copy_button_maxy14():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('antiquewhite')

lb1 = Button(frame3, bd=0, text = "old Lace",
 font='times 12 bold', fg='black', bg='oldlace', command= copy_button_maxy12)
lb1.place(x=248, y=74, width=80, height=35)

lb2 = Button(frame3, bd=0, text = "Linen", 
font='times 12 bold', fg='black', bg='linen', command=copy_button_maxy13)
lb2.place(x=330, y=74, width=80, height=35)

lb3 = Button(frame3, bd=0, text = "Antique\nWhite",
 font='times 12 bold',  fg='black', bg='antiquewhite',command=copy_button_maxy14)
lb3.place(x=412, y=74, width=80, height=35)


def copy_button_maxy15():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('papayawhip')

def copy_button_maxy16():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('ghost white')

lb1 = Button(frame3, bd=0, text = 'Papaya\nWhip',
 font='times 12 bold', fg='black', bg='papayawhip', command= copy_button_maxy15)
lb1.place(x=494, y=74, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Blanched\nAlmond',
             font='times 12 bold', fg='black', bg='blanchedalmond', command=copy_button_maxy16)
lb2.place(x=576, y=74, width=80, height=35)

#==================row3_frame3=====================================
def copy_button_maxy17():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'bisque')  

def copy_button_maxy18():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('peachpuff')

def copy_button_maxy19():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('navajowhite')

lb1 = Button(frame3, bd=0, text = 'Bisque',
 font='times 12 bold', fg='black', bg='bisque', command= copy_button_maxy17)
lb1.place(x=2, y=111, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Peach\nPuff', 
font='times 12 bold', fg='black', bg='peachpuff', command=copy_button_maxy18)
lb2.place(x=84, y=111, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Navajo\nWhite',
 font='times 12 bold',  fg='black', bg='navajowhite',command=copy_button_maxy19)
lb3.place(x=166, y=111, width=80, height=35)

def copy_button_maxy20():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lemonchiffon')  

def copy_button_maxy21():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mintcream')

def copy_button_maxy22():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('azure')

lb1 = Button(frame3, bd=0, text = 'Lemon\nChiffon',
 font='times 12 bold', fg='black', bg='lemonchiffon', command= copy_button_maxy20)
lb1.place(x=248, y=111, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Mint\nCream', 
font='times 12 bold', fg='black', bg='mintcream', command=copy_button_maxy21)
lb2.place(x=330, y=111, width=80, height=35)

lb3 = Button(frame3, bd=0, text = "Azure",
 font='times 12 bold',  fg='black', bg='azure',command=copy_button_maxy22)
lb3.place(x=412, y=111, width=80, height=35)


def copy_button_maxy23():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('aliceblue')

def copy_button_maxy24():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lavender')

lb1 = Button(frame3, bd=0, text = 'Alice\nBlue',
 font='times 12 bold', fg='black', bg='aliceblue', command= copy_button_maxy23)
lb1.place(x=494, y=111, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Lavender',
             font='times 12 bold', fg='black', bg='lavender', command=copy_button_maxy24)
lb2.place(x=576, y=111, width=80, height=35)


#=============================row4_frame3==========================
def copy_button_maxy25():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lavenderblush')  

def copy_button_maxy26():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mistyrose')

def copy_button_maxy27():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkslategray')

lb1 = Button(frame3, bd=0, text = 'Lavender\nBlush',
 font='times 12 bold', fg='black', bg='lavenderblush', command= copy_button_maxy25)
lb1.place(x=2, y=148, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Misty\nRose', 
font='times 12 bold', fg='black', bg='mistyrose', command=copy_button_maxy26)
lb2.place(x=84, y=148, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Dark Slate\nGray',
 font='times 12 bold',  fg='black', bg='darkslategray',command=copy_button_maxy27)
lb3.place(x=166, y=148, width=80, height=35)

def copy_button_maxy28():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('dimgray')  

def copy_button_maxy29():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('slategray')

def copy_button_maxy30():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightslategray')

lb1 = Button(frame3, bd=0, text = 'Dim Gray',
 font='times 12 bold', fg='black', bg='dimgray', command= copy_button_maxy28)
lb1.place(x=248, y=148, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Slate Gray', 
font='times 12 bold', fg='black', bg='slategray', command=copy_button_maxy29)
lb2.place(x=330, y=148, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Light Slate\nGray',
 font='times 12 bold',  fg='black', bg='lightslategray',command=copy_button_maxy30)
lb3.place(x=412, y=148, width=80, height=35)


def copy_button_maxy31():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('gray')

def copy_button_maxy32():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightgrey')

lb1 = Button(frame3, bd=0, text = 'Gray',
 font='times 12 bold', fg='black', bg='gray', command= copy_button_maxy31)
lb1.place(x=494, y=148, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Light Grey',font='times 12 bold',
             fg='black', bg='lightgrey', command=copy_button_maxy32)
lb2.place(x=576, y=148, width=80, height=35)


#=================row5_frame3=====================================
def copy_button_maxy33():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('midnightblue')  

def copy_button_maxy34():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('navy')

def copy_button_maxy35():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cornflowerblue')

lb1 = Button(frame3, bd=0, text = 'Midnight\nBlue',
 font='times 12 bold', fg='black', bg='midnightblue', command= copy_button_maxy33)
lb1.place(x=2, y=185, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Navy', 
font='times 12 bold', fg='black', bg='navy', command=copy_button_maxy34)
lb2.place(x=84, y=185, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Corn Flower\nBlue',
 font='times 12 bold',  fg='black', bg='cornflowerblue',command=copy_button_maxy35)
lb3.place(x=166, y=185, width=80, height=35)

def copy_button_maxy36():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkslateblue')  

def copy_button_maxy37():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('slateblue')

def copy_button_maxy38():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumslateblue')

lb1 = Button(frame3, bd=0, text = 'DarkSlate\nBlue',
 font='times 12 bold', fg='black', bg='darkslateblue', command= copy_button_maxy36)
lb1.place(x=248, y=185, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Slate Blue', 
font='times 12 bold', fg='black', bg='slategray', command=copy_button_maxy37)
lb2.place(x=330, y=185, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Medium\nSlate Blue',
 font='times 12 bold',  fg='black', bg='mediumslateblue',command=copy_button_maxy38)
lb3.place(x=412, y=185, width=80, height=35)


def copy_button_maxy39():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightslateblue')

def copy_button_maxy40():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumblue')

lb1 = Button(frame3, bd=0, text = 'Light\nSlate Blue',font='times 12 bold',
             fg='black', bg='lightslateblue', command= copy_button_maxy39)
lb1.place(x=494, y=185, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Medium\nBlue',font='times 12 bold',
             fg='black', bg='mediumblue', command=copy_button_maxy40)
lb2.place(x=576, y=185, width=80, height=35)


#=================row6_frame3=====================================
def copy_button_maxy41():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('royalblue')  

def copy_button_maxy42():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('dodgerblue')

def copy_button_maxy43():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('deepskyblue')

lb1 = Button(frame3, bd=0, text = 'Royal Blue',
 font='times 12 bold', fg='black', bg='royalblue', command= copy_button_maxy41)
lb1.place(x=2, y=222, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Dodger Blue', 
font='times 12 bold', fg='black', bg='dodgerblue', command=copy_button_maxy42)
lb2.place(x=84, y=222, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Deep\nsky Blue',
 font='times 12 bold',  fg='black', bg='deepskyblue',command=copy_button_maxy43)
lb3.place(x=166, y=222, width=80, height=35)

def copy_button_maxy44():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('skyblue')  

def copy_button_maxy45():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightskyblue')

def copy_button_maxy46():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('steelblue')

lb1 = Button(frame3, bd=0, text = 'Sky Blue',
 font='times 12 bold', fg='black', bg='skyblue', command= copy_button_maxy44)
lb1.place(x=248, y=222, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Light\nSky Blue', 
font='times 12 bold', fg='black', bg='slategray', command=copy_button_maxy45)
lb2.place(x=330, y=222, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Steel Blue',
 font='times 12 bold',  fg='black', bg='steelblue',command=copy_button_maxy46)
lb3.place(x=412, y=222, width=80, height=35)


def copy_button_maxy47():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightsteelblue')

def copy_button_maxy48():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightblue')

lb1 = Button(frame3, bd=0, text = 'Light\nSteel Blue',font='times 12 bold',
             fg='black', bg='lightsteelblue', command= copy_button_maxy47)
lb1.place(x=494, y=222, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Light Blue',font='times 12 bold',
             fg='black', bg='lightblue', command=copy_button_maxy48)
lb2.place(x=576, y=222, width=80, height=35)

#=================row7_frame3=====================================
def copy_button_maxy49():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('powderblue')  

def copy_button_maxy50():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('paleturquoise')

def copy_button_maxy51():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkturquoise')

lb1 = Button(frame3, bd=0, text = 'Powder\nBlue',
 font='times 12 bold', fg='black', bg='powderblue', command= copy_button_maxy49)
lb1.place(x=2, y=259, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Pale\nTurquoise', 
font='times 12 bold', fg='black', bg='paleturquoise', command=copy_button_maxy50)
lb2.place(x=84, y=259, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Dark\nTurquoise',
 font='times 12 bold',  fg='black', bg='darkturquoise',command=copy_button_maxy51)
lb3.place(x=166, y=259, width=80, height=35)

def copy_button_maxy52():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumturquoise')  

def copy_button_maxy53():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('turquoise')

def copy_button_maxy54():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cyan')

lb1 = Button(frame3, bd=0, text = 'Medium\nTurquoise',
 font='times 12 bold', fg='black', bg='mediumturquoise', command= copy_button_maxy54)
lb1.place(x=248, y=259, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Turquoise', 
font='times 12 bold', fg='black', bg='turquoise', command=copy_button_maxy53)
lb2.place(x=330, y=259, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Cyan',
 font='times 12 bold',  fg='black', bg='cyan',command=copy_button_maxy54)
lb3.place(x=412, y=259, width=80, height=35)


def copy_button_maxy55():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightcyan')

def copy_button_maxy56():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cadetblue')

lb1 = Button(frame3, bd=0, text = 'Light\nCyan',font='times 12 bold',
             fg='black', bg='lightslateblue', command= copy_button_maxy55)
lb1.place(x=494, y=259, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Cadet Blue',font='times 12 bold',
             fg='black', bg='mediumblue', command=copy_button_maxy56)
lb2.place(x=576, y=259, width=80, height=35)


#=================row8_frame3=====================================
def copy_button_maxy57():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumaquamarine')  

def copy_button_maxy58():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('aquamarine')

def copy_button_maxy59():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkgreen')

lb1 = Button(frame3, bd=0, text = 'Medium\nAquamarine',
 font='times 12 bold', fg='black', bg='mediumaquamarine', command= copy_button_maxy57)
lb1.place(x=2, y=296, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Aquamarine', 
font='times 12 bold', fg='black', bg='aquamarine', command=copy_button_maxy58)
lb2.place(x=84, y=296, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Dark Green',
 font='times 12 bold',  fg='black', bg='darkgreen',command=copy_button_maxy59)
lb3.place(x=166, y=296, width=80, height=35)

def copy_button_maxy60():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkolivegreen')  

def copy_button_maxy61():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkseagreen')

def copy_button_maxy62():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('seagreen')

lb1 = Button(frame3, bd=0, text = 'Dark Olive\nGreen',
 font='times 12 bold', fg='black', bg='darkolivegreen', command= copy_button_maxy60)
lb1.place(x=248, y=296, width=80, height=35)

lb2 = Button(frame3, bd=0, text = 'Dark Sea\nGreen', 
font='times 12 bold', fg='black', bg='darkseagreen', command=copy_button_maxy61)
lb2.place(x=330, y=296, width=80, height=35)

lb3 = Button(frame3, bd=0, text = 'Sea Green',
 font='times 12 bold',  fg='black', bg='seagreen',command=copy_button_maxy62)
lb3.place(x=412, y=296, width=80, height=35)


def copy_button_maxy63():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumseagreen')

def copy_button_maxy64():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightseagreen')

lb1 = Button(frame3, bd=0, text = 'Medium\nSea Green',font='times 12 bold',
             fg='black', bg='mediumseagreen', command= copy_button_maxy63)
lb1.place(x=494, y=296, width=80, height=35)

lb2 = Button(frame3, bd=0, text='Light\nSea Green',font='times 12 bold',
             fg='black', bg='lightblue', command=copy_button_maxy64)
lb2.place(x=576, y=296, width=80, height=35)

#===========================frame4 content========================
label_color = Label(frame4, text="This collection consit of all the available",
font="times 13",bg='cadetblue').place(x=32, y=3, width=280, height=30)
label_color2 = Label(frame4, text="and recogniced colors in tkinter and python",
font='times 13',bg='cadetblue').place(x=315, y=3, width=300, height=30)

control1 = Button(frame4, text= '>',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame5))
control1.place(x=625, y=3, width=30, height=30)

control2 = Button(frame4, text= '<',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame3))
control2.place(x=2, y=3, width=30, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('palegreen')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('springgreen')

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lawngreen')

lb1 = Button(frame4, bd=0, text = 'Pale\nGreen',
 font='times 12 bold', fg='black', bg='palegreen', command= copy_button_maxy1)
lb1.place(x=2, y=37, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Spring\nGreen', 
font='times 12 bold', fg='black', bg='springgreen', command=copy_button_maxy2)
lb2.place(x=84, y=37, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Lawn\nGreen',
 font='times 12 bold',  fg='black', bg='lawngreen',command=copy_button_maxy3)
lb3.place(x=166, y=37, width=80, height=35)

def copy_button_maxy4():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumspringgreen')  

def copy_button_maxy5():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('greenyellow')

def copy_button_maxy6():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('limegreen')

lb1 = Button(frame4, bd=0, text = 'Medium\nSpring Green',
 font='times 12 bold', fg='black', bg='mediumspringgreen', command= copy_button_maxy4)
lb1.place(x=248, y=37, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Green\nYellow', 
font='times 12 bold', fg='black', bg='greenyellow', command=copy_button_maxy5)
lb2.place(x=330, y=37, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Lime\nGreen',
 font='times 12 bold',  fg='black', bg='limegreen',command=copy_button_maxy6)
lb3.place(x=412, y=37, width=80, height=35)


def copy_button_maxy7():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append("snow")

def copy_button_maxy8():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('ghost white')

lb1 = Button(frame4, bd=0, text = 'snow',
 font='times 12 bold', fg='black', bg='snow', command= copy_button_maxy7)
lb1.place(x=494, y=37, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'ghost white',font='times 12 bold',
             fg='black', bg='ghost white', command=copy_button_maxy8)
lb2.place(x=576, y=37, width=80, height=35)

#=====================row2_frame4=================================
def copy_button_maxy9():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('yellowgreen')  

def copy_button_maxy10():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('forestgreen')

def copy_button_maxy11():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('olivedrab')

lb1 = Button(frame4, bd=0, text = 'Yellow\nGreen',
 font='times 12 bold', fg='black', bg='yellowgreen', command= copy_button_maxy9)
lb1.place(x=2, y=74, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Forest\nGreen', 
font='times 12 bold', fg='black', bg='forestgreen', command=copy_button_maxy10)
lb2.place(x=84, y=74, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Olive\nDrab',
 font='times 12 bold',  fg='black', bg='olivedrab',command=copy_button_maxy11)
lb3.place(x=166, y=74, width=80, height=35)

def copy_button_maxy12():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkkhaki')  

def copy_button_maxy13():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('khaki')

def copy_button_maxy14():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('palegoldenrod')

lb1 = Button(frame4, bd=0, text = 'Dark\nKhaki',
 font='times 12 bold', fg='black', bg='darkkhaki', command= copy_button_maxy12)
lb1.place(x=248, y=74, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Khaki', 
font='times 12 bold', fg='black', bg='khaki', command=copy_button_maxy13)
lb2.place(x=330, y=74, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Pale\nGoldenrod',
 font='times 12 bold',  fg='black', bg='palegoldenrod',command=copy_button_maxy14)
lb3.place(x=412, y=74, width=80, height=35)


def copy_button_maxy15():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightgoldenrodyellow')

def copy_button_maxy16():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightyellow')

lb1 = Button(frame4, bd=0, text = 'Light Goldenrod\nYellow',
 font='times 12 bold', fg='black', bg='lightgoldenrodyellow', command= copy_button_maxy15)
lb1.place(x=494, y=74, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Light Yellow',
             font='times 12 bold', fg='black', bg='lightyellow', command=copy_button_maxy16)
lb2.place(x=576, y=74, width=80, height=35)

#==================row3_frame4=====================================
def copy_button_maxy17():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('gold')  

def copy_button_maxy18():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightgoldenrod')

def copy_button_maxy19():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('goldenrod')

lb1 = Button(frame4, bd=0, text = 'Gold',
 font='times 12 bold', fg='black', bg='gold', command= copy_button_maxy17)
lb1.place(x=2, y=111, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Light\nGoldenrod', 
font='times 12 bold', fg='black', bg='lightgoldenrod', command=copy_button_maxy18)
lb2.place(x=84, y=111, width=80, height=35)

lb3 = Button(frame4, bd=0, text ='Goldenrod',
 font='times 12 bold',  fg='black', bg='goldenrod',command=copy_button_maxy19)
lb3.place(x=166, y=111, width=80, height=35)

def copy_button_maxy20():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkgoldenrod')  

def copy_button_maxy21():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('rosybrown')

def copy_button_maxy22():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('indianred')

lb1 = Button(frame4, bd=0, text = 'Dark\nGoldenrod',
 font='times 12 bold', fg='black', bg='darkgoldenrod', command= copy_button_maxy20)
lb1.place(x=248, y=111, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Rosy\nBrown', 
font='times 12 bold', fg='black', bg='rosybrown', command=copy_button_maxy21)
lb2.place(x=330, y=111, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Indian\nRed',
 font='times 12 bold',  fg='black', bg='indianred',command=copy_button_maxy22)
lb3.place(x=412, y=111, width=80, height=35)


def copy_button_maxy23():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('saddlebrown')

def copy_button_maxy24():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('sandybrown')

lb1 = Button(frame4, bd=0, text = 'Saddle\nBrown',
 font='times 12 bold', fg='black', bg='saddlebrown', command= copy_button_maxy23)
lb1.place(x=494, y=111, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Sandy\nBrown',
             font='times 12 bold', fg='black', bg='sandybrown', command=copy_button_maxy24)
lb2.place(x=576, y=111, width=80, height=35)


#=============================row4_frame4==========================
def copy_button_maxy25():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darksalmon')  

def copy_button_maxy26():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('salmon')

def copy_button_maxy27():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightsalmon')

lb1 = Button(frame4, bd=0, text = 'Dark\nSalmon',
 font='times 12 bold', fg='black', bg='darksalmon', command= copy_button_maxy25)
lb1.place(x=2, y=148, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Salmon', 
font='times 12 bold', fg='black', bg='salmon', command=copy_button_maxy26)
lb2.place(x=84, y=148, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Light\nSalmon',
 font='times 12 bold',  fg='black', bg='lightsalmon',command=copy_button_maxy27)
lb3.place(x=166, y=148, width=80, height=35)

def copy_button_maxy28():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkorange')  

def copy_button_maxy29():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('coral')

def copy_button_maxy30():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightcoral')

lb1 = Button(frame4, bd=0, text = 'Dark\nOrange',
 font='times 12 bold', fg='black', bg='darkorange', command= copy_button_maxy28)
lb1.place(x=248, y=148, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Coral', 
font='times 12 bold', fg='black', bg='coral', command=copy_button_maxy29)
lb2.place(x=330, y=148, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Light\nCoral',
 font='times 12 bold',  fg='black', bg='lightcoral',command=copy_button_maxy30)
lb3.place(x=412, y=148, width=80, height=35)


def copy_button_maxy31():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tomato')

def copy_button_maxy32():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orangered')

lb1 = Button(frame4, bd=0, text = 'Tomato',
 font='times 12 bold', fg='black', bg='tomato', command= copy_button_maxy31)
lb1.place(x=494, y=148, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Orange\nRed',font='times 12 bold',
             fg='black', bg='orangered', command=copy_button_maxy32)
lb2.place(x=576, y=148, width=80, height=35)


#=================row5_frame4=====================================
def copy_button_maxy33():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('hotpink')  

def copy_button_maxy34():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('deeppink')

def copy_button_maxy35():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('pink')

lb1 = Button(frame4, bd=0, text = 'Hot Pink',
 font='times 12 bold', fg='black', bg='hotpink', command= copy_button_maxy33)
lb1.place(x=2, y=185, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Deep Pink', 
font='times 12 bold', fg='black', bg='deeppink', command=copy_button_maxy34)
lb2.place(x=84, y=185, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'pink',
 font='times 12 bold',  fg='black', bg='pink',command=copy_button_maxy35)
lb3.place(x=166, y=185, width=80, height=35)

def copy_button_maxy36():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('lightpink')  

def copy_button_maxy37():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('palevioletred')

def copy_button_maxy38():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('maroon')

lb1 = Button(frame4, bd=0, text = 'Light\nPink',
 font='times 12 bold', fg='black', bg='lightpink', command= copy_button_maxy36)
lb1.place(x=248, y=185, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Pale\nViolet Red', 
font='times 12 bold', fg='black', bg='palevioletred', command=copy_button_maxy37)
lb2.place(x=330, y=185, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Maroon',
 font='times 12 bold',  fg='black', bg='maroon',command=copy_button_maxy38)
lb3.place(x=412, y=185, width=80, height=35)


def copy_button_maxy39():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumvioletred')

def copy_button_maxy40():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('violetred')

lb1 = Button(frame4, bd=0, text = 'Medium\nViolet Red',font='times 12 bold',
             fg='black', bg='mediumvioletred', command= copy_button_maxy39)
lb1.place(x=494, y=185, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Violet\nRed',font='times 12 bold',
             fg='black', bg='violetred', command=copy_button_maxy40)
lb2.place(x=576, y=185, width=80, height=35)


#=================row6_frame4=====================================
def copy_button_maxy41():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumorchid')  

def copy_button_maxy42():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkorchid')

def copy_button_maxy43():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('darkviolet')

lb1 = Button(frame4, bd=0, text = 'Medium\nOrchid',
 font='times 12 bold', fg='black', bg='mediumorchid', command= copy_button_maxy41)
lb1.place(x=2, y=222, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Dark\nOrchid', 
font='times 12 bold', fg='black', bg='darkorchid', command=copy_button_maxy42)
lb2.place(x=84, y=222, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Dark\nViolet',
 font='times 12 bold',  fg='black', bg='darkviolet',command=copy_button_maxy43)
lb3.place(x=166, y=222, width=80, height=35)

def copy_button_maxy44():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('blueviolet')  

def copy_button_maxy45():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('mediumpurple')

def copy_button_maxy46():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('thistle')

lb1 = Button(frame4, bd=0, text = 'Blue\nViolet',
 font='times 12 bold', fg='black', bg='blueviolet', command= copy_button_maxy44)
lb1.place(x=248, y=222, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Medium\nPurple', 
font='times 12 bold', fg='black', bg='mediumpurple', command=copy_button_maxy45)
lb2.place(x=330, y=222, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Thistle',
 font='times 12 bold',  fg='black', bg='thistle',command=copy_button_maxy46)
lb3.place(x=412, y=222, width=80, height=35)


def copy_button_maxy47():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('snow2')

def copy_button_maxy48():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('snow3')

lb1 = Button(frame4, bd=0, text = 'Snow2',font='times 12 bold',
             fg='black', bg='snow2', command= copy_button_maxy47)
lb1.place(x=494, y=222, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Snow3',font='times 12 bold',
             fg='black', bg='snow3', command=copy_button_maxy48)
lb2.place(x=576, y=222, width=80, height=35)

#=================row7_frame4=====================================
def copy_button_maxy49():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('snow4')  

def copy_button_maxy50():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('seashell2')

def copy_button_maxy51():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('seashell3')

lb1 = Button(frame4, bd=0, text = 'Snow4',
 font='times 12 bold', fg='black', bg='snow4', command= copy_button_maxy49)
lb1.place(x=2, y=259, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'seashell2', 
font='times 12 bold', fg='black', bg='seashell2', command=copy_button_maxy50)
lb2.place(x=84, y=259, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Seashell3',
 font='times 12 bold',  fg='black', bg='seashell3',command=copy_button_maxy51)
lb3.place(x=166, y=259, width=80, height=35)

def copy_button_maxy52():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('seashell4')  

def copy_button_maxy53():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('AntiqueWhite1')

def copy_button_maxy54():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'AntiqueWhite2')

lb1 = Button(frame4, bd=0, text = 'Seashell4',
 font='times 12 bold', fg='black', bg='Seashell4', command= copy_button_maxy54)
lb1.place(x=248, y=259, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Antique\nWhite1', 
font='times 12 bold', fg='black', bg='AntiqueWhite1', command=copy_button_maxy53)
lb2.place(x=330, y=259, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Antique\nWhite2',
 font='times 12 bold',  fg='black', bg='AntiqueWhite2',command=copy_button_maxy54)
lb3.place(x=412, y=259, width=80, height=35)


def copy_button_maxy55():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('AntiqueWhite3')

def copy_button_maxy56():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('AntiqueWhite4')

lb1 = Button(frame4, bd=0, text = 'Antique\nWhite3',font='times 12 bold',
             fg='black', bg='AntiqueWhite3', command= copy_button_maxy55)
lb1.place(x=494, y=259, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Antique\nWhite4',font='times 12 bold',
             fg='black', bg='AntiqueWhite4', command=copy_button_maxy56)
lb2.place(x=576, y=259, width=80, height=35)


#=================row8_frame4=====================================
def copy_button_maxy57():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('bisque2')  

def copy_button_maxy58():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('bisque3')

def copy_button_maxy59():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('bisque4')

lb1 = Button(frame4, bd=0, text = 'Bisque2',
 font='times 12 bold', fg='black', bg='bisque2', command= copy_button_maxy57)
lb1.place(x=2, y=296, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Bisque3', 
font='times 12 bold', fg='black', bg='bisque3', command=copy_button_maxy58)
lb2.place(x=84, y=296, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Bisque4',
 font='times 12 bold',  fg='black', bg='bisque4',command=copy_button_maxy59)
lb3.place(x=166, y=296, width=80, height=35)

def copy_button_maxy60():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PeachPuff2')  

def copy_button_maxy61():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PeachPuff3')

def copy_button_maxy62():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PeachPuff4')

lb1 = Button(frame4, bd=0, text = 'Peach\nPuff2',
 font='times 12 bold', fg='black', bg='PeachPuff2', command= copy_button_maxy60)
lb1.place(x=248, y=296, width=80, height=35)

lb2 = Button(frame4, bd=0, text = 'Peach\nPuff3', 
font='times 12 bold', fg='black', bg='PeachPuff3', command=copy_button_maxy61)
lb2.place(x=330, y=296, width=80, height=35)

lb3 = Button(frame4, bd=0, text = 'Peach\nPuff4',
 font='times 12 bold',  fg='black', bg='PeachPuff4',command=copy_button_maxy62)
lb3.place(x=412, y=296, width=80, height=35)


def copy_button_maxy63():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('NavajoWhite2')

def copy_button_maxy64():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('NavajoWhite3')

lb1 = Button(frame4, bd=0, text ='Navajo\nWhite2',font='times 12 bold',
             fg='black', bg='NavajoWhite2', command= copy_button_maxy63)
lb1.place(x=494, y=296, width=80, height=35)

lb2 = Button(frame4, bd=0, text='Navajo\nWhite3',font='times 12 bold',
             fg='black', bg='NavajoWhite3', command=copy_button_maxy64)
lb2.place(x=576, y=296, width=80, height=35)
#======================frame4_closed===============


#=================frame5 content==================
label_color = Label(frame5, text="This collection consit of all the available",
font="times 13",bg='cadetblue').place(x=32, y=3, width=280, height=30)
label_color2 = Label(frame5, text="and recogniced colors in tkinter and python",
font='times 13',bg='cadetblue').place(x=315, y=3, width=300, height=30)

control1 = Button(frame5, text= '>',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame6))
control1.place(x=625, y=3, width=30, height=30)

control2 = Button(frame5, text= '<',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame4) )
control2.place(x=2, y=3, width=30, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('NavajoWhite4')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LemonChiffon2')

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LemonChiffon3')

lb1 = Button(frame5, bd=0, text = 'Navajo\nWhite4',
 font='times 12 bold', fg='black', bg='NavajoWhite4', command= copy_button_maxy1)
lb1.place(x=2, y=37, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Lemon\nChiffon2', 
font='times 12 bold', fg='black', bg='LemonChiffon2', command=copy_button_maxy2)
lb2.place(x=84, y=37, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'LemonChiffon3',
 font='times 12 bold',  fg='black', bg='LemonChiffon3',command=copy_button_maxy3)
lb3.place(x=166, y=37, width=80, height=35)

def copy_button_maxy4():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LemonChiffon4')  

def copy_button_maxy5():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cornsilk2')

def copy_button_maxy6():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cornsilk3')

lb1 = Button(frame5, bd=0, text = 'Lemon\nChiffon4',
 font='times 12 bold', fg='black', bg='LemonChiffon4', command= copy_button_maxy4)
lb1.place(x=248, y=37, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'cornsilk2', 
font='times 12 bold', fg='black', bg='cornsilk2', command=copy_button_maxy5)
lb2.place(x=330, y=37, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'cornsilk3',
 font='times 12 bold',  fg='black', bg='cornsilk3',command=copy_button_maxy6)
lb3.place(x=412, y=37, width=80, height=35)


def copy_button_maxy7():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cornsilk4')

def copy_button_maxy8():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'ivory2')

lb1 = Button(frame5, bd=0, text = 'Cornsilk4',
 font='times 12 bold', fg='black', bg='cornsilk4', command= copy_button_maxy7)
lb1.place(x=494, y=37, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Ivory2',font='times 12 bold',
             fg='black', bg='ivory2', command=copy_button_maxy8)
lb2.place(x=576, y=37, width=80, height=35)

#=====================row2_frame5=================================
def copy_button_maxy9():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('ivory3')  

def copy_button_maxy10():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('ivory4')

def copy_button_maxy11():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('honeydew2')

lb1 = Button(frame5, bd=0, text = 'Ivory3',
 font='times 12 bold', fg='black', bg='ivory3', command= copy_button_maxy9)
lb1.place(x=2, y=74, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Ivory4', 
font='times 12 bold', fg='black', bg='ivory4', command=copy_button_maxy10)
lb2.place(x=84, y=74, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Honeydew2',
 font='times 12 bold',  fg='black', bg='honeydew2',command=copy_button_maxy11)
lb3.place(x=166, y=74, width=80, height=35)

def copy_button_maxy12():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('honeydew3')  

def copy_button_maxy13():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('honeydew4')

def copy_button_maxy14():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LavenderBlush2')

lb1 = Button(frame5, bd=0, text = 'Honeydew3',
 font='times 12 bold', fg='black', bg='honeydew3', command= copy_button_maxy12)
lb1.place(x=248, y=74, width=80, height=35)

lb2 = Button(frame5, bd=0, text = "Honeydew4", 
font='times 12 bold', fg='black', bg='honeydew4', command=copy_button_maxy13)
lb2.place(x=330, y=74, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Lavender\nBlush2',
 font='times 12 bold',  fg='black', bg='LavenderBlush2',command=copy_button_maxy14)
lb3.place(x=412, y=74, width=80, height=35)


def copy_button_maxy15():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LavenderBlush3')

def copy_button_maxy16():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LavenderBlush4')

lb1 = Button(frame5, bd=0, text = 'LavenderBlush3',
 font='times 12 bold', fg='black', bg='LavenderBlush3', command= copy_button_maxy15)
lb1.place(x=494, y=74, width=80, height=35)

lb2 = Button(frame5, bd=0, text='Lavender\nBlush4',
             font='times 12 bold', fg='black', bg='LavenderBlush4', command=copy_button_maxy16)
lb2.place(x=576, y=74, width=80, height=35)

#==================row3_frame5=====================================
def copy_button_maxy17():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'MistyRose2')  

def copy_button_maxy18():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MistyRose3')

def copy_button_maxy19():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MistyRose4')

lb1 = Button(frame5, bd=0, text = 'Misty\nRose2',
 font='times 12 bold', fg='black', bg='MistyRose2', command= copy_button_maxy17)
lb1.place(x=2, y=111, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Misty\nRose3', 
font='times 12 bold', fg='black', bg='MistyRose3', command=copy_button_maxy18)
lb2.place(x=84, y=111, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Misty\nRose4',
 font='times 12 bold',  fg='black', bg='MistyRose4',command=copy_button_maxy19)
lb3.place(x=166, y=111, width=80, height=35)

def copy_button_maxy20():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('azure2')  

def copy_button_maxy21():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('azure3')

def copy_button_maxy22():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('azure4')

lb1 = Button(frame5, bd=0, text = 'Azure2',
 font='times 12 bold', fg='black', bg='azure2', command= copy_button_maxy20)
lb1.place(x=248, y=111, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Azure2', 
font='times 12 bold', fg='black', bg='azure2', command=copy_button_maxy21)
lb2.place(x=330, y=111, width=80, height=35)

lb3 = Button(frame5, bd=0, text = "Azure4",
 font='times 12 bold',  fg='black', bg='azure4',command=copy_button_maxy22)
lb3.place(x=412, y=111, width=80, height=35)


def copy_button_maxy23():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateBlue1')

def copy_button_maxy24():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateBlue2')

lb1 = Button(frame5, bd=0, text = 'Slate\nBlue1',
 font='times 12 bold', fg='black', bg='SlateBlue1', command= copy_button_maxy23)
lb1.place(x=494, y=111, width=80, height=35)

lb2 = Button(frame5, bd=0, text='SlateBlue2',
             font='times 12 bold', fg='black', bg='SlateBlue2', command=copy_button_maxy24)
lb2.place(x=576, y=111, width=80, height=35)


#=============================row4_frame5==========================
def copy_button_maxy25():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateBlue3')  

def copy_button_maxy26():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateBlue4')

def copy_button_maxy27():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RoyalBlue1')

lb1 = Button(frame5, bd=0, text = 'Slate\nBlue3',
 font='times 12 bold', fg='black', bg='SlateBlue3', command= copy_button_maxy25)
lb1.place(x=2, y=148, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Slate\nBlue4', 
font='times 12 bold', fg='black', bg='SlateBlue4', command=copy_button_maxy26)
lb2.place(x=84, y=148, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Royal\nBlue1',
 font='times 12 bold',  fg='black', bg='RoyalBlue1',command=copy_button_maxy27)
lb3.place(x=166, y=148, width=80, height=35)

def copy_button_maxy28():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RoyalBlue2')  

def copy_button_maxy29():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RoyalBlue3')

def copy_button_maxy30():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RoyalBlue4')

lb1 = Button(frame5, bd=0, text = 'Royal\nBlue2',
 font='times 12 bold', fg='black', bg='RoyalBlue2', command= copy_button_maxy28)
lb1.place(x=248, y=148, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Royal\nBlue3', 
font='times 12 bold', fg='black', bg='RoyalBlue3', command=copy_button_maxy29)
lb2.place(x=330, y=148, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Royal\nBlue4',
 font='times 12 bold',  fg='black', bg='RoyalBlue4',command=copy_button_maxy30)
lb3.place(x=412, y=148, width=80, height=35)


def copy_button_maxy31():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('blue2')

def copy_button_maxy32():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('blue3')

lb1 = Button(frame5, bd=0, text = 'Blue2',
 font='times 12 bold', fg='black', bg='blue2', command= copy_button_maxy31)
lb1.place(x=494, y=148, width=80, height=35)

lb2 = Button(frame5, bd=0, text='blue3',font='times 12 bold',
             fg='black', bg='blue3', command=copy_button_maxy32)
lb2.place(x=576, y=148, width=80, height=35)


#=================row5_frame5=====================================
def copy_button_maxy33():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('blue4')  

def copy_button_maxy34():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DodgerBlue2')

def copy_button_maxy35():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DodgerBlue3')

lb1 = Button(frame5, bd=0, text = 'Blue4',
 font='times 12 bold', fg='black', bg='blue4', command= copy_button_maxy33)
lb1.place(x=2, y=185, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Dodger\nBlue2', 
font='times 12 bold', fg='black', bg='DodgerBlue2', command=copy_button_maxy34)
lb2.place(x=84, y=185, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Dodger\nBlue3',
 font='times 12 bold',  fg='black', bg='DodgerBlue3',command=copy_button_maxy35)
lb3.place(x=166, y=185, width=80, height=35)

def copy_button_maxy36():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DodgerBlue4')  

def copy_button_maxy37():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SteelBlue1')

def copy_button_maxy38():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SteelBlue2')

lb1 = Button(frame5, bd=0, text = 'Dodger\nBlue4',
 font='times 12 bold', fg='black', bg='darkslateblue', command= copy_button_maxy36)
lb1.place(x=248, y=185, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Steel\nBlue1', 
font='times 12 bold', fg='black', bg='SteelBlue1', command=copy_button_maxy37)
lb2.place(x=330, y=185, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'SteelBlue2',
 font='times 12 bold',  fg='black', bg='SteelBlue2',command=copy_button_maxy38)
lb3.place(x=412, y=185, width=80, height=35)


def copy_button_maxy39():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SteelBlue3')

def copy_button_maxy40():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SteelBlue4')

lb1 = Button(frame5, bd=0, text ='Steel\nBlue3',font='times 12 bold',
             fg='black', bg='SteelBlue3', command= copy_button_maxy39)
lb1.place(x=494, y=185, width=80, height=35)

lb2 = Button(frame5, bd=0, text='Steel\nBlue4',font='times 12 bold',
             fg='black', bg='SteelBlue4', command=copy_button_maxy40)
lb2.place(x=576, y=185, width=80, height=35)


#=================row6_frame5=====================================
def copy_button_maxy41():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DeepSkyBlue2')  

def copy_button_maxy42():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DeepSkyBlue3')

def copy_button_maxy43():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DeepSkyBlue4')

lb1 = Button(frame5, bd=0, text = 'Deep Sky\nBlue2',
 font='times 12 bold', fg='black', bg='DeepSkyBlue2', command= copy_button_maxy41)
lb1.place(x=2, y=222, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Deep Sky\nBlue3', 
font='times 12 bold', fg='black', bg='DeepSkyBlue3', command=copy_button_maxy42)
lb2.place(x=84, y=222, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Deep Sky\nBlue4',
 font='times 12 bold',  fg='black', bg='DeepSkyBlue4',command=copy_button_maxy43)
lb3.place(x=166, y=222, width=80, height=35)

def copy_button_maxy44():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('skyblue1')  

def copy_button_maxy45():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('skyblue2')

def copy_button_maxy46():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('skyblue3')

lb1 = Button(frame5, bd=0, text = 'Sky Blue1',
 font='times 12 bold', fg='black', bg='skyblue1', command= copy_button_maxy44)
lb1.place(x=248, y=222, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'sky blue2', 
font='times 12 bold', fg='black', bg='skyblue2', command=copy_button_maxy45)
lb2.place(x=330, y=222, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'skyblue3',
 font='times 12 bold',  fg='black', bg='skyblue3',command=copy_button_maxy46)
lb3.place(x=412, y=222, width=80, height=35)


def copy_button_maxy47():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SkyBlue4')

def copy_button_maxy48():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSkyBlue1')

lb1 = Button(frame5, bd=0, text = 'Sky\nBlue4',font='times 12 bold',
             fg='black', bg='SkyBlue4', command= copy_button_maxy47)
lb1.place(x=494, y=222, width=80, height=35)

lb2 = Button(frame5, bd=0, text='Light\nSky Blue1',font='times 12 bold',
             fg='black', bg='LightSkyBlue1', command=copy_button_maxy48)
lb2.place(x=576, y=222, width=80, height=35)

#=================row7_frame5=====================================
def copy_button_maxy49():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSkyBlue2')  

def copy_button_maxy50():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSkyBlue3')

def copy_button_maxy51():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSkyBlue4')

lb1 = Button(frame5, bd=0, text = 'Light\nSky Blue2',
 font='times 12 bold', fg='black', bg='LightSkyBlue2', command= copy_button_maxy49)
lb1.place(x=2, y=259, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Light\nSky Blue3', 
font='times 12 bold', fg='black', bg='LightSky Blue3', command=copy_button_maxy50)
lb2.place(x=84, y=259, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Light\nSky Blue4',
 font='times 12 bold',  fg='black', bg='LightSkyBlue4',command=copy_button_maxy51)
lb3.place(x=166, y=259, width=80, height=35)

def copy_button_maxy52():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateGray1')  

def copy_button_maxy53():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateGray2')

def copy_button_maxy54():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateGray3')

lb1 = Button(frame5, bd=0, text = 'Slate\nGray1',
 font='times 12 bold', fg='black', bg='SlateGray1', command= copy_button_maxy54)
lb1.place(x=248, y=259, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Slate\nGray2', 
font='times 12 bold', fg='black', bg='SlateGray2', command=copy_button_maxy53)
lb2.place(x=330, y=259, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Slate\nGray3',
 font='times 12 bold',  fg='black', bg='SlateGray3',command=copy_button_maxy54)
lb3.place(x=412, y=259, width=80, height=35)


def copy_button_maxy55():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SlateGray4')

def copy_button_maxy56():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSteelBlue1')

lb1 = Button(frame5, bd=0, text = 'Slate\nGray4',font='times 12 bold',
             fg='black', bg='SlateGray4', command= copy_button_maxy55)
lb1.place(x=494, y=259, width=80, height=35)

lb2 = Button(frame5, bd=0, text='Light\nSteel Blue1',font='times 12 bold',
             fg='black', bg='LightSteelBlue1', command=copy_button_maxy56)
lb2.place(x=576, y=259, width=80, height=35)


#=================row8_frame5=====================================
def copy_button_maxy57():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSteelBlue2')  

def copy_button_maxy58():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSteelBlue3')

def copy_button_maxy59():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSteelBlue4')

lb1 = Button(frame5, bd=0, text = 'Light\nSteel Blue2',
 font='times 12 bold', fg='black', bg='LightSteelBlue2', command= copy_button_maxy57)
lb1.place(x=2, y=296, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Light\nSteel Blue3', 
font='times 12 bold', fg='black', bg='LightSteelBlue3', command=copy_button_maxy58)
lb2.place(x=84, y=296, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Light\nSteel Blue4',
 font='times 12 bold',  fg='black', bg='LightSteelBlue4',command=copy_button_maxy59)
lb3.place(x=166, y=296, width=80, height=35)

def copy_button_maxy60():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('Light\nBlue1')  

def copy_button_maxy61():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('Light\nBlue2')

def copy_button_maxy62():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('Light\nBlue3')

lb1 = Button(frame5, bd=0, text = 'Light\nBlue1',
 font='times 12 bold', fg='black', bg='LightBlue1', command= copy_button_maxy60)
lb1.place(x=248, y=296, width=80, height=35)

lb2 = Button(frame5, bd=0, text = 'Light\nBlue2', 
font='times 12 bold', fg='black', bg='LightBlue2', command=copy_button_maxy61)
lb2.place(x=330, y=296, width=80, height=35)

lb3 = Button(frame5, bd=0, text = 'Light\nBlue3',
 font='times 12 bold',  fg='black', bg='LightBlue1',command=copy_button_maxy62)
lb3.place(x=412, y=296, width=80, height=35)


def copy_button_maxy63():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightBlue4')

def copy_button_maxy64():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightCyan2')

lb1 = Button(frame5, bd=0, text = 'Light\nBlue4',font='times 12 bold',
             fg='black', bg='LightBlue4', command= copy_button_maxy63)
lb1.place(x=494, y=296, width=80, height=35)

lb2 = Button(frame5, bd=0, text='Light\nCyan2',font='times 12 bold',
             fg='black', bg='LightCyan2', command=copy_button_maxy64)
lb2.place(x=576, y=296, width=80, height=35)

#=============================frame5_closed===================================


#=================frame6 content==============================================
label_color = Label(frame6, text="This collection consit of all the available",
font="times 13",bg='cadetblue').place(x=32, y=3, width=280, height=30)
label_color2 = Label(frame6, text="and recogniced colors in tkinter and python",
font='times 13',bg='cadetblue').place(x=315, y=3, width=300, height=30)

control1 = Button(frame6, text= '>',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame7))
control1.place(x=625, y=3, width=30, height=30)

control2 = Button(frame6, text= '<',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame5))
control2.place(x=2, y=3, width=30, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightCyan3')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightCyan4')

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleTurquoise1')

lb1 = Button(frame6, bd=0, text = 'Light\nCyan3',
 font='times 12 bold', fg='black', bg='LightCyan3', command= copy_button_maxy1)
lb1.place(x=2, y=37, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Light\nCyan4',
             font='times 12 bold', fg='black', bg='LightCyan4', command=copy_button_maxy2)
lb2.place(x=84, y=37, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Pale\nTurquoise1',
 font='times 12 bold',  fg='black', bg='PaleTurquoise1',command=copy_button_maxy3)
lb3.place(x=166, y=37, width=80, height=35)

def copy_button_maxy4():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleTurquoise2')  

def copy_button_maxy5():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleTurquoise3')

def copy_button_maxy6():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleTurquoise4')

lb1 = Button(frame6, bd=0, text = 'Pale\nTurquoise2',
 font='times 12 bold', fg='black', bg='PaleTurquoise2', command= copy_button_maxy4)
lb1.place(x=248, y=37, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Pale\nTurquoise3', 
font='times 12 bold', fg='black', bg='PaleTurquoise3', command=copy_button_maxy5)
lb2.place(x=330, y=37, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Pale\nTurquoise4',
 font='times 12 bold',  fg='black', bg='PaleTurquoise4',command=copy_button_maxy6)
lb3.place(x=412, y=37, width=80, height=35)


def copy_button_maxy7():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('CadetBlue1')

def copy_button_maxy8():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('CadetBlue2')

lb1 = Button(frame6, bd=0, text = 'Cadet\nBlue1',
 font='times 12 bold', fg='black', bg='CadetBlue1', command= copy_button_maxy7)
lb1.place(x=494, y=37, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Cadet\nBlue2',font='times 12 bold',
             fg='black', bg='CadetBlue2', command=copy_button_maxy8)
lb2.place(x=576, y=37, width=80, height=35)

#=====================row2_frame3=================================
def copy_button_maxy9():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('CadetBlue3')  

def copy_button_maxy10():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('CadetBlue4')

def copy_button_maxy11():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('turquoise1')

lb1 = Button(frame6, bd=0, text = 'Cadet\nBlue3',
 font='times 12 bold', fg='black', bg='CadetBlue3', command= copy_button_maxy9)
lb1.place(x=2, y=74, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Cadet\nBlue4', 
font='times 12 bold', fg='black', bg='CadetBlue4', command=copy_button_maxy10)
lb2.place(x=84, y=74, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Turquoise1',
 font='times 12 bold',  fg='black', bg='turquoise1',command=copy_button_maxy11)
lb3.place(x=166, y=74, width=80, height=35)

def copy_button_maxy12():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('turquoise2')  

def copy_button_maxy13():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('turquoise3')

def copy_button_maxy14():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('turquoise4')

lb1 = Button(frame6, bd=0, text = 'Turquoise2',
 font='times 12 bold', fg='black', bg='turquoise2', command= copy_button_maxy12)
lb1.place(x=248, y=74, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Turquoise3', 
font='times 12 bold', fg='black', bg='turquoise3', command=copy_button_maxy13)
lb2.place(x=330, y=74, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Turquoise4',
 font='times 12 bold',  fg='black', bg='turquoise4',command=copy_button_maxy14)
lb3.place(x=412, y=74, width=80, height=35)


def copy_button_maxy15():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cyan2')

def copy_button_maxy16():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('cyan3')

lb1 = Button(frame6, bd=0, text = 'Cyan2',
 font='times 12 bold', fg='black', bg='cyan2', command= copy_button_maxy15)
lb1.place(x=494, y=74, width=80, height=35)

lb2 = Button(frame6, bd=0, text='cyan3',font='times 12 bold',
             fg='black', bg='cyan3', command=copy_button_maxy16)
lb2.place(x=576, y=74, width=80, height=35)

#==================row3_frame3=====================================
def copy_button_maxy17():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'cyan4')  

def copy_button_maxy18():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSlateGray1')

def copy_button_maxy19():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSlateGray2')

lb1 = Button(frame6, bd=0, text = 'Cyan4',
 font='times 12 bold', fg='black', bg='cyan4', command= copy_button_maxy17)
lb1.place(x=2, y=111, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Dark\nSlate Gray1', 
font='times 12 bold', fg='black', bg='DarkSlateGray1', command=copy_button_maxy18)
lb2.place(x=84, y=111, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Dark\nSlate Gray2',
 font='times 12 bold',  fg='black', bg='DarkSlateGray2',command=copy_button_maxy19)
lb3.place(x=166, y=111, width=80, height=35)

def copy_button_maxy20():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSlateGray3')  

def copy_button_maxy21():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSlateGray4')

def copy_button_maxy22():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('aquamarine2')

lb1 = Button(frame6, bd=0, text ='Dark\nSlate Gray3',
 font='times 12 bold', fg='black', bg='DarkSlateGray3', command= copy_button_maxy20)
lb1.place(x=248, y=111, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Dark\nSlate Gray4', 
font='times 12 bold', fg='black', bg='DarkSlateGray4', command=copy_button_maxy21)
lb2.place(x=330, y=111, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Aquamarine2',
 font='times 12 bold',  fg='black', bg='aquamarine2',command=copy_button_maxy22)
lb3.place(x=412, y=111, width=80, height=35)


def copy_button_maxy23():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('aquamarine4')

def copy_button_maxy24():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSeaGreen1')

lb1 = Button(frame6, bd=0, text = 'Aquamarine4',
 font='times 12 bold', fg='black', bg='aquamarine4', command= copy_button_maxy23)
lb1.place(x=494, y=111, width=80, height=35)

lb2 = Button(frame6, bd=0, text='Dark\nSeaGreen1',font='times 12 bold',
             fg='black', bg='DarkSeaGreen1', command=copy_button_maxy24)
lb2.place(x=576, y=111, width=80, height=35)


#=============================row4_frame6==========================
def copy_button_maxy25():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSeaGreen2')  

def copy_button_maxy26():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSeaGreen3')

def copy_button_maxy27():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkSeaGreen4')

lb1 = Button(frame6, bd=0, text = 'Dark\nSea Green2',
 font='times 12 bold', fg='black', bg='lavenderblush', command= copy_button_maxy25)
lb1.place(x=2, y=148, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Dark\nSea Green3', 
font='times 12 bold', fg='black', bg='DarkSeaGreen3', command=copy_button_maxy26)
lb2.place(x=84, y=148, width=80, height=35)

lb3 = Button(frame6, bd=0, text ='Dark\nSea Green4',
 font='times 12 bold',  fg='black', bg='DarkSeaGreen4',command=copy_button_maxy27)
lb3.place(x=166, y=148, width=80, height=35)

def copy_button_maxy28():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SeaGreen1')  

def copy_button_maxy29():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SeaGreen2')

def copy_button_maxy30():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SeaGreen3')

lb1 = Button(frame6, bd=0, text = 'Sea\nGreen1',
 font='times 12 bold', fg='black', bg='SeaGreen1', command= copy_button_maxy28)
lb1.place(x=248, y=148, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Sea\nGreen2', 
font='times 12 bold', fg='black', bg='SeaGreen2', command=copy_button_maxy29)
lb2.place(x=330, y=148, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Sea\nGreen3',
 font='times 12 bold',  fg='black', bg='SeaGreen3',command=copy_button_maxy30)
lb3.place(x=412, y=148, width=80, height=35)


def copy_button_maxy31():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleGreen1')

def copy_button_maxy32():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleGreen2')

lb1 = Button(frame6, bd=0, text = 'Pale\nGreen1',
 font='times 12 bold', fg='black', bg='PaleGreen1', command= copy_button_maxy31)
lb1.place(x=494, y=148, width=80, height=35)

lb2 = Button(frame6, bd=0, text='Pale\nGreen2',font='times 12 bold',
             fg='black', bg='PaleGreen2', command=copy_button_maxy32)
lb2.place(x=576, y=148, width=80, height=35)


#=================row5_frame6=====================================
def copy_button_maxy33():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleGreen3')  

def copy_button_maxy34():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleGreen4')

def copy_button_maxy35():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SpringGreen2')

lb1 = Button(frame6, bd=0, text = 'Pale\nGreen3',
 font='times 12 bold', fg='black', bg='PaleGreen3', command= copy_button_maxy33)
lb1.place(x=2, y=185, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Pale\nGreen4', 
font='times 12 bold', fg='black', bg='PaleGreen4', command=copy_button_maxy34)
lb2.place(x=84, y=185, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Spring\nGreen2',
 font='times 12 bold',  fg='black', bg='SpringGreen2',command=copy_button_maxy35)
lb3.place(x=166, y=185, width=80, height=35)

def copy_button_maxy36():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SpringGreen3')  

def copy_button_maxy37():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('SpringGreen4')

def copy_button_maxy38():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('green2')

lb1 = Button(frame6, bd=0, text = 'Spring\nGreen3',
 font='times 12 bold', fg='black', bg='SpringGreen3', command= copy_button_maxy36)
lb1.place(x=248, y=185, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Spring\nGreen4', 
font='times 12 bold', fg='black', bg='SpringGreen4', command=copy_button_maxy37)
lb2.place(x=330, y=185, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Green2',
 font='times 12 bold',  fg='black', bg='green2',command=copy_button_maxy38)
lb3.place(x=412, y=185, width=80, height=35)


def copy_button_maxy39():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('green3')

def copy_button_maxy40():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('green4')

lb1 = Button(frame6, bd=0, text = 'Green3',font='times 12 bold',
             fg='black', bg='green3', command= copy_button_maxy39)
lb1.place(x=494, y=185, width=80, height=35)

lb2 = Button(frame6, bd=0, text='Green4',font='times 12 bold',
             fg='black', bg='green4', command=copy_button_maxy40)
lb2.place(x=576, y=185, width=80, height=35)


#=================row6_frame6=====================================
def copy_button_maxy41():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('chartreuse2')  

def copy_button_maxy42():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('chartreuse3')

def copy_button_maxy43():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('chartreuse4')

lb1 = Button(frame6, bd=0, text = 'Chartreuse2',
 font='times 12 bold', fg='black', bg='chartreuse2', command= copy_button_maxy41)
lb1.place(x=2, y=222, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Chartreuse3', 
font='times 12 bold', fg='black', bg='chartreuse3', command=copy_button_maxy42)
lb2.place(x=84, y=222, width=80, height=35)

lb3 = Button(frame6, bd=0, text ='Chartreuse4',
 font='times 12 bold',  fg='black', bg='chartreuse4',command=copy_button_maxy43)
lb3.place(x=166, y=222, width=80, height=35)

def copy_button_maxy44():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('OliveDrab1')  

def copy_button_maxy45():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('OliveDrab2')

def copy_button_maxy46():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('OliveDrab4')

lb1 = Button(frame6, bd=0, text = 'Olive\nDrab1',
 font='times 12 bold', fg='black', bg='OliveDrab1', command= copy_button_maxy44)
lb1.place(x=248, y=222, width=80, height=35)

lb2 = Button(frame6, bd=0, text ='Olive\nDrab2', 
font='times 12 bold', fg='black', bg='OliveDrab2', command=copy_button_maxy45)
lb2.place(x=330, y=222, width=80, height=35)

lb3 = Button(frame6, bd=0, text ='Olive\nDrab4',
 font='times 12 bold',  fg='black', bg='OliveDrab4',command=copy_button_maxy46)
lb3.place(x=412, y=222, width=80, height=35)


def copy_button_maxy47():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOliveGreen1')

def copy_button_maxy48():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOliveGreen2')

lb1 = Button(frame6, bd=0, text ='DarkOlive\nGreen1',font='times 12 bold',
             fg='black', bg='DarkOliveGreen1', command= copy_button_maxy47)
lb1.place(x=494, y=222, width=80, height=35)

lb2 = Button(frame6, bd=0, text='DarkOlive\nGreen2',font='times 12 bold',
             fg='black', bg='DarkOliveGreen2', command=copy_button_maxy48)
lb2.place(x=576, y=222, width=80, height=35)

#=================row7_frame6=====================================
def copy_button_maxy49():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOliveGreen3')  

def copy_button_maxy50():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOliveGreen4')

def copy_button_maxy51():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('khaki1')

lb1 = Button(frame6, bd=0, text ='Dark Olive\nGreen3',
 font='times 12 bold', fg='black', bg='DarkOliveGreen3', command= copy_button_maxy49)
lb1.place(x=2, y=259, width=80, height=35)

lb2 = Button(frame6, bd=0, text ='Dark Olive\nGreen4', 
font='times 12 bold', fg='black', bg='DarkOliveGreen4', command=copy_button_maxy50)
lb2.place(x=84, y=259, width=80, height=35)

lb3 = Button(frame6, bd=0, text ='Khaki1',
 font='times 12 bold',  fg='black', bg='khaki1',command=copy_button_maxy51)
lb3.place(x=166, y=259, width=80, height=35)

def copy_button_maxy52():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('khaki2')  

def copy_button_maxy53():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('khaki3')

def copy_button_maxy54():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('khaki4')

lb1 = Button(frame6, bd=0, text ='Khaki2',
 font='times 12 bold', fg='black', bg='khaki2', command= copy_button_maxy54)
lb1.place(x=248, y=259, width=80, height=35)

lb2 = Button(frame6, bd=0, text ='Khaki3', 
font='times 12 bold', fg='black', bg='khaki3', command=copy_button_maxy53)
lb2.place(x=330, y=259, width=80, height=35)

lb3 = Button(frame6, bd=0, text ='Khaki4',
 font='times 12 bold',  fg='black', bg='khaki4',command=copy_button_maxy54)
lb3.place(x=412, y=259, width=80, height=35)


def copy_button_maxy55():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'LightGoldenrod1')

def copy_button_maxy56():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'LightGoldenrod2')

lb1 = Button(frame6, bd=0, text = 'Light\nGoldenrod1',font='times 12 bold',
             fg='black', bg= 'LightGoldenrod1', command= copy_button_maxy55)
lb1.place(x=494, y=259, width=80, height=35)

lb2 = Button(frame6, bd=0, text= 'Light\nGoldenrod2',font='times 12 bold',
             fg='black', bg= 'LightGoldenrod2', command=copy_button_maxy56)
lb2.place(x=576, y=259, width=80, height=35)


#=================row8_frame6=====================================
def copy_button_maxy57():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'LightGoldenrod3')  

def copy_button_maxy58():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'LightGoldenrod4')

def copy_button_maxy59():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightYellow2')

lb1 = Button(frame6, bd=0, text ='Light\nGoldenrod3',
 font='times 12 bold', fg='black', bg='LightGoldenrod3', command= copy_button_maxy57)
lb1.place(x=2, y=296, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Light\nGoldenrod4', 
font='times 12 bold', fg='black', bg='LightGoldenrod4', command=copy_button_maxy58)
lb2.place(x=84, y=296, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Light\nYellow2',
 font='times 12 bold',  fg='black', bg='LightYellow2',command=copy_button_maxy59)
lb3.place(x=166, y=296, width=80, height=35)

def copy_button_maxy60():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightYellow3')  

def copy_button_maxy61():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightYellow4')

def copy_button_maxy62():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('yellow2')

lb1 = Button(frame6, bd=0, text ='Light\nYellow3',
 font='times 12 bold', fg='black', bg='LightYellow3', command= copy_button_maxy60)
lb1.place(x=248, y=296, width=80, height=35)

lb2 = Button(frame6, bd=0, text = 'Light\nYellow4', 
font='times 12 bold', fg='black', bg='LightYellow4', command=copy_button_maxy61)
lb2.place(x=330, y=296, width=80, height=35)

lb3 = Button(frame6, bd=0, text = 'Yellow2',
 font='times 12 bold',  fg='black', bg='yellow2',command=copy_button_maxy62)
lb3.place(x=412, y=296, width=80, height=35)


def copy_button_maxy63():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('yellow3')

def copy_button_maxy64():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('yellow4')

lb1 = Button(frame6, bd=0, text ='Yellow3',font='times 12 bold',
             fg='black', bg='yellow3', command= copy_button_maxy63)
lb1.place(x=494, y=296, width=80, height=35)

lb2 = Button(frame6, bd=0, text='Yellow4',font='times 12 bold',
             fg='black', bg='yellow4', command=copy_button_maxy64)
lb2.place(x=576, y=296, width=80, height=35)

#==========================frame6_closed==========================


#=================frame7 content==================================
label_color = Label(frame7, text="This collection consit of all the available",
font="times 13",bg='cadetblue').place(x=32, y=3, width=280, height=30)
label_color2 = Label(frame7, text="and recogniced colors in tkinter and python",
font='times 13',bg='cadetblue').place(x=315, y=3, width=300, height=30)

control1 = Button(frame7, text= '>',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame8))
control1.place(x=625, y=3, width=30, height=30)

control2 = Button(frame7, text= '<',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame6))
control2.place(x=2, y=3, width=30, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('gold2')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('gold3')

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('gold4')

lb1 = Button(frame7, bd=0, text ='Gold2',
 font='times 12 bold', fg='black', bg='gold2', command= copy_button_maxy1)
lb1.place(x=2, y=37, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Gold3', 
font='times 12 bold', fg='black', bg='gold3', command=copy_button_maxy2)
lb2.place(x=84, y=37, width=80, height=35)

lb3 = Button(frame7, bd=0, text = 'Gold4',
 font='times 12 bold',  fg='black', bg='gold4',command=copy_button_maxy3)
lb3.place(x=166, y=37, width=80, height=35)

def copy_button_maxy4():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('goldenrod1')  

def copy_button_maxy5():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('goldenrod2')

def copy_button_maxy6():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('goldenrod3')

lb1 = Button(frame7, bd=0, text = 'Golden\nrod1',
 font='times 12 bold', fg='black', bg='goldenrod1', command= copy_button_maxy4)
lb1.place(x=248, y=37, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Golden\nrod2', 
font='times 12 bold', fg='black', bg='goldenrod2', command=copy_button_maxy5)
lb2.place(x=330, y=37, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Golden\nrod3',
 font='times 12 bold',  fg='black', bg='goldenrod3',command=copy_button_maxy6)
lb3.place(x=412, y=37, width=80, height=35)


def copy_button_maxy7():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('goldenrod4')

def copy_button_maxy8():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkGoldenrod1')

lb1 = Button(frame7, bd=0, text = 'Goldenrod4',
 font='times 12 bold', fg='black', bg='goldenrod4', command= copy_button_maxy7)
lb1.place(x=494, y=37, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Dark\nGoldenrod1',font='times 12 bold',
             fg='black', bg='DarkGoldenrod1', command=copy_button_maxy8)
lb2.place(x=576, y=37, width=80, height=35)

#=====================row2_frame7=================================
def copy_button_maxy9():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkGoldenrod2')  

def copy_button_maxy10():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkGoldenrod3')

def copy_button_maxy11():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkGoldenrod4')

lb1 = Button(frame7, bd=0, text = 'Dark\nGoldenrod2',
 font='times 12 bold', fg='black', bg='DarkGoldenrod2', command= copy_button_maxy9)
lb1.place(x=2, y=74, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Dark\nGoldenrod3', 
font='times 12 bold', fg='black', bg='DarkGoldenrod3', command=copy_button_maxy10)
lb2.place(x=84, y=74, width=80, height=35)

lb3 = Button(frame7, bd=0, text = 'Dark\nGoldenrod4',
 font='times 12 bold',  fg='black', bg='DarkGoldenrod4',command=copy_button_maxy11)
lb3.place(x=166, y=74, width=80, height=35)

def copy_button_maxy12():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RosyBrown1')  

def copy_button_maxy13():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RosyBrown2')

def copy_button_maxy14():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RosyBrown3')

lb1 = Button(frame7, bd=0, text ='Rosy\nBrown1',
 font='times 12 bold', fg='black', bg='RosyBrown1', command= copy_button_maxy12)
lb1.place(x=248, y=74, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Rosy\nBrown2', 
font='times 12 bold', fg='black', bg='RosyBrown2', command=copy_button_maxy13)
lb2.place(x=330, y=74, width=80, height=35)

lb3 = Button(frame7, bd=0, text = 'Rosy\nBrown3',
 font='times 12 bold',  fg='black', bg='RosyBrown3',command=copy_button_maxy14)
lb3.place(x=412, y=74, width=80, height=35)


def copy_button_maxy15():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('RosyBrown4')

def copy_button_maxy16():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('IndianRed1')

lb1 = Button(frame7, bd=0, text = 'Rosy\nBrown4',
 font='times 12 bold', fg='black', bg='RosyBrown4', command= copy_button_maxy15)
lb1.place(x=494, y=74, width=80, height=35)

lb2 = Button(frame7, bd=0, text='Indian\nRed1',font='times 12 bold',
             fg='black', bg='IndianRed1', command=copy_button_maxy16)
lb2.place(x=576, y=74, width=80, height=35)

#==================row3_frame7=====================================
def copy_button_maxy17():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('IndianRed2')  

def copy_button_maxy18():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('IndianRed3')

def copy_button_maxy19():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('IndianRed4')

lb1 = Button(frame7, bd=0, text = 'Indian\nRed2',
 font='times 12 bold', fg='black', bg='IndianRed2', command= copy_button_maxy17)
lb1.place(x=2, y=111, width=80, height=35)

lb2 = Button(frame7, bd=0, text ='Indian\nRed3', 
font='times 12 bold', fg='black', bg='IndianRed3', command=copy_button_maxy18)
lb2.place(x=84, y=111, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Indian\nRed4',
 font='times 12 bold',  fg='black', bg='IndianRed4',command=copy_button_maxy19)
lb3.place(x=166, y=111, width=80, height=35)

def copy_button_maxy20():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('sienna1')  

def copy_button_maxy21():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('sienna2')

def copy_button_maxy22():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('sienna3')

lb1 = Button(frame7, bd=0, text = 'Sienna1',
 font='times 12 bold', fg='black', bg='sienna1', command= copy_button_maxy20)
lb1.place(x=248, y=111, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Sienna2', 
font='times 12 bold', fg='black', bg='sienna2', command=copy_button_maxy21)
lb2.place(x=330, y=111, width=80, height=35)

lb3 = Button(frame7, bd=0, text = 'Sienna3',
 font='times 12 bold',  fg='black', bg='sienna3',command=copy_button_maxy22)
lb3.place(x=412, y=111, width=80, height=35)


def copy_button_maxy23():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('sienna4')

def copy_button_maxy24():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('burlywood1')

lb1 = Button(frame7, bd=0, text ='Sienna4',
 font='times 12 bold', fg='black', bg='sienna4', command= copy_button_maxy23)
lb1.place(x=494, y=111, width=80, height=35)

lb2 = Button(frame7, bd=0, text='Burlywood1',font='times 12 bold',
             fg='black', bg='burlywood1', command=copy_button_maxy24)
lb2.place(x=576, y=111, width=80, height=35)


#=============================row4_frame7==========================
def copy_button_maxy25():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('burlywood2')  

def copy_button_maxy26():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('burlywood3')

def copy_button_maxy27():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('burlywood4')

lb1 = Button(frame7, bd=0, text = 'Burlywood2',
 font='times 12 bold', fg='black', bg='burlywood2', command= copy_button_maxy25)
lb1.place(x=2, y=148, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'burlywood3', 
font='times 12 bold', fg='black', bg='burlywood3', command=copy_button_maxy26)
lb2.place(x=84, y=148, width=80, height=35)

lb3 = Button(frame7, bd=0, text = 'burlywood4',
 font='times 12 bold',  fg='black', bg='burlywood4',command=copy_button_maxy27)
lb3.place(x=166, y=148, width=80, height=35)

def copy_button_maxy28():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('wheat1')  

def copy_button_maxy29():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('wheat2')

def copy_button_maxy30():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('wheat3')

lb1 = Button(frame7, bd=0, text = 'Wheat1',
 font='times 12 bold', fg='black', bg='wheat1', command= copy_button_maxy28)
lb1.place(x=248, y=148, width=80, height=35)

lb2 = Button(frame7, bd=0, text ='Wheat2', 
font='times 12 bold', fg='black', bg='wheat2', command=copy_button_maxy29)
lb2.place(x=330, y=148, width=80, height=35)

lb3 = Button(frame7, bd=0, text = 'Wheat3',
 font='times 12 bold',  fg='black', bg='wheat3',command=copy_button_maxy30)
lb3.place(x=412, y=148, width=80, height=35)


def copy_button_maxy31():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('wheat4')

def copy_button_maxy32():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tan1')

lb1 = Button(frame7, bd=0, text ='Wheat4',
 font='times 12 bold', fg='black', bg='wheat4', command= copy_button_maxy31)
lb1.place(x=494, y=148, width=80, height=35)

lb2 = Button(frame7, bd=0, text='tan1',font='times 12 bold',
             fg='black', bg='tan1', command=copy_button_maxy32)
lb2.place(x=576, y=148, width=80, height=35)


#=================row5_frame7=====================================
def copy_button_maxy33():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tan2')  

def copy_button_maxy34():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tan3')

def copy_button_maxy35():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('chocolate1')

lb1 = Button(frame7, bd=0, text ='Tan2',
 font='times 12 bold', fg='black', bg='tan2', command= copy_button_maxy33)
lb1.place(x=2, y=185, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Tan3', 
font='times 12 bold', fg='black', bg='tan3', command=copy_button_maxy34)
lb2.place(x=84, y=185, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Chocolate1',
 font='times 12 bold',  fg='black', bg='chocolate1',command=copy_button_maxy35)
lb3.place(x=166, y=185, width=80, height=35)

def copy_button_maxy36():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('chocolate2')  

def copy_button_maxy37():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('chocolate3')

def copy_button_maxy38():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('firebrick1')

lb1 = Button(frame7, bd=0, text ='Chocolate2',
 font='times 12 bold', fg='black', bg='chocolate2', command= copy_button_maxy36)
lb1.place(x=248, y=185, width=80, height=35)

lb2 = Button(frame7, bd=0, text ='Chocolate3', 
font='times 12 bold', fg='black', bg='chocolate3', command=copy_button_maxy37)
lb2.place(x=330, y=185, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Firebrick1',
 font='times 12 bold',  fg='black', bg='firebrick1',command=copy_button_maxy38)
lb3.place(x=412, y=185, width=80, height=35)


def copy_button_maxy39():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('firebrick2')

def copy_button_maxy40():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('firebrick3')

lb1 = Button(frame7, bd=0, text ='Firebrick2',font='times 12 bold',
             fg='black', bg='firebrick2', command= copy_button_maxy39)
lb1.place(x=494, y=185, width=80, height=35)

lb2 = Button(frame7, bd=0, text='Firebrick3',font='times 12 bold',
             fg='black', bg='firebrick3', command=copy_button_maxy40)
lb2.place(x=576, y=185, width=80, height=35)


#=================row6_frame7=====================================
def copy_button_maxy41():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('firebrick4')  

def copy_button_maxy42():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('brown1')

def copy_button_maxy43():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('brown2')

lb1 = Button(frame7, bd=0, text ='Firebrick4',
 font='times 12 bold', fg='black', bg='firebrick4', command= copy_button_maxy41)
lb1.place(x=2, y=222, width=80, height=35)

lb2 = Button(frame7, bd=0, text ='Brown1', 
font='times 12 bold', fg='black', bg='brown1', command=copy_button_maxy42)
lb2.place(x=84, y=222, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Brown2',
 font='times 12 bold',  fg='black', bg='brown2',command=copy_button_maxy43)
lb3.place(x=166, y=222, width=80, height=35)

def copy_button_maxy44():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('brown3')  

def copy_button_maxy45():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('brown4')

def copy_button_maxy46():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('salmon1')

lb1 = Button(frame7, bd=0, text = 'Brown3',
 font='times 12 bold', fg='black', bg='brown3', command= copy_button_maxy44)
lb1.place(x=248, y=222, width=80, height=35)

lb2 = Button(frame7, bd=0, text ='Brown4', 
font='times 12 bold', fg='black', bg='brown4', command=copy_button_maxy45)
lb2.place(x=330, y=222, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Salmon1',
 font='times 12 bold',  fg='black', bg='salmon1',command=copy_button_maxy46)
lb3.place(x=412, y=222, width=80, height=35)


def copy_button_maxy47():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('salmon2')

def copy_button_maxy48():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('salmon3')

lb1 = Button(frame7, bd=0, text = 'Salmon2',font='times 12 bold',
             fg='black', bg='salmon2', command= copy_button_maxy47)
lb1.place(x=494, y=222, width=80, height=35)

lb2 = Button(frame7, bd=0, text='Salmon3',font='times 12 bold',
             fg='black', bg='salmon3', command=copy_button_maxy48)
lb2.place(x=576, y=222, width=80, height=35)

#=================row7_frame7=====================================
def copy_button_maxy49():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('salmon4')  

def copy_button_maxy50():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSalmon2')

def copy_button_maxy51():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSalmon3')

lb1 = Button(frame7, bd=0, text = 'Salmon4',
 font='times 12 bold', fg='black', bg='salmon4', command= copy_button_maxy49)
lb1.place(x=2, y=259, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Light\nSalmon2', 
font='times 12 bold', fg='black', bg='LightSalmon2', command=copy_button_maxy50)
lb2.place(x=84, y=259, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='LightSalmon3',
 font='times 12 bold',  fg='black', bg='LightSalmon3',command=copy_button_maxy51)
lb3.place(x=166, y=259, width=80, height=35)

def copy_button_maxy52():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightSalmon4')  

def copy_button_maxy53():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orange2')

def copy_button_maxy54():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orange3')

lb1 = Button(frame7, bd=0, text ='Light\nSalmon4',
 font='times 12 bold', fg='black', bg='LightSalmon4', command= copy_button_maxy54)
lb1.place(x=248, y=259, width=80, height=35)

lb2 = Button(frame7, bd=0, text ='Orange2', 
font='times 12 bold', fg='black', bg='orange2', command=copy_button_maxy53)
lb2.place(x=330, y=259, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='Orange3',
 font='times 12 bold',  fg='black', bg='orange3',command=copy_button_maxy54)
lb3.place(x=412, y=259, width=80, height=35)


def copy_button_maxy55():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orange4')

def copy_button_maxy56():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrange1')

lb1 = Button(frame7, bd=0, text ='Orange4',font='times 12 bold',
             fg='black', bg='orange4', command= copy_button_maxy55)
lb1.place(x=494, y=259, width=80, height=35)

lb2 = Button(frame7, bd=0, text='Dark\nOrange1',font='times 12 bold',
             fg='black', bg='DarkOrange1', command=copy_button_maxy56)
lb2.place(x=576, y=259, width=80, height=35)


#=================row8_frame7=====================================
def copy_button_maxy57():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrange2')  

def copy_button_maxy58():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrange3')

def copy_button_maxy59():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrange4')

lb1 = Button(frame7, bd=0, text ='Dark\nOrange2',
 font='times 12 bold', fg='black', bg='DarkOrange2', command= copy_button_maxy57)
lb1.place(x=2, y=296, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'DarkOrange3', 
font='times 12 bold', fg='black', bg='DarkOrange3', command=copy_button_maxy58)
lb2.place(x=84, y=296, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='DarkOrange4',
 font='times 12 bold',  fg='black', bg='DarkOrange4',command=copy_button_maxy59)
lb3.place(x=166, y=296, width=80, height=35)

def copy_button_maxy60():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('coral1')  

def copy_button_maxy61():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('coral2')

def copy_button_maxy62():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('coral3')

lb1 = Button(frame7, bd=0, text ='Coral1',
 font='times 12 bold', fg='black', bg='coral1', command= copy_button_maxy60)
lb1.place(x=248, y=296, width=80, height=35)

lb2 = Button(frame7, bd=0, text = 'Coral2', 
font='times 12 bold', fg='black', bg='coral2', command=copy_button_maxy61)
lb2.place(x=330, y=296, width=80, height=35)

lb3 = Button(frame7, bd=0, text ='coral3',
 font='times 12 bold',  fg='black', bg='coral3',command=copy_button_maxy62)
lb3.place(x=412, y=296, width=80, height=35)


def copy_button_maxy63():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('coral4')

def copy_button_maxy64():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tomato2')

lb1 = Button(frame7, bd=0, text ='Coral4',font='times 12 bold',
             fg='black', bg='coral4', command= copy_button_maxy63)
lb1.place(x=494, y=296, width=80, height=35)

lb2 = Button(frame7, bd=0, text='Tomato2',font='times 12 bold',
             fg='black', bg='tomato2', command=copy_button_maxy64)
lb2.place(x=576, y=296, width=80, height=35)

#=================================frame7_closed===============================


#=================frame8 content==============================================
label_color = Label(frame8, text="This collection consit of all the available",
font="times 13",bg='cadetblue').place(x=57, y=3, width=280, height=30)
label_color2 = Label(frame8, text="and recogniced colors in tkinter and python",
font='times 13',bg='cadetblue').place(x=340, y=3, width=300, height=30)

control2 = Button(frame8, text= '<',bg='cadetblue', font='verdana 16 bold',
                  command= lambda: new_frame(frame7))
control2.place(x=2, y=3, width=30, height=30)


def copy_button_maxy1():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tomato3')  

def copy_button_maxy2():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('tomato4')

def copy_button_maxy3():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('OrangeRed2')

lb1 = Button(frame8, bd=0, text = 'Tomato3',
 font='times 12 bold', fg='black', bg='tomato3', command= copy_button_maxy1)
lb1.place(x=2, y=37, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Tomato4',font='times 12 bold',
             fg='black', bg='tomato4', command=copy_button_maxy2)
lb2.place(x=84, y=37, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Orange\nRed2',
 font='times 12 bold',  fg='black', bg='OrangeRed2',command=copy_button_maxy3)
lb3.place(x=166, y=37, width=80, height=35)

def copy_button_maxy4():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('OrangeRed3')  

def copy_button_maxy5():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('OrangeRed4')

def copy_button_maxy6():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('red2')

lb1 = Button(frame8, bd=0, text ='Orange\nRed3',
 font='times 12 bold', fg='black', bg='OrangeRed3', command= copy_button_maxy4)
lb1.place(x=248, y=37, width=80, height=35)

lb2 = Button(frame8, bd=0, text = 'Orange\nRed4', 
font='times 12 bold', fg='black', bg='OrangeRed4', command=copy_button_maxy5)
lb2.place(x=330, y=37, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Red2',
 font='times 12 bold',  fg='black', bg='red2',command=copy_button_maxy6)
lb3.place(x=412, y=37, width=80, height=35)


def copy_button_maxy7():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('red3')

def copy_button_maxy8():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('red4')

lb1 = Button(frame8, bd=0, text = 'Red3',
 font='times 12 bold', fg='black', bg='red3', command= copy_button_maxy7)
lb1.place(x=494, y=37, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='red4',font='times 12 bold',
             fg='black', bg='red4', command=copy_button_maxy8)
lb2.place(x=576, y=37, width=80, height=35)

#=====================row2_frame3=================================
def copy_button_maxy9():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DeepPink2')  

def copy_button_maxy10():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DeepPink3')

def copy_button_maxy11():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DeepPink4')

lb1 = Button(frame8, bd=0, text ='Deep\nPink2',
 font='times 12 bold', fg='black', bg='DeepPink2', command= copy_button_maxy9)
lb1.place(x=2, y=74, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Deep\nPink3', 
font='times 12 bold', fg='black', bg='DeepPink3', command=copy_button_maxy10)
lb2.place(x=84, y=74, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Deep\nPink4',
 font='times 12 bold',  fg='black', bg='DeepPink4',command=copy_button_maxy11)
lb3.place(x=166, y=74, width=80, height=35)

def copy_button_maxy12():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('HotPink1')  

def copy_button_maxy13():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('HotPink2')

def copy_button_maxy14():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('HotPink3')

lb1 = Button(frame8, bd=0, text = 'Hot\nPink1',
 font='times 12 bold', fg='black', bg='HotPink1', command= copy_button_maxy12)
lb1.place(x=248, y=74, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Hot\nPink2', 
font='times 12 bold', fg='black', bg='HotPink2', command=copy_button_maxy13)
lb2.place(x=330, y=74, width=80, height=35)

lb3 = Button(frame8, bd=0, text = 'Hot\nPink3',
 font='times 12 bold',  fg='black', bg='HotPink3',command=copy_button_maxy14)
lb3.place(x=412, y=74, width=80, height=35)


def copy_button_maxy15():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('HotPink4')

def copy_button_maxy16():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('pink1')

lb1 = Button(frame8, bd=0, text ='Hot\nPink4',
 font='times 12 bold', fg='black', bg='HotPink4', command= copy_button_maxy15)
lb1.place(x=494, y=74, width=80, height=35)

lb2 = Button(frame8, bd=0, text='Pink1',font='times 12 bold',
             fg='black', bg='pink1', command=copy_button_maxy16)
lb2.place(x=576, y=74, width=80, height=35)

#==================row3_frame8=====================================
def copy_button_maxy17():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'pink2')  

def copy_button_maxy18():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('pink3')

def copy_button_maxy19():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('pink4')

lb1 = Button(frame8, bd=0, text = 'Pink2',
 font='times 12 bold', fg='black', bg='pink2', command= copy_button_maxy17)
lb1.place(x=2, y=111, width=80, height=35)

lb2 = Button(frame8, bd=0, text = 'pink3', 
font='times 12 bold', fg='black', bg='pink3', command=copy_button_maxy18)
lb2.place(x=84, y=111, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='pink4',
 font='times 12 bold',  fg='black', bg='pink4',command=copy_button_maxy19)
lb3.place(x=166, y=111, width=80, height=35)

def copy_button_maxy20():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightPink1')  

def copy_button_maxy21():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightPink2')

def copy_button_maxy22():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightPink3')

lb1 = Button(frame8, bd=0, text ='Light\nPink1',
 font='times 12 bold', fg='black', bg='LightPink1', command= copy_button_maxy20)
lb1.place(x=248, y=111, width=80, height=35)

lb2 = Button(frame8, bd=0, text = 'Light\nPink2', 
font='times 12 bold', fg='black', bg='LightPink2', command=copy_button_maxy21)
lb2.place(x=330, y=111, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Light\nPink3',
 font='times 12 bold',  fg='black', bg='LightPink3',command=copy_button_maxy22)
lb3.place(x=412, y=111, width=80, height=35)


def copy_button_maxy23():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('LightPink4')

def copy_button_maxy24():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleVioletRed1')

lb1 = Button(frame8, bd=0, text = 'Light\nPink4',
 font='times 12 bold', fg='black', bg='LightPink4', command= copy_button_maxy23)
lb1.place(x=494, y=111, width=80, height=35)

lb2 = Button(frame8, bd=0, text='Pale\nVioletRed1',font='times 12 bold',
             fg='black', bg='PaleVioletRed1', command=copy_button_maxy24)
lb2.place(x=576, y=111, width=80, height=35)


#=============================row4_frame8==========================
def copy_button_maxy25():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleVioletRed2')  

def copy_button_maxy26():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleVioletRed3')

def copy_button_maxy27():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('PaleVioletRed4')

lb1 = Button(frame8, bd=0, text ='Pale\nVioletRed2',
 font='times 12 bold', fg='black', bg='PaleVioletRed2', command= copy_button_maxy25)
lb1.place(x=2, y=148, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Pale\nVioletRed3', 
font='times 12 bold', fg='black', bg='PaleVioletRed3', command=copy_button_maxy26)
lb2.place(x=84, y=148, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Pale\nVioletRed4',
 font='times 12 bold',  fg='black', bg='PaleVioletRed4',command=copy_button_maxy27)
lb3.place(x=166, y=148, width=80, height=35)

def copy_button_maxy28():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('maroon1')  

def copy_button_maxy29():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('maroon2')

def copy_button_maxy30():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('maroon3')

lb1 = Button(frame8, bd=0, text = 'Maroon1',
 font='times 12 bold', fg='black', bg='maroon1', command= copy_button_maxy28)
lb1.place(x=248, y=148, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Maroon2', 
font='times 12 bold', fg='black', bg='maroon2', command=copy_button_maxy29)
lb2.place(x=330, y=148, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Maroon3',
 font='times 12 bold',  fg='black', bg='maroon3',command=copy_button_maxy30)
lb3.place(x=412, y=148, width=80, height=35)


def copy_button_maxy31():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('maroon4')

def copy_button_maxy32():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'VioletRed1')

lb1 = Button(frame8, bd=0, text = 'Maroon4',
 font='times 12 bold', fg='black', bg='maroon4', command= copy_button_maxy31)
lb1.place(x=494, y=148, width=80, height=35)

lb2 = Button(frame8, bd=0, text= 'Violet\nRed1',font='times 12 bold',
             fg='black', bg= 'VioletRed1', command=copy_button_maxy32)
lb2.place(x=576, y=148, width=80, height=35)


#=================row5_frame8=====================================
def copy_button_maxy33():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('VioletRed2')  

def copy_button_maxy34():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('VioletRed3')

def copy_button_maxy35():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('VioletRed4')

lb1 = Button(frame8, bd=0, text = 'VioletRed2',
 font='times 12 bold', fg='black', bg='VioletRed2', command= copy_button_maxy33)
lb1.place(x=2, y=185, width=80, height=35)

lb2 = Button(frame8, bd=0, text = 'VioletRed3',font='times 12 bold',
             fg='black', bg='VioletRed3', command=copy_button_maxy34)
lb2.place(x=84, y=185, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='VioletRed4',
 font='times 12 bold',  fg='black', bg='VioletRed4',command=copy_button_maxy35)
lb3.place(x=166, y=185, width=80, height=35)

def copy_button_maxy36():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('magenta2')  

def copy_button_maxy37():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('magenta3')

def copy_button_maxy38():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('magenta4')

lb1 = Button(frame8, bd=0, text = 'Magenta2',
 font='times 12 bold', fg='black', bg='magenta2', command= copy_button_maxy36)
lb1.place(x=248, y=185, width=80, height=35)

lb2 = Button(frame8, bd=0, text = 'Magenta3', 
font='times 12 bold', fg='black', bg='magenta3', command=copy_button_maxy37)
lb2.place(x=330, y=185, width=80, height=35)

lb3 = Button(frame8, bd=0, text = 'Magenta4',
 font='times 12 bold',  fg='black', bg='magenta4',command=copy_button_maxy38)
lb3.place(x=412, y=185, width=80, height=35)


def copy_button_maxy39():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orchid1')

def copy_button_maxy40():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orchid1')

lb1 = Button(frame8, bd=0, text ='Orchid1',font='times 12 bold',
             fg='black', bg='orchid1', command= copy_button_maxy39)
lb1.place(x=494, y=185, width=80, height=35)

lb2 = Button(frame8, bd=0, text='Orchid2',font='times 12 bold',
             fg='black', bg='orchid2', command=copy_button_maxy40)
lb2.place(x=576, y=185, width=80, height=35)


#=================row6_frame8=====================================
def copy_button_maxy41():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orchid3')  

def copy_button_maxy42():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('orchid4')

def copy_button_maxy43():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('Plum1')

lb1 = Button(frame8, bd=0, text = 'Orchid3',
 font='times 12 bold', fg='black', bg='orchid4', command= copy_button_maxy41)
lb1.place(x=2, y=222, width=80, height=35)

lb2 = Button(frame8, bd=0, text = 'Orchid4', 
font='times 12 bold', fg='black', bg='orchid4', command=copy_button_maxy42)
lb2.place(x=84, y=222, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Plum1',
 font='times 12 bold',  fg='black', bg='plum1',command=copy_button_maxy43)
lb3.place(x=166, y=222, width=80, height=35)

def copy_button_maxy44():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('plum2')  

def copy_button_maxy45():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('plum3')

def copy_button_maxy46():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('plum4')

lb1 = Button(frame8, bd=0, text = 'Plum2',
 font='times 12 bold', fg='black', bg='plum2', command= copy_button_maxy44)
lb1.place(x=248, y=222, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Plum3', 
font='times 12 bold', fg='black', bg='plum3', command=copy_button_maxy45)
lb2.place(x=330, y=222, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Plum4',
 font='times 12 bold',  fg='black', bg='plum4',command=copy_button_maxy46)
lb3.place(x=412, y=222, width=80, height=35)


def copy_button_maxy47():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumOrchid1')

def copy_button_maxy48():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumOrchid2')

lb1 = Button(frame8, bd=0, text ='Medium\nOrchid1',font='times 12 bold',
             fg='black', bg='MediumOrchid1', command= copy_button_maxy47)
lb1.place(x=494, y=222, width=80, height=35)

lb2 = Button(frame8, bd=0, text='Medium\nOrchid2',font='times 12 bold',
             fg='black', bg='MediumOrchid2', command=copy_button_maxy48)
lb2.place(x=576, y=222, width=80, height=35)

#=================row7_frame8=====================================
def copy_button_maxy49():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumOrchid3')  

def copy_button_maxy50():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumOrchid4')

def copy_button_maxy51():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrchid1')

lb1 = Button(frame8, bd=0, text ='Medium\nOrchid3',
 font='times 12 bold', fg='black', bg='MediumOrchid3', command= copy_button_maxy49)
lb1.place(x=2, y=259, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Medium\nOrchid4',font='times 12 bold',
             fg='black', bg='MediumOrchid4', command=copy_button_maxy50)
lb2.place(x=84, y=259, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Dark\nOrchid1',
 font='times 12 bold',  fg='black', bg='DarkOrchid1',command=copy_button_maxy51)
lb3.place(x=166, y=259, width=80, height=35)

def copy_button_maxy52():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrchid2')  

def copy_button_maxy53():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrchid3')

def copy_button_maxy54():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('DarkOrchid4')

lb1 = Button(frame8, bd=0, text ='Dark\nOrchid2',
 font='times 12 bold', fg='black', bg='DarkOrchid2', command= copy_button_maxy52)
lb1.place(x=248, y=259, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Dark\nOrchid3',font='times 12 bold',
             fg='black', bg='DarkOrchid3',command= copy_button_maxy53)
lb2.place(x=330, y=259, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Dark\nOrchid4',
 font='times 12 bold',  fg='black', bg='DarkOrchid4',command=copy_button_maxy54)
lb3.place(x=412, y=259, width=80, height=35)


def copy_button_maxy55():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'purple1')

def copy_button_maxy56():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('purple2')

lb1 = Button(frame8, bd=0, text ='Purple1',font='times 12 bold',
             fg='black', bg='purple1', command= copy_button_maxy55)
lb1.place(x=494, y=259, width=80, height=35)

lb2 = Button(frame8, bd=0, text='Purple2',font='times 12 bold',
             fg='black', bg='purple2', command=copy_button_maxy56)
lb2.place(x=576, y=259, width=80, height=35)


#=================row8_frame8=====================================
def copy_button_maxy57():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append( 'purple3')  

def copy_button_maxy58():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('purple4')

def copy_button_maxy59():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumPurple1')

lb1 = Button(frame8, bd=0, text ='Purple3',
 font='times 12 bold', fg='black', bg='purple3', command= copy_button_maxy57)
lb1.place(x=2, y=296, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Purple4', 
font='times 12 bold', fg='black', bg='purple4', command=copy_button_maxy58)
lb2.place(x=84, y=296, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Medium\nPurple1',
 font='times 12 bold',  fg='black', bg='MediumPurple1',command=copy_button_maxy59)
lb3.place(x=166, y=296, width=80, height=35)

def copy_button_maxy60():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumPurple2')  

def copy_button_maxy61():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumPurple3')

def copy_button_maxy62():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('MediumPurple4')

lb1 = Button(frame8, bd=0, text ='Medium\nPurple2',
 font='times 12 bold', fg='black', bg='MediumPurple2', command= copy_button_maxy60)
lb1.place(x=248, y=296, width=80, height=35)

lb2 = Button(frame8, bd=0, text ='Medium\nPurple3', 
font='times 12 bold', fg='black', bg='MediumPurple3', command=copy_button_maxy61)
lb2.place(x=330, y=296, width=80, height=35)

lb3 = Button(frame8, bd=0, text ='Medium\nPurple4',
 font='times 12 bold',  fg='black', bg='MediumPurple4',command=copy_button_maxy62)
lb3.place(x=412, y=296, width=80, height=35)


def copy_button_maxy63():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('thistle1')

def copy_button_maxy64():
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append('thistle2')

lb1 = Button(frame8, bd=0, text ='Thistle1',font='times 12 bold',
             fg='black', bg='thistle1', command= copy_button_maxy63)
lb1.place(x=494, y=296, width=80, height=35)

lb2 = Button(frame8, bd=0, text='Thistle2',font='times 12 bold',
             fg='black', bg='thistle2', command=copy_button_maxy64)
lb2.place(x=576, y=296, width=80, height=35)

#==========================frame8_closed==========================

#=============create side menu bar widget==========================
# =============================close button================================
font_frame2 = Frame(font_frame)
font_frame2.place(x=0,y=0, width=660, height=151)

def my_func():
        maxy(root)
        
closebutton = Button(font_frame2, text='Home', fg= 'black', bg='orange',
 font='times 10', command= my_func)
closebutton.place(x=0, y=0, width=50, height=20)

#=========================close button #closed#========================


def explore(ex_raise):
    ex_raise.tkraise()

explore_frame1 = Frame()
exp1 = Frame()


for m1 in (explore_frame1, exp1):
    m1.place(x=0, y=0, width=80, height=110)

#===============================
def my_func22():
    maxy(font_frame)

new_canvas = Canvas(explore_frame1)
new_canvas.place(x=0, y=0, height=110, width=100)

#new_canvas.create_circle(50, 60, 150, 50, fill="#476042")
new_canvas.create_rectangle(10, 38, 70, 70, fill="cadetblue")
new_canvas.create_line(35,38, 20, 15, fill="black", width=3)
new_canvas.create_line(40, 38, 61, 10, fill="black", width=3)
new_canvas.create_line(35,70, 20, 95, fill="black", width=3)
new_canvas.create_line(40, 70, 59, 95, fill="black", width=3)

#=======================closed============================================

3#=================About-page for font_frame=======================================
def opm():
    maxy(font_frame)
    maxy(font_frame2)

about_frame2 = Frame()
about_frame2.place(x=0,y=0,width=660, height=485)

closebutton = Button(new_canvas, text='About', fg= 'black',
 bg='powderblue',bd= 0, font='times 12 bold', command= lambda: maxy(about_frame2))
closebutton.place(x=10, y=38, width=60, height=32)


back_button_about = Button(about_frame2, text='<Back',  command= opm)
back_button_about.place(x=3, y=460, width=40, height=20)

text_about= Label(about_frame2, text='Togit is a GUI application that helps programmers access all supported colors and fonts',
                   font='times 12')
text_about.place(x=10, y=47, width=530, height=30)

tx = Label(about_frame2, text='in python and other major languegues, also it helps you out with spelling and typing,',
           font='times 12')
tx.place(x=2, y=71, width=510, height=30)

tx = Label(about_frame2, text='therefore it copies the colors or font name to clickboard once clicked, and all the pro-',
           font='times 12')  
tx.place(x=5, y=95, width=518, height=30)

tx = Label(about_frame2, text='grammer or user needs to do is just paste the element where he needs to use it.',
           font='times 12')
tx.place(x=1, y=119, width=485, height=30)


text_about3 = Label(about_frame2,  text='What is Togit?', font='times 16')
text_about3.place(x=5, y=2, width=129, height=30)

text_about2 = Label(about_frame2,  text='Why Togit?', font='times 16')
text_about2.place(x=5, y=164, width=120, height=30)



tx = Label(about_frame2, text='1. It helps you to make the right color choice when designing a UI of an app or website.',
           font='times 12')
tx.place(x=2, y=209, width=530, height=30)

tx = Label(about_frame2, text='2. The click-and-copy feature helps save you time and energy.',
           font='times 12')
tx.place(x=5, y=233, width=375, height=30)


#========================Build with love===================================
bwl_frame = Frame(about_frame2)
bwl_frame.place(x=440, y=410, width=213, height=70)
bwl_frame.configure(background='white')

labi = Label(bwl_frame, text="Made with", fg="gray", bg="white", font="times 9")
labi.place(x=0, y=10, width=60, height=15)

labi2 = Label(bwl_frame, text="by GetbusyHub", fg="gray", bg="white", font="times 9")
labi2.place(x=114, y=10, width=80, height=15)

labi3 = Label(bwl_frame, text="Founder:", fg="gray", bg="white", font="times 9 bold")
labi3.place(x=0, y=34, width=53, height=15)

labi3 = Label(bwl_frame, text="Okonkwo Success E.", fg="gray", bg="white", font="times 9")
labi3.place(x=53, y=34, width=110, height=15)

labi4 = Label(bwl_frame, text="Website :", fg="gray", bg="white", font="times 9 bold")
labi4.place(x=0, y=53, width=52, height=15)

labi4 = Label(bwl_frame, text="www.getbusyhub.com", fg="gray", bg="white", font="times 9")
labi4.place(x=59, y=53, width=111, height=15)


loveimage = PhotoImage(file="C:\\Users\\SUCCESS\\Desktop\\New folder\\imagees.png")
love2 = Label(bwl_frame, image=loveimage)
love2.place(x=62, y=0, width=50, height=30)

#===============================About, closed==============================

def ctr(cost):
    cost.tkraise()

def gold():
    ctr(root2)
    ctr(frame11)
def andy():
    ctr(root2)
    ctr(font_frame)
    
optionbutton1 = Button(font_frame2, text='Explore',fg= 'black', bg='orange', 
 font='times 10', command= lambda: explore(explore_frame1))
optionbutton1.place(x=0, y=26, width=50, height=20)

colorbutton1 = Button(explore_frame1, text='Colors',
 font='times 10 bold', bg='powderblue', bd=1, command= gold)
colorbutton1.place(x=15, y=2, width=50, height=15)

colorbutton11 = Button(explore_frame1, text='Fonts',
                      font='times 10 bold', bg='powderblue', bd=1,
                      command= andy)
colorbutton11.place(x=15, y=93, width=50, height=15)

label1 = Label(font_frame2,  text='Welcome User,',
               font='times 14')
label1.place(x=150, y=0, width=250, height=30)

label2 = Label(font_frame2,  text='Togit', fg='blue4',
               font='times 14 bold')
label2.place(x=334, y=0, width=45, height=30)

label2 = Label(font_frame2,  text='got your back!',
               font='times 14')
label2.place(x=380, y=0, width=125, height=30)


label1 = Label(font_frame2,  text='''kindly click any of the button with the preferred FONT you like,
the Name will be copied to clickboard and you
can paste it where ever u wanna use it.''',
               font='times 12 ')
label1.place(x=100, y=26, width=500, height=80)

button3 = Button(font_frame2, text='All Fonts', fg= 'black', bg='cadetblue',
 font='times 12')
button3.place(x=255, y=112, width=150, height=40)

arc =Label(font_frame, text='<<NIL>>', font="verdana 14 bold",
           fg='orange',bg='cadetblue')
arc.place(x=215, y=180, width=210, height=40)

arc1 =Label(font_frame, text='    Build in progress..{check back later}',font="times 10",
           fg='yellow',bg='cadetblue')
arc1.place(x=209, y=210, width=210, height=25)

#=============create side menu bar widget #closed#=======================

maxy(root)
maxy2(frame11)
window.mainloop()
