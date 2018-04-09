from cs1graphics import *
from time import sleep

canvas = Canvas(300,200,'skyblue', 'My world')

miyuk = Polygon(Point(10, 200), Point(30, 185) , 
             Point(10, 170),  Point(30, 155), Point(10,140), Point(30,125),
             Point(35,125),Point(15,140), Point(35, 155),Point(15, 170),Point(35,185),Point(15,200))
miyuk.setFillColor('green')
canvas.add(miyuk)

miyuk2 = miyuk.clone()
miyuk2.moveTo(50,200)
canvas.add(miyuk2)

miyuk3 = miyuk.clone()
miyuk3.moveTo(150,200)
canvas.add(miyuk3)

sanho = Rectangle(30,70, Point(120,200))
sanho.setFillColor('red')
canvas.add(sanho)



dot = Path(Point(230,150),Point(230,100))
dot.setBorderWidth(3)
canvas.add(dot)

git = Polygon(Point(230,100),Point(230,130),Point(265,115))
git.setFillColor('black')
canvas.add(git)

fish=Layer()

body=Polygon(Point(160,50),Point(205,5), Point(205,25),Point(230,50),Point(205,75),Point(205,95))
body.setFillColor('blue')
fish.add(body)

eye=Circle(3,Point(175,42))
eye.setFillColor('black')
fish.add(eye)

tail=Layer()

tai=Polygon(Point(220,50), Point(240,15) ,Point(240,85) )

tai.setFillColor('red')
tai.setDepth(80)
tail.add(tai)

rain=Layer()

boil=Circle(10, Point(120,150))
boil.setBorderWidth(2)

rain.add(boil)


hok=Layer()
head = Circle(10, Point(200,150))
head.setFillColor('brown')
head.setDepth(80)
hok.add(head)

bod = Polygon(Point(190,150),Point(210,150), Point(210,170), Point(190,170))

ship = Polygon(Point(180,150),Point(280,150),Point(260,200),Point(200,200))
ship.setFillColor('gray')
hok.add(ship)


canvas.add(tail)
canvas.add(fish)
canvas.add(rain)
canvas.add(hok)

timedelay=0.5
sleep(timedelay)

fish.move(-20,0)
tail.adjustReference(220,50)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)


sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)


sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

sleep(timedelay)

fish.move(-20,0)
tail.move(-20,0)
tail.rotate(-15)
rain.move(0,-10)

show_animation
