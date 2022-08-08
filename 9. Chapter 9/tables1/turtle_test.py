# import turtle
# ninja=turtle.Turtle()
# ninja.speed(10)


# for i in range(200):
#     ninja.forward(10)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)


#     ninja.penup()
#     ninja.setposition
#     ninja.pendown()


#     ninja.right(2)

# turtle.done()

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)