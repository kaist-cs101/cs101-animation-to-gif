from cs1graphics import *
from time import sleep

pink = (255,100,180)
timeDelay = 1
black = (255, 255, 255)
white = (0, 0, 0)


paper = Canvas()

paper.setBackgroundColor('skyBlue')
paper.setWidth(1000)
paper.setHeight(500)
paper.setTitle('My World')

background = Layer()

for i in range(15):
    for j in range(10):
        leaf1 = Rectangle(10,10)
        leaf1.setFillColor("pink")
        leaf1.rotate(45)
        leaf1.moveTo(i*90+40,j*90+40)
        background.add(leaf1)


bike = Layer()

tire1 = Circle(50, Point(200,400))
tire1.setFillColor('black')
bike.add(tire1)
subtire1 = Rectangle(50,10,Point(200,400))
subtire1.setFillColor('white')
bike.add(subtire1)

tire2 = Circle(50, Point(400,400))
tire2.setFillColor('black')
bike.add(tire2)
subtire2 = Rectangle(50,10,Point(400,400))
subtire2.rotate(90)
subtire2.setFillColor('white')
bike.add(subtire2)

framebelow = Rectangle(100,10, Point(300, 400))
framebelow.setFillColor('white')
bike.add(framebelow)
frame1 = Rectangle(100, 10, Point(200, 300))
frame1.setFillColor('white')
frame1.rotate(90)
bike.add(frame1)

frame2 = Rectangle(100, 10, Point(400, 300))
frame2.setFillColor('white')
frame2.rotate(90)

frameabove = Rectangle(300,10, Point(300, 250))
frameabove.setFillColor('white')
bike.add(frameabove)
bike.add(frame2)

handle = Rectangle(60,15, Point(450,250))
handle.setFillColor('black')
handle.rotate(125)
bike.add(handle)

paper.add(bike)




paper.add(background)

for i in range(30):
    if i%2 ==0:
        background.move(10,3)
    elif i%2 ==1:
        background.move(-10,3)
    bike.move(10, 0)
    subtire1.rotate(45)
    subtire2.rotate(45)
    sleep(timeDelay)







