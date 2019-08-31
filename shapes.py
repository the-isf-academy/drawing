# shapes.py
# by Chris Proctor
# Functions which draw fancy shapes

# =============================================================================
# ! Advanced !
# =============================================================================
# This module contains some fancy code that we don't expect you to understand 
# yet. That's ok--as long as we know how to use code, we don't have to 
# understand everything about it. (Do you understand everything about 
# MacOS?) Check out the README for documentation on how to use this code. 

# Of course, if you want to dig into this module, feel free. You can ask a 
# teacher about it if you're interested. 
# =============================================================================

from turtle import *
from math import sin, cos, tau

def fly(x, y):
    penup()
    goto(x, y)
    pendown()

def star(inner_radius, outer_radius, number_of_points):
    "Draws a star with `number_of_points`"
    x_origin, y_origin = position()
    fly(x_origin, y_origin + inner_radius)
    for point in range(number_of_points):
        goto(
            x_origin + inner_radius * sin(tau * (point / number_of_points)), 
            y_origin + inner_radius * cos(tau * (point / number_of_points))
        )
        goto(
            x_origin + outer_radius * sin(tau * ((point + 0.5) / number_of_points)), 
            y_origin + outer_radius * cos(tau * ((point + 0.5) / number_of_points))
        )
    goto(x_origin, y_origin + inner_radius)
    fly(x_origin, y_origin)

if __name__ == '__main__':
    star(50, 80, 7)
    input("OK")


