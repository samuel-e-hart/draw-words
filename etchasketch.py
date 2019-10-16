# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:02:26 2019

@author: Samuel Hart
"""

import turtle
t = turtle

### the next 26+ functions are drawn out turtle coordinates for the upper case character
def letA(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+a/2,y+a)
    t.goto(x+a,y)
    t.penup()
    t.goto(x+a/4,y+a/2)
    t.pendown()
    t.goto(x+(3*a)/4,y+a/2)
    return

def letB(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x+(3*a)/4,y+(.875*a))
    t.goto(x+(3*a)/4,y+(3*a)/4)
    t.goto(x+(3*a)/4,y+(.625*a))
    t.goto(x+(.25*a),y+(.5*a))
    t.goto(x+(.75*a),y+(.375*a))
    t.goto(x+(3*a)/4,y+a/4)
    t.goto(x+(3*a)/4,y+(.125*a))
    t.goto(x+a/4,y)
    t.goto(x,y)
    return

def letC(x,y,a):
    t.penup()
    t.goto(x,y+a/2)
    t.pendown()
    t.goto(x,y+(.375*a))
    t.goto(x+(.075*a),y+a/4)
    t.goto(x+a/4,y+(.125*a))
    t.goto(x+a/2,y)
    t.goto(x+(3*a)/4,y)
    t.penup()
    t.goto(x,y+a/2)
    t.pendown()
    t.goto(x,y+(.625*a))
    t.goto(x+(.075*a),y+(3*a)/4)
    t.goto(x+a/4,y+(.875*a))
    t.goto(x+a/2,y+a)
    t.goto(x+(3*a)/4,y+a)
    return

def letD(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x+(.375*a),y+a)
    t.goto(x+a/2,y+(.95*a))
    t.goto(x+(3*a)/4,y+(.625*a))
    t.goto(x+(3*a)/4,y+a/2)
    t.goto(x+(3*a)/4,y+(.375*a))
    t.goto(x+a/2,y+a/20)
    t.goto(x+(.375*a),y)
    t.goto(x+a/4,y)
    t.goto(x,y)
    return

def letE(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+(3*a)/4,y+a)
    t.penup()
    t.goto(x,y+a/2)
    t.pendown()
    t.goto(x+a/2,y+a/2)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+(3*a)/4,y)
    return

def letF(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+(3*a)/4,y+a)
    t.penup()
    t.goto(x,y+a/2)
    t.pendown()
    t.goto(x+a/2,y+a/2)
    return

def letG(x,y,a):
    t.penup()
    t.goto(x+a,y+(3*a)/4)
    t.pendown()
    t.goto(x+(3*a)/4,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x,y+(3*a)/4)
    t.goto(x,y+a/4)
    t.goto(x+a/4,y)
    t.goto(x+(3*a)/4,y)
    t.goto(x+a,y+a/4)
    t.goto(x+a,y+a/2)
    t.goto(x+a/2,y+a/2)
    return

def letH(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.penup()
    t.goto(x+(3*a)/4,y)
    t.pendown()
    t.goto(x+(3*a)/4,y+a)
    t.penup()
    t.goto(x+(3*a)/4,y+a/2)
    t.pendown()
    t.goto(x,y+a/2)
    return

def letI(x,y,a):
    t.penup()
    t.goto(x+a/3,y)
    t.pendown()
    t.goto(x+(2*a)/3,y)
    t.penup()
    t.goto(x+a/3,y+a)
    t.pendown()
    t.goto(x+(2*a)/3,y+a)
    t.penup()
    t.goto(x+a/2,y+a)
    t.pendown()
    t.goto(x+a/2,y)
    return

def letJ(x,y,a):
    t.penup()
    t.goto(x+a/3,y+a)
    t.pendown()
    t.goto(x+(2*a)/3,y+a)
    t.penup()
    t.goto(x+a/2,y+a)
    t.pendown()
    t.goto(x+a/2,y+a/4)
    t.goto(x+a/3,y)
    t.goto(x+a/6,y)
    t.goto(x,y+a/4)
    return

def letK(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.penup()
    t.goto(x+a/2,y+a)
    t.pendown()
    t.goto(x,y+a/2)
    t.goto(x+a/2,y)
    return

def letL(x,y,a):
    t.penup()
    t.goto(x,y+a)
    t.pendown()
    t.goto(x,y)
    t.goto(x+a/2,y)
    return

def letM(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+a/3,y+a/2)
    t.goto(x+(a*2)/3,y+a)
    t.goto(x+(a*2)/3,y)
    return

def letN(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+(a*2)/3,y)
    t.goto(x+(a*2)/3,y+a)
    return

def letO(x,y,a):
    t.penup()
    t.goto(x,y+a/4)
    t.pendown()
    t.goto(x+a/4,y)
    t.goto(x+(3*a)/4,y)
    t.goto(x+a,y+a/4)
    t.goto(x+a,y+(3*a)/4)
    t.goto(x+(3*a)/4,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x,y+(3*a)/4)
    t.goto(x,y+a/4)
    return

def letP(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x+a/2,y+(3*a)/4)
    t.goto(x+a/2,y+a/2)
    t.goto(x+a/4,y+a/2)
    t.goto(x,y+a/2)
    return

def letQ(x,y,a):
    t.penup()
    t.goto(x,y+a/4)
    t.pendown()
    t.goto(x+a/4,y)
    t.goto(x+(3*a)/4,y)
    t.goto(x+a,y+a/4)
    t.goto(x+a,y+(3*a)/4)
    t.goto(x+(3*a)/4,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x,y+(3*a)/4)
    t.goto(x,y+a/4)
    t.penup()
    t.goto(x+(3*a)/4,y+a/4)
    t.pendown()
    t.goto(x+a,y)
    return

def letR(x,y,a):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x+a/4,y+a)
    t.goto(x+a/2,y+(3*a)/4)
    t.goto(x+a/2,y+a/2)
    t.goto(x+a/4,y+a/2)
    t.goto(x,y+a/2)
    t.penup()
    t.goto(x+a/3,y+a/2)
    t.pendown()
    t.goto(x+a/2,y)
    return

def letS(x,y,a):
    t.penup()
    t.goto(x+(3*a)/4,y+a)
    t.pendown()
    t.goto(x,y+a)
    t.goto(x,y+a/2)
    t.goto(x+(3*a)/4,y+a/2)
    t.goto(x+(3*a)/4,y)
    t.goto(x,y)
    return

def letT(x,y,a):
    t.penup()
    t.goto(x+a/2,y)
    t.pendown()
    t.goto(x+a/2,y+a)
    t.penup()
    t.goto(x+a/4,y+a)
    t.pendown()
    t.goto(x+(3*a)/4,y+a)
    return

def letU(x,y,a):
    t.penup()
    t.goto(x,y+a)
    t.pendown()
    t.goto(x,y+a/4)
    t.goto(x+a/4,y)
    t.goto(x+(3*a)/4,y)
    t.goto(x+a,y+a/4)
    t.goto(x+a,y+a)
    return

def letV(x,y,a):
    t.penup()
    t.goto(x,y+a)
    t.pendown()
    t.goto(x+a/2,y)
    t.goto(x+a,y+a)
    return

def letW(x,y,a):
    t.penup()
    t.goto(x,y+a)
    t.pendown()
    t.goto(x+a/4,y)
    t.goto(x+a/2,y+a/2)
    t.goto(x+(3*a)/4,y)
    t.goto(x+a,y+a)
    return

def letX(x,y,a):
    t.penup()
    t.goto(x,y+a)
    t.pendown()
    t.goto(x+(3*a)/4,y)
    t.penup()
    t.goto(x+(3*a)/4,y+a)
    t.pendown()
    t.goto(x,y)
    return

def letY(x,y,a):
    t.penup()
    t.goto(x,y+a)
    t.pendown()
    t.goto(x+a/2,y+a/2)
    t.penup()
    t.goto(x+a,y+a)
    t.pendown()
    t.goto(x+a/2,y+a/2)
    t.goto(x+a/2,y)
    return

def letZ(x,y,a):
    """
    this function writes the letter z
    """
    t.penup()
    t.goto(x,y+a)
    t.pendown()  
    t.goto(x+(3*a)/4,y+a)
    t.goto(x,y)
    t.goto(x+(3*a)/4,y)
    return



    
    
# input what you want to say
mess = input("What do you want to say: ")
#make it upper case
mess = mess.upper()

#split it at the spaces to utilize the new list for lines of text
wordSpace = mess.split(" ")
mess = list(mess)
#i don't want to type turtle everytime
t = turtle
t.setup(640,480)
t.setworldcoordinates(0,0,1000,1000)
t.hideturtle()

#initialize wordCount, a variable that traverses through wordSpace
wordCount = 0
#the amount of space left on each line
spaceLeft = 10
### i need to run the mess string and implement spaces to push complete words to
### a new line
#initialize a copy of the message to insert spaces
temp = mess.copy()
# anytime the next word exceeds the spaceleft on the line, insert enough 
## blank spaces to bump it down to the next line as a complete word
for a in range(len(mess)):
    spaceLeft = 10-(a%10)
    if len(wordSpace[wordCount]) > spaceLeft:
        temp.insert(a," ")
    if mess[a] == " ":
        wordCount = wordCount + 1
print(temp)
# set mess to the new list with correct amount of spaces
mess = temp.copy()
#initialize h as the height counting down from the top of the window (i.e. y = 800 is
## equivalent to 1000-h when h is 200)
h = 100
# c is the len of mess
c = len(mess)
# while loop
i = 0
#while i < c:
## these if statements bump the message to the next line after there is no room
#    if i > 9:
#        h = 200
#        if i > 19:
#            h = 300
#            if i > 29:
#                h = 400
#                if i > 39:
#                    h = 500
#                    if i > 49:
#                        h = 600
#                        if i > 59:
#                            h = 700
#                            if i > 69:
#                                h = 800
#                                if i > 79:
#                                    h = 900
##    spaceLeft = 10-(i%10)
##    if len(wordSpace[wordCount]) > spaceLeft:
##        for a in range(spaceLeft):
##            mess.insert(i," ")
##            i = i + 1
##        h = h-100
##    
##    print(mess)
##    if 100*i > 900:
##        x =(i*100)%1000
##    else:
##        x = 100*i
##    print(i,x,1000-h)
#    
##initializing x
#    x = 0                         
#      
## each if statement calls a function to write a letter at the coordinates x,y
### where x is equal to the next 100 from the previous letter from 0 to 900
### and y is equal to 1000 - h
#    
#    if mess[i] == "A":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
##        print(i,x,1000-h)
#        letA(x,1000-h,50)
#    if mess[i] == "B":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letB(x,1000-h,50)
#    if mess[i] == "C":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letC(x,1000-h,50)
#    if mess[i] == "D":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letD(x,1000-h,50)
#    if mess[i] == "E":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letE(x,1000-h,50)
#    if mess[i] == "F":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letF(x,1000-h,50)
#    if mess[i] == "G":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letG(x,1000-h,50)
#    if mess[i] == "H":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letH(x,1000-h,50)
#    if mess[i] == "I":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letI(x,1000-h,50)
#    if mess[i] == "J":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letJ(x,1000-h,50)
#    if mess[i] == "K":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letK(x,1000-h,50)
#    if mess[i] == "L":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letL(x,1000-h,50)
#    if mess[i] == "M":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letM(x,1000-h,50)
#    if mess[i] == "N":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letN(x,1000-h,50)
#    if mess[i] == "O":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letO(x,1000-h,50)
#    if mess[i] == "P":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letP(x,1000-h,50)
#    if mess[i] == "Q":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letQ(x,1000-h,50)
#    if mess[i] == "R":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letR(x,1000-h,50)
#    if mess[i] == "S":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letS(x,1000-h,50)
#    if mess[i] == "T":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letT(x,1000-h,50)
#    if mess[i] == "U":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letU(x,1000-h,50)
#    if mess[i] == "V":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letV(x,1000-h,50)
#    if mess[i] == "W":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letW(x,1000-h,50)
#    if mess[i] == "X":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letX(x,1000-h,50)
#    if mess[i] == "Y":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letY(x,1000-h,50)
#    if mess[i] == "Z":
#        if 100*i > 900:
#            x =(i*100)%1000
#        else:
#            x = 100*i
#        letZ(x,1000-h,50)
#    if mess[i] == " ":
#        wordCount = wordCount + 1
#        None
#    i = i + 1
#        


#letA(100,800,50)
#letB(200,800,50)
#letC(300,800,50)
#letD(400,800,50)
#letE(500,800,50)
#letF(600,800,50)
#letG(700,800,50)
#letH(800,800,50)
#letI(100,700,50)
#letJ(200,700,50)
#letK(300,700,50)
#letL(400,700,50)
#letM(500,700,50)
#letN(600,700,50)
#letO(700,700,50)
#letP(800,700,50)
#letQ(100,600,50)
#letR(200,600,50)
#letS(300,600,50)
#letT(400,600,50)
#letU(500,600,50)
#letV(600,600,50)
#letW(700,600,50)
#letX(800,600,50)
#letY(100,500,50)
#letZ(200,500,50)
















t.exitonclick()