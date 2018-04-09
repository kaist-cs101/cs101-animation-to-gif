from cs1graphics import *
from time import sleep
paper = Canvas(300, 200, 'skyBlue', 'My World')
grass = Rectangle(300,90,Point(150,155))
grass.setFillColor('green')
grass.setBorderColor('green')
paper.add(grass)

bird = Layer()

body = Ellipse(70, 30, Point(0,0))
body.setFillColor('white')
body.setBorderColor('white')
body.setDepth(20)

bird.add(body)

leg1 = Layer()
leg2 = Layer()

leftleg=Rectangle(4,10,Point(-6,19))
leftleg.setFillColor('orange')
rightleg=Rectangle(4,10,Point(6,19))
rightleg.setFillColor('orange')
leftleg.setDepth(25)
rightleg.setDepth(25)
leg1.add(leftleg)
leg2.add(rightleg)

bird.add(leg1)
bird.add(leg2)

high = Layer()

neck = Rectangle(13, 60, Point(0,-30))
neck.setFillColor('white')
neck.setBorderColor('white')
neck.setDepth(25)

head = Circle(10, Point(0,-60))
head.setFillColor('white')
head.setBorderColor('white')
head.setDepth(20)

eyeball = Circle(3, Point(0, -63))
eyeball.setFillColor('black')
eyeball.setBorderColor('black')
eyeball.setDepth(15)

beak = Polygon(Point(8, -63), Point(8, -57), Point(15, -60))
beak.setFillColor('yellow')
beak.setBorderColor('yellow')
beak.setDepth(25)

high.add(neck)
high.add(head)
high.add(eyeball)
high.add(beak)

bird.add(high)
paper.add(bird)
high.moveTo(28,0)
bird.moveTo(50, 150)

i = 0
while True:
    timeDelay = 0.025
    sleep(timeDelay)
    if i%40 < 20:
        high.rotate(2.25)
        leg1.move(0.6,0)
        leg2.move(-0.6,0)
    else:
        high.rotate(-2.25)
        leg1.move(-0.6,0)
        leg2.move(0.6,0)
    bird.move(2,0)
    i = i + 1