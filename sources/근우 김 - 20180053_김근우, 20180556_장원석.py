from cs1graphics import *
from time import sleep
paper=Canvas()
paper.setBackgroundColor('green')
paper.setWidth(700)
paper.setHeight(500)

hole=Circle(100,Point(700,200))
hole.setFillColor('black')
paper.add(hole)

bug=Layer()
def draw_animal():
    global bug, eye1, eye2
    head=Circle(60,Point(200,200))
    head.setFillColor('brown')

    body=Rectangle(250,120,Point(330,200))

    head2=Circle(60,Point(450,200))



    head2.setFillColor('brown')
    body.setFillColor('brown')
    eye1=Circle(5,Point(470,180))
    eye1.setFillColor('white')

    eye2=Circle(5,Point(470,220))
    eye2.setFillColor('white')

    line=Path(Point(250,150),Point(250,250))

    line2=Path(Point(290,150),Point(290,250))

    line3=Path(Point(330,150),Point(330,250))

    line4=Path(Point(370,150),Point(370,250))

    line5=Path(Point(410,150),Point(410,250))




    bug.add(body)
    bug.add(head)
    bug.add(head2)
    bug.add(eye1)
    bug.add(eye2)
    bug.add(line)
    bug.add(line2)
    bug.add(line3)
    bug.add(line4)
    bug.add(line5)

    paper.add(bug)


def show_animation():
    global bug,eye1,eye2
    timeDelay=2
    sleep(timeDelay)

    bug.move(10,0)
    eye1.move(0,10)
    eye2.move(0,-10)
    sleep(timeDelay)

    bug.move(30,0)
    sleep(timeDelay)
    eye1.move(0,-10)
    eye2.move(0,10)


    bug.move(50,0)
    sleep(timeDelay)
    eye1.move(0,10)
    eye2.move(0,-10)


    bug.move(70,0)
    sleep(timeDelay)
    eye1.move(0,-10)
    eye2.move(0,10)



    bug.move(100,0)
    sleep(timeDelay)
    eye1.move(0,10)
    eye2.move(0,-10)

draw_animal()
show_animation()