import turtle
import pickle

def draw_bag():
    turtle.shape("turtle")
    turtle.pen(pencolor="brown", pensize=5)
    turtle.penup()
    turtle.goto(-35, 35)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)

def escaped(position):
    x = int(position[0])
    y = int(position[1])
    return x < -35 or x > 35 or y < -35 or y > 35

def draw_line():
    angle = 0
    step = 5
    t = turtle.Turtle()
    while not escaped(t.position()):
        t.left(angle)
        t.forward(step)

def draw_squares_until_escaped():
    t = turtle.Turtle()
    L = draw_squares()
    with open("data_square", "w") as f:
        pickle.dump(L, f)

def draw_squares():
    t = turtle.Turtle()
    L = []
    i = 1
    while not escaped(t.position()):
        t.penup()
        t.goto(-i, -i)
        t.pendown()
        L.extend(draw_square(t, i*2))
        i += 1
    return L

def draw_square(t, size):
    L = []
    for i in range(4):
        t.forward(size)
        t.left(90)
        store_position_data(L, t)
    return L

def store_position_data(L, t):
    position = t.position()
    L.append([position[0], position[1], escaped(position)])

if __name__ == "__main__":
    turtle.setworldcoordinates(-70, -70, 70, 70)
    draw_bag()
    draw_line()
    draw_squares_until_escaped()
    turtle.mainloop()
