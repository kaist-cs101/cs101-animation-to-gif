from cs1graphics import *
from time import sleep

paper = Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('This World')

grass = Polygon(Point(0, 600), Point(800, 600), Point(800, 300), Point(0, 300))
grass.setFillColor('gray')
grass.setDepth(70)
paper.add(grass)
#add grass
#########################################
building = Rectangle(138, 450, Point(138, 270))
building.setFillColor('white')
building.setDepth(60)
paper.add(building)

window1 = Rectangle(46, 60, Point(105.8, 90))
window1.setFillColor('azure3')
window1.setDepth(50)
paper.add(window1)
window2 = Rectangle(46, 60, Point(105.8, 165))
window2.setFillColor('azure3')
window2.setDepth(50)
paper.add(window2)
window3 = Rectangle(46, 60, Point(105.8, 240))
window3.setFillColor('azure3')
window3.setDepth(50)
paper.add(window3)
window4 = Rectangle(46, 60, Point(105.8, 315))
window4.setFillColor('azure3')
window4.setDepth(50)
paper.add(window4)
window5 = Rectangle(46, 60, Point(170.2, 90))
window5.setFillColor('azure3')
window5.setDepth(50)
paper.add(window5)
window6 = Rectangle(46, 60, Point(170.2, 165))
window6.setFillColor('azure3')
window6.setDepth(50)
paper.add(window6)
window7 = Rectangle(46, 60, Point(170.2, 240))
window7.setFillColor('azure3')
window7.setDepth(50)
paper.add(window7)
window8 = Rectangle(46, 60, Point(170.2, 315))
window8.setFillColor('azure3')
window8.setDepth(50)
paper.add(window8)
######################################################building1

building2 = Rectangle(138, 300, Point(575, 210))
building2.setFillColor('white')
building2.setDepth(60)
paper.add(building2)

window22 = Rectangle(46, 60, Point(542.8, 105))
window22.setFillColor('azure3')
window22.setDepth(50)
paper.add(window22)
window32 = Rectangle(46, 60, Point(542.8, 180))
window32.setFillColor('azure3')
window32.setDepth(50)
paper.add(window32)
window42 = Rectangle(46, 60, Point(542.8, 255))
window42.setFillColor('azure3')
window42.setDepth(50)
paper.add(window42)
window62 = Rectangle(46, 60, Point(607.2, 105))
window62.setFillColor('azure3')
window62.setDepth(50)
paper.add(window62)
window72 = Rectangle(46, 60, Point(607.2, 180))
window72.setFillColor('azure3')
window72.setDepth(50)
paper.add(window72)
window82 = Rectangle(46, 60, Point(607.2, 255))
window82.setFillColor('azure3')
window82.setDepth(50)
paper.add(window82)

#######################
monster = Layer()

body = Circle(80, Point(50, 100))
body.setFillColor('yellowgreen')
body.setDepth(5)
monster.add(body)

eye = Circle(50, Point(50, 80))
eye.setFillColor('white')
eye.setDepth(5)
monster.add(eye)

mouth = Ellipse(30, 20, Point(50, 155))
mouth.setFillColor('darkslategrey')
mouth.setDepth(5)
monster.add(mouth)

pupil1 = Circle(30, Point(50, 80))
pupil1.setFillColor('mediumseagreen')
pupil1.setDepth(5)
monster.add(pupil1)

pupil2 = Circle(20, Point(50, 80))
pupil2.setFillColor('black')
pupil2.setDepth(5)
monster.add(pupil2)

leg1 = Rectangle(15, 80, Point(25, 180))
leg1.setFillColor('yellowgreen')
leg1.setDepth(20) # behind the tires
monster.add(leg1)

leg2 = Rectangle(15, 80, Point(75, 180))
leg2.setFillColor('yellowgreen')
leg2.setDepth(20) # behind the tires
monster.add(leg2)

feet1 = Rectangle(25, 10, Point(22, 220))
feet1.setFillColor('yellowgreen')
feet1.setDepth(20) # behind the tires
monster.add(feet1)

feet2 = Rectangle(25, 10, Point(78, 220))
feet2.setFillColor('yellowgreen')
feet2.setDepth(20) # behind the tires
monster.add(feet2)

arm1 = Rectangle(10, 80, Point(-25, 130))
arm1.setFillColor('yellowgreen')
arm1.setDepth(30) # behind the tires
monster.add(arm1)

arm2 = Rectangle(10, 80, Point(125, 130))
arm2.setFillColor('yellowgreen')
arm2.setDepth(30) # behind the tires
monster.add(arm2)

horn1 = Ellipse(20, 30, Point(-5, 45))
horn1.setFillColor('blanchedalmond')
horn1.setDepth(30) 
monster.add(horn1)

horn2 = Ellipse(20, 30, Point(105, 45))
horn2.setFillColor('blanchedalmond')
horn2.setDepth(30) 
monster.add(horn2)

monster.moveTo(200, 200)
paper.add(monster)
#################
ball = Layer()
body = Circle(30, Point(600, 400))
body.setFillColor('gold')
ball.add(body)
ball.move(3,0)

paper.add(ball)
###############




timedelay = 0.002
sleep(timedelay)

for i in range(3):
    monster.move(0,-50)
    arm1.rotate(130)
    arm1.move(0, -30)
    arm2.rotate(-130)
    arm2.move(0, -30)
    sleep(0.5)
    monster.move(0,50)
    arm1.move(0, 30)
    arm1.rotate(-130)
    arm2.rotate(130)
    arm2.move(0, 30)
    sleep(0.5)
    


for i in range(30):
    monster.move(10,0)
    arm1.rotate(30)
    arm2.rotate(-30)
    leg1.move(-15, 0)
    leg2.move(5, 0)
    feet1.move(-15, 0)
    feet2.move(5, 0)
    sleep(timedelay)
    arm1.rotate(-30)
    arm2.rotate(30)
    leg1.move(15, 0)
    leg2.move(-5, 0)
    feet1.move(15, 0)
    feet2.move(-5, 0)
    sleep(timedelay)
    
    
leg2.move(0, -10)
leg2.rotate(-40)
feet2.move(18, -20)
feet2.rotate(-40)
ball.move(10, -10)

sleep(0.2)

for i in range(700):
    ball.move(5,-5)
    sleep(0.0001)