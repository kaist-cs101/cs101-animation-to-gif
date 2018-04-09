from cs1graphics import *
from time import sleep

def draw_animal():
    global layer, row1, row2, row3, row4
    body=Polygon(Point(80,200), Point(200,200), Point(240,240), Point(200,280), Point(80,280))
    body.setFillColor('blue')
    layer.add(body)

    row1=Rectangle(10, 120, Point(120,140))
    row1.adjustReference(0, 60)
    row1.setFillColor('red')
    layer.add(row1)

    row2=Rectangle(10, 120, Point(180,140))
    row2.adjustReference(0, 60)
    row2.setFillColor('red')
    layer.add(row2)

    row3=Rectangle(10, 120, Point(120,340))
    row3.adjustReference(0, -60)
    row3.setFillColor('red')
    layer.add(row3)

    row4=Rectangle(10, 120, Point(180,340))
    row4.adjustReference(0, -60)
    row4.setFillColor('red')
    layer.add(row4)

def show_animation_fr():
    for i in range(75):
        row1.rotate(-1)
        row2.rotate(-1)
        row3.rotate(1)
        row4.rotate(1)
        sleep(0.001)
        layer.move(2.5,0)
    
def show_animation_bk():
    for i in range(100):
        row1.rotate(1)
        row2.rotate(1)
        row3.rotate(-1)
        row4.rotate(-1)
        sleep(0.001)
        layer.move(0.5,0)

canvas=Canvas(1000,480)
canvas.setBackgroundColor("light blue")
layer=Layer()
row1=None
row2=None
row3=None
row4=None
canvas.add(layer)
draw_animal()

for i in range(2):
    show_animation_fr()
    show_animation_bk()

show_animation_fr()
##row1=Rectangle(120, 10, Point(120,200))
##row1.setFillColor('red')
##layer.add(row1)