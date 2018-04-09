from cs1graphics import *
from time import sleep
paper = Canvas()
paper.setBackgroundColor('darkBlue')
paper.setWidth(1080)
paper.setHeight(550)

def tree(x):
    tree = Layer()
    body = Rectangle(30,80,Point(x,420))
    body.setFillColor('brown')
    tree.add(body)
    leaf=Polygon(Point(x,280),Point(x-30,380), Point(x+30,380))
    leaf.setFillColor('darkGreen')
    tree.add(leaf)
    paper.add(tree)

tree(60)
tree(140)
tree(700)
tree(600)
tree(530)

snowman = Layer()
d = Circle(80,Point(300,400))
d.setFillColor('white')
snowman.add(d)
u = Circle(60,Point(300,280))
u.setFillColor('white')
snowman.add(u)
e1 = Circle(8,Point(280,270))
e1.setFillColor('black')
snowman.add(e1)
e2 = Circle(8,Point(320,270))
e2.setFillColor('black')
snowman.add(e2)
b1 = Circle(10,Point(300,360))
b1.setFillColor('brown')
snowman.add(b1)
b2 = Circle(10,Point(300,400))
b2.setFillColor('brown')
snowman.add(b2)
b3 = Circle(10,Point(300,440))
b3.setFillColor('brown')
snowman.add(b3)
n = Polygon(Point(300,290), Point(300,300), Point(200,310))
n.setFillColor('orange')
snowman.add(n)
paper.add(snowman)
s = Circle(50,Point(700,100))
s.setFillColor('yellow')
paper.add(s)

r = Rectangle(800,150,Point(400,530))
r.setFillColor('white')
paper.add(r)

import random

l = []
for i in range(50):
    a = random.randint(0, 1000)
    b = random.randint(0, 600)
    r = random.randint(5, 10)
    snow = Circle(r,Point(a,b))
    snow.setFillColor('white')
    snow.setBorderColor('white')
    l.append(snow)
    paper.add(snow)
snow 

while True:
    for i in range(3) :
        for snow in l:
            a = random.randint(2, 3)
            snow.move(0, a)
            sleep(0.001)

        v = -20
        for i in range (5) :
            v = v+5*i
            snowman.move(0,v)
            sleep(0.1)

