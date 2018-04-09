from cs1graphics import *
from time import *
import math

canvas = Canvas(400,550)
canvas.setBackgroundColor("white")
canvas.setTitle("CS101 Drawing exercise")
body = Circle(180)
body.setFillColor("white")
body.setBorderColor("black")
body.setBorderWidth(5)
body.moveTo(200,350)
canvas.add(body)
center = Circle(5)

center.setFillColor("white")
center.setBorderColor("black")
center.setBorderWidth(2)
center.moveTo(200,350)
canvas.add(center)

h_n = Rectangle(5,160)
m_n = Rectangle(3,120)
s_n = Rectangle(3,100)
h_n.setFillColor("black")
h_n.setBorderWidth(0)
m_n.setFillColor("black")
m_n.setBorderWidth(0)
s_n.setFillColor("red")
s_n.setBorderWidth(0)
door_1 = Rectangle(150,150)
door_1.setFillColor("yellow")
door_1.setBorderColor("black")
door_1.setBorderWidth(3)

door_1.moveTo(125,85)
door_2 = Rectangle(150,150)
door_2.setFillColor("yellow")
door_2.setBorderColor("black")
door_2.setBorderWidth(3)

door_2.moveTo(275,85)
door = Layer()
door.add(door_1)
door.add(door_2)
canvas.add(door)
#am_pm_1 = Text("AM",20)
#am_pm_1.moveTo(200,300)
#am_pm_2 = Text("AM",20)
#am_pm_2.moveTo(200,300)
clock = Layer()
clock.add(h_n)
clock.add(m_n)
clock.add(s_n)
current_am = 0 
am_pm = 0
animal_flag = 0
b_head = Layer()
b_body = Layer()
bird = Layer()
step = 0
#beak_upper = Poly(Point(),)
#beak_lower = Poly(Point())

for i in range(12) :
    if i==0 :
        text = Text("12",20)
    else :
        text = Text("%d"%i,20)
    text.moveTo(200+160*math.sin((math.pi*i)/6),350-160*math.cos((math.pi*i)/6))
    canvas.add(text)

current_angle = (0,0,0)


    
def draw_animal(time) :
    global bird
    global b_head
    global step
    head = Circle(30,Point(0,0))
    head.setFillColor('Brown')
    head.setBorderColor('Black')
    head.setDepth(40)
    bird.add(head)

    eye1 = Circle(8, Point(-14,-6))
    eye1.setFillColor('Black')
    eye1.setBorderColor('Black')
    eye1.setDepth(30)
    bird.add(eye1)
    
    eye2 = Circle(8, Point(14,-6))
    eye2.setFillColor('Black')
    eye2.setBorderColor('Black')
    eye2.setDepth(30)
    bird.add(eye2)
    
    beak1 = Polygon(Point(0,5), Point(-20,13), Point(20,13))
    beak1.setFillColor('Yellow')
    beak1.setBorderColor('Black')
    beak1.setDepth(20)
    bird.add(beak1)
    
    beak2 = Polygon(Point(-20,15), Point(20,15), Point(0,23))
    beak2.setFillColor('Yellow')
    beak2.setBorderColor('Black')
    beak2.setDepth(20)
    bird.add(beak2)
    
    global b_body
    body = Polygon(Point(-20,88),Point(20,88),Point(30,48),Point(20,8),Point(-20,8),Point(-30,48))
    body.setFillColor('Brown')
    body.setBorderColor('Black')
    body.setBorderWidth(5)
    body.setDepth(50)
    bird.add(body)
    
    
    if time[2]%6 < 3 :
        wing1 = Rectangle(40,30,Point(40,48))
        wing1.setFillColor("white")
        wing1.setBorderColor("black")
        wing1.setBorderWidth(5)
        wing1.setDepth(60)
        bird.add(wing1)
        wing2 = Rectangle(40,30,Point(-40,48))
        wing2.setFillColor("white")
        wing2.setBorderColor("black")
        wing2.setBorderWidth(5)
        wing2.setDepth(60)
        bird.add(wing2)
        bird.moveTo(200,30)
        
        canvas.add(bird)
        wing1.rotate(-45)
        wing2.rotate(45)
        sleep(0.5)
        # bird.remove(wing1)
        # bird.remove(wing2)
        # canvas.remove(bird)
        # canvas.add(bird)
        wing1.rotate(45)
        wing2.rotate(-45)
        # sleep(0.5)
        bird.remove(wing1)
        bird.remove(wing2)
        canvas.remove(bird)
        
        
        
        
    
def toRad(angle) :
    return angle*math.pi/180
    
def animate_clock(time) :
    global canvas
    global time_int
    global h_n
    global m_n
    global s_n
    global current_angle
    global current_am
    global clock
    global am_pm
    h = time[0]
    m = time[1]
    s = time[2]

    am = 0
    if h//12 == 1 :
        am = "PM"
    else :
        am = "AM"
    h_angle = (h%12)*30+m*0.5
    m_angle = m*6+s*0.1
    s_angle = s*6
    h_n.moveTo(200+70*math.sin(toRad(h_angle)),350-70*math.cos(toRad(h_angle)))
    h_n.rotate(h_angle-current_angle[0])
    m_n.moveTo(200+50*math.sin(toRad(m_angle)),350-50*math.cos(toRad(m_angle)))
    m_n.rotate(m_angle-current_angle[1])
    s_n.moveTo(200+40*math.sin(toRad(s_angle)),350-40*math.cos(toRad(s_angle)))
    s_n.rotate(s_angle-current_angle[2]) 
    if am != current_am :
        clock.remove(am_pm)
        am_pm = Text(am,30)
        am_pm.moveTo(200,300)
        clock.add(am_pm)
    current_am = am
    current_angle = (h_angle,m_angle,s_angle)


def main() :
    global canvas
    global clock
    global current_angle
    global am_pm
    global current_am
    global animal_flag
    now = gmtime(time())
    current_time = (now.tm_hour, now.tm_min, now.tm_sec)
    if now.tm_hour//12 == 1:
        current_am = "PM"
    else :
        current_am = "AM"
    am_pm = Text(current_am,30)
    am_pm.moveTo(200,300)
    clock.add(am_pm)
    canvas.add(clock)
    while True :
        now = gmtime(time())
        time_now = (now.tm_hour, now.tm_min, now.tm_sec)
        animate_clock(time_now)
        draw_animal(time_now)
        

def main2() :
    global canvas
    draw_animal(100)
main()