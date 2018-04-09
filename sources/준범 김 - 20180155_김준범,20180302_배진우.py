from cs1graphics import *
from time import sleep
cloud = Layer()



paper = Canvas()
rain1 = Rectangle(2,60)
rain2 = Rectangle(2,60)
rain3 = Rectangle(2,60)
rain4 = Rectangle(2,80)
rain5 = Rectangle(2,60)
rain6 = Rectangle(2,60)
rain7 = Rectangle(2,80)
rain8 = Rectangle(2,60)
rain9 = Rectangle(2,60)
rain10 = Rectangle(2,80)
rain11 = Rectangle(2,60)
rain12 = Rectangle(2,60)
rain13 = Rectangle(2,80)
rain14 = Rectangle(2,60)
rain15 = Rectangle(2,60)
rain16 = Rectangle(2,60)
rain17 = Rectangle(2,60)
rain18 = Rectangle(2,60)
rain19 = Rectangle(2,80)
rain20 = Rectangle(2,60)
rain21 = Rectangle(2,60)
rain22 = Rectangle(2,80)
rain23 = Rectangle(2,60)
rain24 = Rectangle(2,60)
rain25 = Rectangle(2,80)
rain26 = Rectangle(2,60)
rain27 = Rectangle(2,60)
rain28 = Rectangle(2,80)
rain29 = Rectangle(2,60)
rain30 = Rectangle(2,60)





bicycle = Layer()

tire1 = Circle(30, Point(-60, -30))
tire1.setFillColor('black')
bicycle.add(tire1)
tire2 = Circle(30, Point(60,-30))
tire2.setFillColor('black')
bicycle.add(tire2)
paper.add(bicycle)
bicycle.moveTo(600, 500)

 
body = Polygon( Point(530,525), Point(530,535), Point(550,555), Point(600,510), Point(615,525), Point(650,525), Point(650,515), Point(623,515), Point(610,500), Point(600,480), Point(580, 480) )

body.setFillColor('black')
paper.add(body)
body.moveTo(540,410)

leg = Polygon(Point(550,545), Point(550,555), Point(570,570), Point(570,610),Point(590,610), Point(590,555), Point(570,540), Point(560,533) )
paper.add(leg)
leg.setFillColor('black')
leg.move(8,-118)




def shake_leg():

    global leg
    for i in range(10):
        leg.rotate(-2)
        sleep(0.001)
    for i in range(10):
        leg.rotate(2)
        sleep(0.001)




def move(x):
    global head
    global body
    global leg
    global bicycle
    global rain1
    
    timeDelay = 0.01
    
    for i in range(100):
        cloud.move(+4,0)
        rain1.move(0,4)
        rain2.move(0,4)
        rain3.move(0,4)
        rain4.move(0,4)
        rain5.move(0,4)
        rain6.move(0,4)
        rain7.move(0,4)
        rain8.move(0,4)
        rain9.move(0,4)
        rain10.move(0,4)
        rain11.move(0,4)
        rain12.move(0,4)
        rain13.move(0,4)
        rain14.move(0,4)
        rain15.move(0,4)
        rain16.move(0,4)
        rain17.move(0,4)
        rain18.move(0,4)
        rain19.move(0,4)
        rain20.move(0,4)
        rain21.move(0,4)
        rain22.move(0,4)
        rain23.move(0,4)
        rain24.move(0,4)
        rain25.move(0,4)
        rain26.move(0,4)
        rain27.move(0,4)
        rain28.move(0,4)
        rain29.move(0,4)
        rain30.move(0,4)
        head.move(4,0)
        body.move(4,0)
        leg.move(4,0)
        bicycle.move(4,0)
        shake_leg()

        sleep(timeDelay)







def draw_E11():

    building = Rectangle(200,400)
    building.setFillColor("white")
    building.setBorderColor("black")
    building.setBorderWidth(10)
    building.move(700,300)
    text1 = Text("E11",30)
    text1.move(650,130)
    
    
    window1 = Square(40)
    window1.setFillColor("black")
    window1.setBorderColor("red")
    window1.setBorderWidth(5)
    window1.move(650,200)
    window2 = Square(40)
    window2.setFillColor("black")
    window2.setBorderColor("red")
    window2.setBorderWidth(5)
    window2.move(650,270)
    window3 = Square(40)
    window3.setFillColor("black")
    window3.setBorderColor("red")
    window3.setBorderWidth(5)
    window3.move(650,340)
    window4 = Square(40)
    window4.setFillColor("black")
    window4.setBorderColor("red")
    window4.setBorderWidth(5)
    window4.move(650,410)
    window5 = Square(40)
    window5.setFillColor("black")
    window5.setBorderColor("red")
    window5.setBorderWidth(5)
    window5.move(750,200)
    window6 = Square(40)
    window6.setFillColor("black")
    window6.setBorderColor("red")
    window6.setBorderWidth(5)
    window6.move(750,270)
    window7 = Square(40)
    window7.setFillColor("black")
    window7.setBorderColor("red")
    window7.setBorderWidth(5)
    window7.move(750,340)
    window8 = Square(40)
    window8.setFillColor("black")
    window8.setBorderColor("red")
    window8.setBorderWidth(5)
    window8.move(750,410)


    
    
    paper.add(building)
    paper.add(text1)
    paper.add(window1)
    paper.add(window2)
    paper.add(window3)
    paper.add(window4)
    paper.add(window5)
    paper.add(window6)
    paper.add(window7)
    paper.add(window8) 
    
    
    
