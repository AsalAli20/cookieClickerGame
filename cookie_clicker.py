import turtle
# to name and give it a background and then dispaly on screen
wn = turtle.Screen()
wn.title("Cookie Clicker by @Asal")
wn.bgcolor("black")

wn.register_shape("cookie.gif")

# to create the cookie i'll make turtle object
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 150)
pen.write(f"Clicks:{clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x,y):
    global clicks
    clicks +=1
    pen.clear()
    pen.write(f"Clicks:{clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)
wn.mainloop()
