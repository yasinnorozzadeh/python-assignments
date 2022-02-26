import turtle
import time
t=turtle.Pen()
azlaa = 3
t.shape("turtle")
t.speed(100000)
turtle.bgcolor("red")
adad1 = 0
adad2 = 0
a = 50
t.goto(-adad1 , -adad2)
while not azlaa == 11:
    for i in range (azlaa):
        t.left(360 / azlaa)
        t.forward(a)
    azlaa += 1
    time.sleep(1)
    t.penup()
    adad1 += 5
    adad2 -= 18
    t.goto(adad1 , adad2)
    t.pendown()
    a += 15
