from cs1graphics import *
from time import sleep

timeDelay = 0.7

paper = Canvas(600, 600, 'skyBlue')

man = Layer()

head = Circle(50, Point(300, 100))
head.setFillColor('white')
head.setBorderColor('black')
man.add(head)

arm1 = Path(Point(300,175), Point(450,220))
man.add(arm1)
paper.add(man)

arm2 = Path(Point(150,220), Point(300,175))
man.add(arm2)

body = Path(Point(300,150), Point(300,375))
man.add(body)

leg1 = Path(Point(300,375), Point(450,475))
man.add(leg1)


leg2 = Path(Point(150,475), Point(300,375))
man.add(leg2)

leg1.adjustReference(0,0)
leg1.rotate(50)

arm1.adjustReference(0,0)
arm1.rotate(30)

for i in range(4):

    man.move(25,0)
    sleep(timeDelay)

    leg1.adjustReference(0,0)
    leg1.rotate(50)

    arm1.adjustReference(0,0)
    arm1.rotate(30)
    
for i in range(8):

    man.move(-25,0)
    sleep(timeDelay)

    leg1.adjustReference(0,0)
    leg1.rotate(-50)

    arm1.adjustReference(0,0)
    arm1.rotate(-30)


