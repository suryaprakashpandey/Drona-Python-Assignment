from turtle import *

screen = Screen()
screen.title("Drona Python Assignment Q1: Simulated Drone Movement System")
screen.bgcolor("lightblue")
screen.addshape("drone.gif")

drone = Turtle()
drone.shape("drone.gif")
drone.penup()
drone.left(90)

left_end = -200
right_end = 200
top_end = 200
bottom_end = -200

border = Turtle()
border.hideturtle()
border.penup()
border.speed(10)
border.pensize(3)

border.goto(left_end, top_end)
border.pendown()
border.goto(right_end, top_end)
border.goto(right_end, bottom_end)
border.goto(left_end, bottom_end)
border.goto(left_end, top_end)


# Logic to move forward
w_pressed = False

def move_forward():
    global w_pressed
    w_pressed = True
    while w_pressed and drone.ycor() < top_end - 30:
        drone.forward(2)

def stop_forward():
    global w_pressed
    w_pressed = False

screen.onkeypress(move_forward, "w")
screen.onkeyrelease(stop_forward, "w")


# Logic to move backward
s_pressed = False

def move_backward():
    global s_pressed
    s_pressed = True
    while s_pressed and drone.ycor() > bottom_end + 30:
        drone.backward(2)

def stop_backward():
    global s_pressed
    s_pressed = False

screen.onkeypress(move_backward, "s")
screen.onkeyrelease(stop_backward, "s")


# Logic to move left
a_pressed = False

def move_left():
    global a_pressed
    a_pressed = True
    while a_pressed and drone.xcor() > left_end + 30:
        drone.setx(drone.xcor() - 2)

def stop_left():
    global a_pressed
    a_pressed = False

screen.onkeypress(move_left, "a")
screen.onkeyrelease(stop_left, "a")


# Logic to move right
d_pressed = False

def move_right():
    global d_pressed
    d_pressed = True
    while d_pressed and drone.xcor() < right_end - 30:
        drone.setx(drone.xcor() + 2)

def stop_right():
    global d_pressed
    d_pressed = False

screen.onkeypress(move_right, "d")
screen.onkeyrelease(stop_right, "d")

note = Turtle()
note.hideturtle()
note.penup()
note.color("black")
note.goto(0, 250)
note.write("Use 'W' to move forward, 'S' to move backward, 'A' to move left, 'D' to move right !", align="center", font=("Arial", 13, "bold"))

screen.listen()
mainloop()
