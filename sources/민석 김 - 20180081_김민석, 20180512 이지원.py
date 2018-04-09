from cs1graphics import *
from time import sleep

# title : Tear of Antarctic

paper=Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(600)
paper.setHeight(600)

peng=Layer()

floar=Polygon(Point(600, 300), Point(0, 300), Point(0,600), Point(600, 600))
floar.setDepth(0)
floar.setFillColor('white')
peng.add(floar)

water=Polygon(Point(800, 400), Point(600, 400), Point(600,600), Point(800, 600))
water.setDepth(0)
water.setFillColor('blue')
peng.add(water)

head=Circle(30, Point(220,100))
head.setFillColor('black')
head.setDepth(30)
peng.add(head)

body=Polygon(Point(200, 100), Point(250, 100), Point(250,300), Point(200, 300))
body.setDepth(0)
body.setFillColor('white')
peng.add(body)

wing=Polygon(Point(250,100),Point(250,300),Point(280,300))
wing.setDepth(0)
wing.setFillColor('black')
peng.add(wing)

beak=Polygon(Point(180,95),Point(180,105),Point(150,100))
beak.setDepth(30)
beak.setFillColor('black')
peng.add(beak)


#


head1=Circle(15, Point(340,200))
head1.setFillColor('black')
head1.setDepth(30)
peng.add(head1)

body1=Polygon(Point(330, 200), Point(330, 300), Point(360,300), Point(360, 200))
body1.setDepth(0)
body1.setFillColor('gray')
peng.add(body1)

wing1=Polygon(Point(360,200),Point(360,300),Point(380,300))
wing1.setDepth(0)
wing1.setFillColor('white')
peng.add(wing1)

beak1=Polygon(Point(320,197),Point(320,203),Point(310,200))
beak1.setDepth(30)
beak1.setFillColor('black')
peng.add(beak1)


paper.add(peng)

timeDelay = 0.5
sleep(timeDelay)
for i in range (15):
    wing.flip()
    peng.move(-10, 0)
    wing1.flip()
    sleep(timeDelay)
