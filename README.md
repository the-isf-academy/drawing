# Drawing

This `package` contains several modules full of useful (or amusing) functions. Here's a description:

## shapes

The `shapes` module contains functions which draw some fancy shapes. Enjoy!

### `block_a(height)`
Draws the letter A with the given height, and returns the width of the letter.

### `block_b(height)`
Draws the letter B with the given height, and returns the width of the letter.

### `block_c(height)`
Draws the letter C with the given height, and returns the width of the letter.

Using these letter functions, you can spell out words (It would be nice to have more letters!): 

    :::python
    height = 100
    kerning = 10
    for letter_function in [block_a, block_b, block_c]:
        spacing = letter_function(height)
        penup()
        forward(spacing + kerning)
        pendown()

### `fancy_star(inner_radius, outer_radius, number_of_points)`
`fancy_star` takes three arguments: `inner_radius`, `outer_radius`, and `number_of_points`. Then it draws
a zig-zag between points on an inner and outer circle.

### `square_with_points(size)`
Works just like a regular square, but returns a list of the vertices. For example, 

    >>> points = square_with_points(100)
    >>> points
    [(-0.00,-0.00), (100.00,0.00), (100.00,-100.00), (0.00,-100.00)]

### `add_perspective(points, origin, depth)`
Projects `points` toward `origin`, creating the perception of depth. `depth` should be a number between 
0 and 1, indicating how much of the distance between each point and `origin` the perspective line should draw.
Here's an example:

    for x in range(-200, 200, 50):
        fly(x, 0)
        points = square_with_points(30)
        add_perspective(points, [0, 100], 0.3)

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
