# Drawing

This `package` contains several modules full of useful (or amusing) functions. Here's a description:

## shapes

The `shapes` module contains functions which draw some fancy shapes. Enjoy!

### star
`star` takes three arguments: `inner_radius`, `outer_radius`, and `number_of_points`. Then it draws the 

## lines

The `lines` module contains helpers that change how the turtle draws. Each of these is a context manager, 
which means that it changes the behavior of the code block which follows it. Think of these as temporarily
changing the rules of the world. 

### dashes()
Causes the turtle to draw dashes. For example: 

    from drawing.lines import dashes
    from turtle import forward, pensize

    pensize(4)
    with dashes():
        for side in range(4):
            forward(100)
            right(90)

You may also call dashes with an optional spacing argument, like `with dashes(spacing=3)`.

### dots
Causes the turtle to draw dots. For example:

    from drawing.lines import dots

    with dots():
        for i in range(100):
            forward(i)
            right(20)

You may also call dots with an optional spacing argument, like `with dots(spacing=25)`.

### rainbow
Causes the turtle to draw in rainbow colors. For example:

    from drawing.lines import rainbow
    from turtle import circle, pensize, position, penup, pendown

    pensize(10)
    with rainbow():
        for i in range(10, 100, 10):
            circle(i)
            penup()
            x, y = position()
            sety(y - 10)
            pendown()

You may also call `rainbow` with an optional spacing argument and/or an optional colors argument, 
like `with rainbow(spacing=25, colors=["red", "green", "blue"])`.

## speed

The `speed` module contains a helper to speed up the turtle.

### `no_delay`

`no_delay` causes a code block to run instantly. Like the functions in `lines`, `no_delay`
is a context manager which changes how a code block runs. For example: 

    from turtle import forward, right
    from drawing.speed import no_delay

    with no_delay():
        for i in range(10000):
            forward(100)
            right(180.1)
