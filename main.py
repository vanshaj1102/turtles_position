from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

tim.forward(25)

def move_forward():
    tim.forward(20)  # Move forward by 20 pixels

def move_backward():
    tim.backward(20)
    # Move backward by 20 pixels
def turn_clockwise():
    tim.right(15)  # Turn right (clockwise) by 15 degrees

def turn_counterclockwise():
    tim.left(15)  #

def clear_screen():
    tim.clear()  # Clear the turtle drawings
    tim.penup()
    tim.home()  # Reset position to the center
    tim.pendown()
# Listen for keyboard input
screen.listen()
screen.onkey(move_forward, "w")  # Move forward on 'W' key press
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "a")
screen.onkey(turn_counterclockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
