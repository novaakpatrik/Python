import random
import sys

from pygame import display, draw, time, event, KEYDOWN, NOEVENT

screen = display.set_mode([1200, 800])
screen.fill([255, 255, 255])

class Circle(object):

    def __init__(self):
        self.colour = [random.randint(0, 255) for i in range(3)]
        self.center = [random.randint(50, 1150), random.randint(50, 750)]
        self.radius = 10

    def draw(self):
        draw.circle(screen, self.colour, self.center, self.radius, 10)

    def grow(self):
        self.radius = self.radius + 1


circles = []

display.flip()

clock = time.Clock()

while True:
    ev = event.poll()
    if ev.type == KEYDOWN:
        sys.exit(0)

    screen.fill([255, 255, 255])
    for circle in circles:
        circle.draw()
        circle.grow()

    display.flip()

    circles = [c for c in circles if c.radius < 160]

    if len(circles) < 50:
        if random.random() > 0.90 + (len(circles) / 1000.0):
            circles.append(Circle())

    clock.tick(60)
