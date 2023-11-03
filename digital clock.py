'''
#digitel clock

import time
import datetime as dt
import turtle
t=turtle.Turtle()
t1=turtle.Turtle()
S=turtle.Screen()
S.bgcolor("green")
sec=dt.datetime.now().second
min=dt.datetime.now().minute
hr=dt.datetime.now().hour
t1.pensize(3)
t1.color('black')
t1.penup()
t1.goto(-20,0)
t1.pendown()
for i in range(2):
    t1.forward(210)
    t1.left(90)
    t1.forward(70)
    t1.left(90)
    t1.hideturtle()
while True:
    t.hideturtle()
    t.clear()
    t.write(str(hr).zfill(2)
            +":"+str(min).zfill(2)
            +":"+str(sec).zfill(2),
            font=("Aril Narrow",35,"bold"))
    time.sleep(1)
    sec+=1
    if sec==60:
        sec=0
        min=1
    if min==60:
        min=0
        hr+=1
    if hr==13:
        hr=1
'''




#grifik digine
import turtle
from turtle import *
wn=Screen()
wn.bgcolor('black')
t=turtle.Turtle()
t.pencolor('white')
def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)
def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.end_fill()

heart()
t.ht()

def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil Std',18,'italic')
    t.write(message,font=style)
write('I',(-65,95))
write('L',(-55,95))      
write('O',(-42,95))
write('V',(-29,95))
write('E',(-14,95))
write('Y',(10,95))
write('O',(26,95))
write('U',(45,95))
wn.mainloop()

                                            
                        

