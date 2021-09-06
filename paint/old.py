from swampy.TurtleWorld import Turtle, TurtleWorld, fd, rt

import math
import time


world = TurtleWorld()
bob = Turtle()
bob.set_delay(0.1)

circum = lambda r: 2 * math.pi * r
square = lambda turtle, w, h: list(map(lambda s: [fd(turtle, s), rt(turtle)], [w, h, w, h]))
poly = lambda turtle, n, face_l, a=360: list(map(lambda i: [fd(turtle, face_l), rt(turtle, a / n)], range(n)))
circle = lambda turtle, rad: poly(turtle, 30, (circum(rad)/180) * 2)
arc = lambda turtle, rad, angle: poly(turtle, 30, (circum(rad)/180) * 2, a=angle)
plot = lambda turtle, func, steps, siz: list(map(lambda x: [fd(turtle, siz), lt(turtle), fd(turtle, func(x)), rt(turtle)],range(steps)))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

R =  100

square(bob, R, R)
circle(bob, R)

bob.x += R

arc(bob, R, 180)

time.sleep(3)

world.clear()

bob = Turtle()

bob.x = 0
plot(bob, lambda x: (math.cos(x) * math.pi * 2) * 6, 150, 2)

wait_for_user()