def draw_cloud():
        
    global cloud
    global rains
    global rain1
    global rain2
    global rain3
    global rain4
    global rain5
    global rain6
    global rain7
    global rain8
    global rain9
    global rain10
    global rain11
    global rain12
    global rain13
    global rain14
    global rain15
    global rain16
    global rain17
    global rain18
    global rain19
    global rain20
    global rain21
    global rain22
    global rain23
    global rain24
    global rain25
    global rain26
    global rain27
    global rain28
    global rain29
    global rain30
    
    
    
    cir1 = Circle(40)
    cir1.setFillColor((85,85,85))
    cir1.setBorderColor((85,85,85))
    cir1.move(400,30)
    cir2 = Circle(40)
    cir2.setFillColor((85,85,85))
    cir2.setBorderColor((85,85,85))
    cir2.move(450,30)
    cir3 = Circle(40)
    cir3.setFillColor((85,85,85))
    cir3.setBorderColor((85,85,85))
    cir3.move(500,30)
    cir4 = Circle(40)
    cir4.setFillColor((85,85,85))
    cir4.setBorderColor((85,85,85))
    cir4.move(550,30)
    cir5 = Circle(40)
    cir5.setFillColor((85,85,85))
    cir5.setBorderColor((85,85,85))
    cir5.move(600,30)
    
    cir1.setDepth(-200)
    cir2.setDepth(-200)    
    cir3.setDepth(-200)
    cir4.setDepth(-200)
    cir5.setDepth(-200)
    
    rain1.setFillColor((0,0,150))
    rain1.move(400,100)
    rain2.setFillColor((0,0,150))
    rain2.move(400,300)
    rain3.setFillColor((0,0,150))
    rain3.move(450,200)
    rain4.setFillColor((0,0,150))
    rain4.move(470,320)
    rain5.setFillColor((0,0,150))
    rain5.move(550,250)
    rain6.setFillColor((0,0,150))
    rain6.move(490,150)
    rain6.setFillColor((0,0,150))
    rain6.move(490,150)
    rain7.setFillColor((0,0,150))
    rain7.move(540,120)
    rain8.setFillColor((0,0,150))
    rain8.move(590,220)
    rain9.setFillColor((0,0,150))
    rain9.move(600,100)
    rain10.setFillColor((0,0,150))
    rain10.move(600,100)
    rain11.setFillColor((0,0,150))
    rain11.move(400,-200)
    rain12.setFillColor((0,0,150))
    rain12.move(400,0)
    rain13.setFillColor((0,0,150))
    rain13.move(450,-100)
    rain14.setFillColor((0,0,150))
    rain14.move(470,80)
    rain15.setFillColor((0,0,150))
    rain15.move(550,-50)
    rain16.setFillColor((0,0,150))
    rain16.move(490,-150)

    rain17.setFillColor((0,0,150))
    rain17.move(540,-140)
    rain18.setFillColor((0,0,150))
    rain18.move(590,-80)
    rain19.setFillColor((0,0,150))
    rain19.move(600,-200)

    rain20.move(600,100)
    rain20.setFillColor((0,0,150))
    rain21.move(400,-500)
    rain22.setFillColor((0,0,150))
    rain22.move(400,-300)
    rain23.setFillColor((0,0,150))
    rain23.move(450,-400)
    rain24.setFillColor((0,0,150))
    rain24.move(470,-280)
    rain25.setFillColor((0,0,150))
    rain25.move(550,-450)
    rain26.setFillColor((0,0,150))
    rain26.move(490,-250)

    rain27.setFillColor((0,0,150))
    rain27.move(540,-380)
    rain28.setFillColor((0,0,150))
    rain28.move(590,-380)
    rain29.setFillColor((0,0,150))
    rain29.move(600,-500)
    rain30.setFillColor((0,0,150))
    rain30.move(600,-500)


    cloud.add(cir1)
    cloud.add(cir2)
    cloud.add(cir3)
    cloud.add(cir4)
    cloud.add(cir5)
    cloud.add(rain1)
    cloud.add(rain2)
    cloud.add(rain3)
    cloud.add(rain4)
    cloud.add(rain5)
    cloud.add(rain7)
    cloud.add(rain8) 
    cloud.add(rain9) 
    cloud.add(rain10)
    cloud.add(rain11)
    cloud.add(rain12)
    cloud.add(rain13)
    cloud.add(rain14)
    cloud.add(rain15)
    cloud.add(rain17)
    cloud.add(rain18) 
    cloud.add(rain19) 
    cloud.add(rain20)
    cloud.add(rain21)
    cloud.add(rain22)
    cloud.add(rain23)
    cloud.add(rain24)
    cloud.add(rain25)
    cloud.add(rain27)
    cloud.add(rain28) 
    cloud.add(rain29) 
    cloud.add(rain30)
    
    paper.add(cloud)

    cloud.move(-400,0)
    
    #원은 중심이 원점에 가게 생성됨
    

def draw_animal():
    return





paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')
rectangle = Rectangle(800,200) 
#직사각형은 중심이 원점에 가게 생성됨
rectangle.setFillColor("gray")
rectangle.setDepth(-100)
paper.add(rectangle)
rectangle.move(400,600)
#직사각형을 움직여서 땅을 만듬





draw_E11()
draw_cloud()
draw_animal()


head = Circle(20, Point(638,350))
head.setFillColor('black')
paper.add(head)
head.move(-500,0)
body.move(-500,0)
leg.move(-500,0)
bicycle.move(-500,0)

move(300)



