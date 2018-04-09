from cs1graphics import *
from time import sleep
import math

paper = Canvas()

paper.setBackgroundColor('skyBlue')
paper.setHeight(200)
paper.setWidth(300)
paper.setTitle('My World')

turtle = Layer()

body=Polygon(Point(-20,-20),Point(-30,0),Point(-20,20),Point(20,20),Point(30,0),Point(20,-20))
body.setFillColor('darkgreen')
body.setDepth(20)
turtle.add(body)

leg1=Square(13,Point(15,20))
leg1.setFillColor('olivedrab')
leg1.rotate(45)
turtle.add(leg1)

leg2=Square(13,Point(-15,20))
leg2.setFillColor('olivedrab')
leg2.rotate(45)
turtle.add(leg2)

leg3=Square(13,Point(-15,-20))
leg3.setFillColor('olivedrab')
leg3.rotate(45)
turtle.add(leg3)

leg4=Square(13,Point(15,-20))
leg4.setFillColor('olivedrab')
leg4.rotate(45)
turtle.add(leg4)

head=Square(13,Point(30,0))
head.setFillColor('olivedrab')
turtle.add(head)


turtle.moveTo(50,100)

def draw_animal():
    paper.add(turtle)

def show_animation():
    draw_animal()
    t = 0.1

    for i in range(100):
        x = (i//10)%2
        if x == 0:
            leg1.rotate(4)
            leg2.rotate(-4)
            leg3.rotate(4)
            leg4.rotate(-4)
        else: 
            leg1.rotate(-4)
            leg2.rotate(4)
            leg3.rotate(-4)
            leg4.rotate(4)
        turtle.move(1,0)
        sleep(t)

    for i in range(100):
        x = (i//10)%2
        y = (i/50)*math.pi
        if x == 0:
            leg1.rotate(4)
            leg2.rotate(-4)
            leg3.rotate(4)
            leg4.rotate(-4)
        else: 
            leg1.rotate(-4)
            leg2.rotate(4)
            leg3.rotate(-4)
            leg4.rotate(4)
        turtle.rotate(3.6)
        turtle.move(math.cos(y),math.sin(y))
        sleep(t)

    for i in range(100):
        x = (i//10)%2
        if x == 0:
            leg1.rotate(4)
            leg2.rotate(-4)
            leg3.rotate(4)
            leg4.rotate(-4)
        else: 
            leg1.rotate(-4)
            leg2.rotate(4)
            leg3.rotate(-4)
            leg4.rotate(4)
        turtle.move(1,0)
        sleep(t)
        
show_animation()