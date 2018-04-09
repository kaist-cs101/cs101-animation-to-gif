from cs1graphics import *
from time import sleep

paper=Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(300)
paper.setHeight(200)

def draw_animal():
    global paper
    global tire
    global car
    car = Layer()
    #tire1 = Circle(10, Point(-20, -10))
    tire=Layer()
    tire1 = Circle(10, Point(0,0))
    tire1.setFillColor('black')
    tire11=Circle(2,Point(0,4))
    tire11.setFillColor('white')
    tire.add(tire1)
    tire.add(tire11)
    tire.moveTo(-20,-10)
    car.add(tire)
    tire2 = Circle(10, Point(20, -10))
    tire2.setFillColor('black')
    car.add(tire2)
    body = Polygon(Point(-35,-40), Point(15,-40), Point(15,-60),Point(35,-60), Point(35, -10),Point(-35,-10))
    body.setFillColor('blue')
    body.setDepth(60) # behind the tires
    car.add(body)
    car.moveTo(70, 180)
    car.setDepth(20) # in front of the house
    paper.add(car)

    road=Layer()
    rd=Rectangle(300,30,Point(0,0))
    rd.setFillColor('darkgray')
    road.add(rd)
    road.moveTo(150,170)
    paper.add(road)


def show_animation(timedelay):
    for i in range(25):
        car.move(10,0)
        tire.rotate(45)
        sleep(timedelay)

draw_animal()
show_animation(0.5)
