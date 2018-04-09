from cs1graphics import *
from time import sleep

paper = Canvas(400, 300, "skyBlue")
body = Ellipse (w=100,h=50,centerPt=Point(300,200))
body.setFillColor("White")
leg1 = Ellipse (w=15,h=50,centerPt=Point(330,230))
leg1.setFillColor("White")
leg2 = Ellipse (w=15,h=50,centerPt=Point(270,230))
leg2.setFillColor("White")
head = Circle (25,Point(240,200))
head.setFillColor("White")
ear1 = Circle (10,Point(220,180))
ear1.setFillColor("White")
ear2 = Circle (10,Point(260,180))
ear2.setFillColor("White")
eye1 = Circle (3,Point(250,190))
eye1.setFillColor("Black")
eye2 = Circle (3,Point(230,190))
eye2.setFillColor("Black")
nose = Ellipse (w=10,h=5,centerPt=Point(240,200))
nose.setFillColor("Black")
paper.add(body)
paper.add(leg1)
paper.add(leg2)
paper.add(ear1)
paper.add(ear2)
paper.add(head)
paper.add(eye1)
paper.add(eye2)
paper.add(nose)






brown = Layer()
body = Ellipse (w=100,h=50,centerPt=Point(300,130))
body.setFillColor("Brown")
leg3 = Ellipse (w=15,h=50,centerPt=Point(330,160))
leg3.setFillColor("Brown")
leg4 = Ellipse (w=15,h=50,centerPt=Point(270,160))
leg4.setFillColor("Brown")
head = Circle (25,Point(240,130))
head.setFillColor("Brown")
ear1 = Circle (10,Point(220,110))
ear1.setFillColor("Brown")
ear2 = Circle (10,Point(260,110))
ear2.setFillColor("Brown")
eye1 = Circle (3,Point(250,120))
eye1.setFillColor("Black")
eye2 = Circle (3,Point(230,120))
eye2.setFillColor("Black")
nose = Ellipse (w=10,h=5,centerPt=Point(240,130))
nose.setFillColor("Black")
brown.add(body)
brown.add(leg3)
brown.add(leg4)
brown.add(ear1)
brown.add(ear2)
brown.add(head)
brown.add(eye1)
brown.add(eye2)
brown.add(nose)

paper.add(brown)

panda = Layer()
body = Ellipse (w=100,h=50,centerPt=Point(300,60))
body.setFillColor("White")
leg5 = Ellipse (w=15,h=50,centerPt=Point(330,90))
leg5.setFillColor("White")
leg6 = Ellipse (w=15,h=50,centerPt=Point(270,90))
leg6.setFillColor("White")
head = Circle (25,Point(240,60))
head.setFillColor("White")
ear1 = Circle (10,Point(220,40))
ear1.setFillColor("White")
ear2 = Circle (10,Point(260,40))
ear2.setFillColor("Black")
eye1 = Circle (3,Point(250,50))
eye1.setFillColor("Black")
eye2 = Circle (3,Point(230,50))
eye2.setFillColor("Black")
nose = Ellipse (w=10,h=5,centerPt=Point(240,60))
nose.setFillColor("Black")
stripe1 = Ellipse (w=15,h=50,centerPt=Point(310,60))
stripe1.setFillColor("Black")
stripe2 = Ellipse (w=15,h=50,centerPt=Point(290,60))
stripe2.setFillColor("Black")
panda.add(body)
panda.add(leg5)
panda.add(leg6)
panda.add(ear1)
panda.add(ear2)
panda.add(head)
panda.add(eye1)
panda.add(eye2)
panda.add(nose)
panda.add(stripe1)
panda.add(stripe2)
paper.add(panda)

def animate_fallp(bear):
    for i in range(100):
        bear.move(-1, 0)
        leg5.rotate(45)
        leg5.rotate(-90)
        leg5.rotate(45)
        leg6.rotate(45)
        leg6.rotate(-90)
        leg6.rotate(45)

    for i in range(50):
        bear.move(-1, 1)
        leg5.rotate(45)
        leg5.rotate(-90)
        leg5.rotate(45)
        leg6.rotate(45)
        leg6.rotate(-90)
        leg6.rotate(45)
    for i in range(100):
        bear.move(0, 1)
        leg5.rotate(45)
        leg5.rotate(-90)
        leg5.rotate(45)
        leg6.rotate(45)
        leg6.rotate(-90)
        leg6.rotate(45)
    for i in range(200):
        bear.move(-1, 0)
        leg5.rotate(45)
        leg5.rotate(-90)
        leg5.rotate(45)
        leg6.rotate(45)
        leg6.rotate(-90)
        leg6.rotate(45)
        
def animate_fallb(bear):
    for i in range(100):
        bear.move(-1, 0)
        leg3.rotate(45)
        leg3.rotate(-90)
        leg3.rotate(45)
        leg4.rotate(45)
        leg4.rotate(-90)
        leg4.rotate(45)
    for i in range(50):
        bear.move(-1, 1)
        leg3.rotate(45)
        leg3.rotate(-90)
        leg3.rotate(45)
        leg4.rotate(45)
        leg4.rotate(-90)
        leg4.rotate(45)
    for i in range(50):
        bear.move(0, 1)
        leg3.rotate(45)
        leg3.rotate(-90)
        leg3.rotate(45)
        leg4.rotate(45)
        leg4.rotate(-90)
        leg4.rotate(45)


animate_fallp(panda)
animate_fallb(brown)