from cs1graphics import *
from time import sleep

paper=Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(500)
paper.setHeight(500)
paper.setTitle('Dog')

dog=Layer()

# �� �Ӹ�
head=Circle(30)
head.setFillColor('white')
head.moveTo(100,350)
dog.add(head)

#�� ��
ear=Polygon(Point(0,0),Point(16,0),Point(8,22))
ear.rotate(150)
ear.setFillColor('white')
ear.moveTo(100,330)
dog.add(ear)



#�� ��

eye=Circle(3)
eye.setFillColor('black')
eye.moveTo(120,340)
dog.add(eye)
#�� ����
body=Rectangle(100,50)
body.setFillColor('white')
body.moveTo(60,400)
dog.add(body)

#�� �޴ٸ�1
leg1=Rectangle(60,10)
leg1.setFillColor('white')
leg1.moveTo(20,450)
leg1.rotate(90)
dog.add(leg1)

#�� �޴ٸ�2

leg3=Rectangle(60,10)
leg3.setFillColor('white')
leg3.setBorderColor('black')
leg3.moveTo(25,450)
leg3.rotate(90)
dog.add(leg3)

#�� �մٸ�1
leg2=Rectangle(60,10)
leg2.setFillColor('white')
leg2.moveTo(100,450)
leg2.rotate(90)
dog.add(leg2)

#�� �մٸ�2
leg4=Rectangle(60,10)
leg4.setFillColor('white')
leg4.setBorderColor('black')
leg4.moveTo(105,450)
leg4.rotate(90)
dog.add(leg4)

#�ٸ� ȸ���� �ٲ�
leg1.adjustReference(0,-30)
leg2.adjustReference(0,-30)
leg3.adjustReference(0,-30)
leg4.adjustReference(0,-30)

#����
tail=Rectangle(60,12)
tail.setFillColor('white')
tail.moveTo(-5, 360)
tail.rotate(45)
dog.add(tail)




#���
paper.add(dog)


def moving():
    leg1.rotate(-45)
    leg3.rotate(-45)
    leg2.rotate(45)
    leg4.rotate(45)
    for i in range(10):
        sleep(0.2)
        leg1.rotate(90)
        leg3.rotate(90)
        
        leg2.rotate(-90)
        leg4.rotate(-90)
        dog.move(50,0)
        sleep(0.2)
        leg1.rotate(-90)
        leg3.rotate(-90)
        leg2.rotate(90)
        leg4.rotate(90)
    



moving()


