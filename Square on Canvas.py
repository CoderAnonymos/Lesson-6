import turtle

turtle.Screen().bgcolor("Purple")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("This is TURTLE!!!!!!!!!!")

board = turtle.Turtle()


for i in range(4):
    board.forward(100)
    board.left(90)

    i = i + 1