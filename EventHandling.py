import turtle

# Create screen and turtle
screen = turtle.Screen()
screen.title("Keyboard Controlled Turtle")

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# Movement functions
def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)

# Color change functions
def color_red():
    t.pencolor("red")

def color_blue():
    t.pencolor("blue")

def color_green():
    t.pencolor("green")

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.onkey(color_red, "r")
screen.onkey(color_blue, "b")
screen.onkey(color_green, "g")

# Keep the window open
turtle.done()
