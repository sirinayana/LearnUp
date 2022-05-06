import turtle

turtle.speed(0)


def figure(n, side, color):
    s = 180 - 180 * (n - 2) / n
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(side)
        turtle.right(s)
    turtle.end_fill()


turtle.up()
turtle.goto(0, 100)
figure(20, 50, 'midnight blue')
turtle.goto(3, 94)
figure(20, 45, 'navy')
turtle.goto(6, 88)
figure(20, 40, 'dark slate blue')

turtle.goto(-50, -60)
turtle.fillcolor('white')
turtle.begin_fill()
turtle.color('white')
turtle.write('CODE', font=('Arial', 40))
turtle.end_fill()

turtle.exitonclick()
