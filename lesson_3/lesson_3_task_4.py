from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

def draw_circle(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
def draw_head():
    my_turtle.penup()
    my_turtle.goto(0, 100)
    my_turtle.pendown()
    draw_circle(my_turtle, 50, "green")
def draw_body():
    my_turtle.penup()
    my_turtle.goto(0, -50)
    my_turtle.pendown()
    draw_circle(my_turtle, 100, "darkgreen")
def draw_legs():
    positions = [(-70, -70), (70, -70), (-70, -150), (70, -150)]
    for pos in positions:
        my_turtle.penup()
        my_turtle.goto(pos)
        my_turtle.pendown()
        draw_circle(my_turtle, 30, "green")
def draw_eyes():
    eye_positions = [(-20, 130), (20, 130)]
    for pos in eye_positions:
        my_turtle.penup()
        my_turtle.goto(pos)
        my_turtle.pendown()
        draw_circle(my_turtle, 10, "white")
        my_turtle.penup()
        my_turtle.goto(pos[0], pos[1] + 5)
        my_turtle.pendown()
        draw_circle(my_turtle, 5, "black")
    draw_head()
draw_body()
draw_legs()
draw_eyes()
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()



    

