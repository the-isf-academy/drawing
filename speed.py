# speed.py
# by Chris Proctor
# Helper functions that affect the turtle's speed

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

from turtle import tracer, delay, update

class no_delay:
    "A context manager which causes drawing code to run instantly"

    def __enter__(self):
        self.n = tracer()
        self.delay = delay()
        tracer(0, 0)

    def __exit__(self, exc_type, exc_value, traceback):
        update()
        tracer(self.n, self.delay)

if __name__ == '__main__':
    from turtle import forward, right

    with no_delay():
        for i in range(10000):
            forward(300)
            right(181)
    input("That was fast!")
