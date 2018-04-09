from cs1graphics import *
from time import sleep
paper = Canvas()
zam=Layer()


paper.setBackgroundColor('skyBlue')
paper.setWidth(500)
paper.setHeight(300)
paper.setTitle('My World')

wing1 = Rectangle()
wing2 = Rectangle()
wing3 = Rectangle()
wing4 = Rectangle()

def draw_animal():
    global wing1
    global wing2
    global wing3
    global wing4
    head = Circle(25, Point(290,150))
    head.setFillColor('brown')
    head.setDepth(20)
    zam.add(head)


    body = Rectangle(200, 40, Point(175,150))
    body.setFillColor('red')
    body.setDepth(30) # in front of roof
    zam.add(body)

    wing1 = Rectangle(30, 70, Point(170,110))
    wing1.adjustReference(-15, 35)
    wing1.rotate(330)
    wing1.setFillColor('white')
    wing1.setDepth(60) # in front of roof
    zam.add(wing1)

    wing2 = Rectangle(30, 70, Point(170,190))
    wing2.adjustReference(-15, -35)
    wing2.rotate(30)
    wing2.setFillColor('white')
    wing2.setDepth(60) # in front of roof
    zam.add(wing2)

    wing3 = Rectangle(30, 70, Point(250,190))
    wing3.adjustReference(-15, -35)
    wing3.rotate(30)
    wing3.setFillColor('white')
    wing3.setDepth(60) # in front of roof
    zam.add(wing3)

    wing4 = Rectangle(30, 70, Point(250,110))
    wing4.adjustReference(-15, 35)
    wing4.rotate(330)
    wing4.setFillColor('white')
    wing4.setDepth(60) # in front of roof
    zam.add(wing4)

    paper.add(zam)
def show_animation() :
    global wing1
    global wing2
    global wing3
    global wing4
    timeDelay = 1
    sleep(timeDelay)
    for i in range (8) :     
        zam.move(10, 0)
        wing1.rotate(60)
        wing2.rotate(-60)
        wing3.rotate(-60)
        wing4.rotate(60)
        sleep(timeDelay)
        zam.move(10, 0)
        wing1.rotate(-60)
        wing2.rotate(60)
        wing3.rotate(60)
        wing4.rotate(-60)
        sleep(timeDelay)

draw_animal()
show_animation()