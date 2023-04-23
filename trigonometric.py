#Import necessary modules and packages
from equation import Equation
import turtle
import constants as ct

#Create a Trigonometric class that inherits from Equation class
class Trigonometric(Equation):
    def __init__(self):
        super().__init__()

    # Define a method to draw the equation graph
    def draw(self, a, c, type):
        # Open a turtle graphics screen
        self.open_screen()
        # Draw the coordinate plane
        self.draw_plane(enumerate=True)
        # Write the equation on the screen
        self.write_equation(a, c, 'sin')

        # Show the turtle on the screen and set its color to red
        self.turtle.showturtle()
        self.turtle.pencolor('red')

        # Iterate through the x values and calculate the corresponding y values for the graph
        for x in self.x_range:
            x = float(x) / self.precision
            y = a * type(x) + c

            # Move the turtle to the calculated (x, y) position and draw a line
            self.turtle.goto(x, y)
            self.turtle.pendown()

        # Hide the turtle and wait for a click to exit the screen
        self.turtle.hideturtle()
        self.screen.exitonclick()

    # Define a method to write the equation on the screen
    def write_equation(self, a, c, type):
        # Save the current turtle position and move it to the position to write the equation
        temp = self.turtle.position()
        self.turtle.penup()
        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        self.turtle.setposition(equation_pos)
        # Write the equation on the screen
        self.turtle.write(f'y = {a}{type}(x) + {c}')
        # Return the turtle to the saved position
        self.turtle.setposition(temp)