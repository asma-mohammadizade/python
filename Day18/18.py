# Hirst Painting


import colorgram
import turtle as t
import random



timmy = t.Turtle()
screen = t.Screen()
screen.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()





# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


rgb_colors = [(253, 252, 250), (246, 253, 252), (249, 240, 243), (126, 161, 203), (214, 232, 246), (250, 208, 85), (133, 192, 175), (17, 62, 122), (141, 32, 24), (7, 110, 87), (163, 23, 29), (14, 51, 97), (233, 174, 115), (47, 82, 127), (29, 116, 97), (159, 206, 192), (144, 61, 55), (161, 51, 56), (96, 26, 17), (180, 185, 213), (203, 138, 145), (113, 123, 159), (171, 105, 100), (226, 173, 169), (233, 169, 174), (180, 97, 102), (89, 148, 135), (101, 17, 21), (160, 203, 219), (4, 78, 61)]
timmy.setheading(225)
timmy.forward(350)
timmy.setheading(0)

num_dots = 100

for move in range(1, num_dots + 1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)
    if move % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)




















screen.exitonclick()










