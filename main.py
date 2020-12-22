"""import colorgram

colors = colorgram.extract("painting.jpg", 30)

rgb_colors = []

for color in colors:
    new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(new_color)

print(rgb_colors)"""

from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)

color_list = [
    (194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115),
    (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104),
    (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182),
    (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15)
    ]

my_turtle = Turtle()
my_screen = Screen()

my_screen.title("My Hirst Painting")
my_turtle.shape("classic")
my_turtle.color("dark blue")

my_turtle.penup()

x = -230
y = -230
for n in range(10):
    my_turtle.speed("fastest")
    my_turtle.setposition(x, y)
    for i in range(10):
        my_turtle.speed("slow")
        current_color = choice(color_list)
        my_turtle.dot(20, current_color)
        if i < 9:
            my_turtle.fd(50)
    y += 50
    if n == 9:
        my_turtle.speed("fastest")
        my_turtle.home()

my_screen.exitonclick()
