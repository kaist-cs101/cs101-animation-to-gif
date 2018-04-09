from cs1graphics import *
from time import*
import math
cos=math.cos
pi=math.pi

paper=Canvas(300,200,'skyBlue','My World')

grass = Rectangle(300, 80, Point(150, 160))
grass.setFillColor('blue')
grass.setBorderColor('blue')
grass.setDepth(100)
paper.add(grass)

cloud=Layer()

clo1=Circle(20,Point(10,40))
clo1.setFillColor('white')
clo1.setBorderColor('white')
clo1.setDepth(100)
cloud.add(clo1)

clo2=clo1.clone()
clo2.move(20,0)
cloud.add(clo2)
clo3=clo2.clone()
clo3.move(20,0)
cloud.add(clo3)

cloud2=Layer()
cloud2=cloud.clone()
cloud2.move(300,0)




paper.add(cloud)
paper.add(cloud2)

chi=Layer()

chih=Layer()

head = Circle(30, Point(170, 70))
head.setFillColor('yellow')
head.setBorderColor('yellow')
head.setDepth(20)
chih.add(head)

mo=Polygon(Point(142,75),Point(150,90),Point(125,90))
mo.setFillColor('orange')
mo.setBorderColor('orange')
mo.setDepth(0)
chih.add(mo)

eye=Circle(5,Point(160,70))
eye.setFillColor('black')
eye.setDepth(10)
chih.add(eye)

body = Circle(50, Point(150, 100))
body.setFillColor('yellow')
body.setBorderColor('yellow')
body.setDepth(30)
chi.add(body)

wing = Rectangle(100, 40, Point(150, 50))
wing.setFillColor('skyBlue')
wing.setBorderColor('skyBlue')
wing.setDepth(29)
chi.add(wing)

chi.rotate(-20)
chi.setDepth(20)
chih.setDepth(10)
paper.add(chi)
paper.add(chih)
chi.moveTo(80,50)
chih.moveTo(30,0)

t=0.05
sleep(t)

for i in range(110):
    chi.move(-3,0)
    chih.move(-3,0)
    cloud.move(-2,0)
    cloud2.move(-2,0)
    x=cos(pi*i/10)*2.00
    y=-x*0.3639
    chih.move(x,y)
    sleep(t)
