#정사각형을 그려보자
import turtle

turtle.shape("turtle")

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)

# 반복문 사용해서
for i in range(4):
    #turtle.write(turtle.position())
    turtle.forward(100)
    turtle.right(90)

turtle.done()