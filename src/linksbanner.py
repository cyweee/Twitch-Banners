import turtle
import os
from montserrat_font import font_mon

base_dir = os.path.dirname(__file__)
font_path = os.path.join(base_dir, r"C:\Users\qqqqq\twitchBanners\Twitch-Banners\font\Montserrat\montserrat.ttf")

screen = turtle.Screen()
screen.bgcolor("black")

my_font = font_mon(screen._root, "Montserrat", 36, font_path)

pen = turtle.Turtle()
pen.color("purple")
pen.pensize(3)
pen.penup()

pen.goto(0, 40)
pen.pendown()
pen.write("Links", align="center", font=("Montserrat", 36, "bold"))

pen.hideturtle()
screen.exitonclick()
