import turtle as tu

# Initialize the turtle and screen
turtle = tu.Turtle()
screen = tu.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree Pattern")

# Set initial turtle properties
turtle.left(90)
turtle.speed(10)

def draw_fractal(length, color, pen_size):
    """
    Draws a fractal tree with the given length, color, and pen size.
    """
    if length < 10:
        return
    else:
        turtle.pensize(pen_size)
        turtle.pencolor(color)
        turtle.forward(length)
        turtle.left(30)
        draw_fractal(3 * length / 4, color, pen_size)
        turtle.right(60)
        draw_fractal(3 * length / 4, color, pen_size)
        turtle.left(30)
        turtle.backward(length)

def draw_tree():
    """
    Draw multiple fractal trees with varying colors and sizes.
    """
    # Parameters for different fractal trees
    trees = [
        (20, "yellow", 2),
        (20, "magenta", 2),
        (20, "red", 2),
        (20, "#FFF8DC", 2),
        (40, "lightgreen", 3),
        (40, "red", 3),
        (40, "yellow", 3),
        (40, "#FFF8DC", 3),
        (60, "cyan", 2),
        (60, "yellow", 2),
        (60, "magenta", 2),
        (60, "#FFF8DC", 2)
    ]

    for length, color, pen_size in trees:
        draw_fractal(length, color, pen_size)
        turtle.right(90)
        turtle.speed(10)

# Draw the fractal trees
draw_tree()

# Close the window on click
screen.exitonclick()
