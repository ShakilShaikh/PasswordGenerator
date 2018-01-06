# In the name of Allah


from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import ttk
import tkMessageBox
import threading
import datetime
import sys,os,subprocess,time,random


alp=['a','c','b','e','d','g','f',
     'i','h','k','j','m','l','o',
     'n','q','p','r','u','t','w',
     'v','y','x','z']

# ========= Tkniter ==============
root = Tk()
root.title('PassWord Generator')


style = ttk.Style()
style.theme_use('winnative')


def gen():
    a=Memo.a
    n=Memo.n
    nu=Memo.nu
    a=random.choice(a)
    random.shuffle(n)
    b=random.choice(n)
    random.shuffle(nu)
    c=random.choice(nu)
    random.shuffle(alp)
    d=a+b+c+random.choice(alp)+random.choice(alp)
    entry2.delete(0,END)
    entry2.insert(0,d)
    



label2 = ttk.Label(root, text='Key : ')
label2.grid(row=0, column=0)
entry2 = ttk.Entry(root, width=40)
entry2.grid(row=0, column=1, columnspan=4)

MyButton6 = ttk.Button(root, text='genarate', width=10, command=gen)
MyButton6.grid(row=2, column=4)

# ------------------- X ----------------

# WebSearch from box


class Memo:
    a=['Big','Cute','Red','Blue','Black','Back','Old','Dark','Small',
       'Captain','Large','Nice','Good','Lovely','Handsome','White',
       'Hero','Striker']
    n=['Apple','Ball','Bot','Bat','Chicken','Dog','Diamond','Disco'
       'Door','Egg','Earth','Fish','God','Girl','Ice','Ink','Jangle'
       'Joker','King','Lemon','Man','Mango','Nut','Park','Plastic',
       'Planet','Panther','Queen','Spider','Thor','Umbrella',
       'Women','X']
    nu=map(str,range(100,1000))
# =================== Internal ===============

def dom(event):
    t = threading.Thread(target=gen)
    t.start()
# ---------------------------------- X ------------------------------------------

entry2.bind('<Return>', dom)



entry2.focus()
root.wm_attributes('-topmost', 1)
root.mainloop()
