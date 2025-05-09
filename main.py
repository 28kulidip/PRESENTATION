import turtle
screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("lightpink")
t = turtle.Turtle()
t.speed(0)
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()


#slide 1
#rectangle

t.fillcolor("black")
t.begin_fill()
t.penup()
t.goto(-30,130)
t.pendown()
t.forward(55)
t.left(90)
t.forward(35)
t.left(90)
t.forward(55)
t.left(90)
t.forward(35)
t.left(90)
t.end_fill()

t.pencolor("magenta")
t.penup()
t.goto(0,7)
t.pendown()
t.write(("All About Me:"),font=("Arial",30,"bold"),align="center")
t.penup()
t.goto(0,-40)
t.pendown()
t.write(("Polina Kulidi"),font=("Arial",30,"bold"),align="center")

t.pencolor('blue')
t.penup()
t.goto(-20,250)
t.write("Click Enter for next slide", font=("arial", 25, "bold italic"), align="center")
t.pendown()

t.penup()
t.goto(0,-120)
t.pendown()
screen.addshape('14.gif')
t.shape('14.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0,-280)
t.pendown()
screen.addshape('beach.gif')
t.shape('beach.gif')
t.stamp()
t.shape('classic')

round = input("press enter to continue:")

t.clear()
t.hideturtle()

screen.bgcolor('skyblue')

#slide 2
#circle

t2.fillcolor("red")
t2.begin_fill()
t2.penup()
t2.goto(0,130)
t2.pendown()
t2.circle(40)
t2.end_fill()

t2.pencolor('blue')
t2.penup()
t2.goto(-20,250)
t2.write("Click Enter for next slide", font=("arial", 25, "bold italic"), align="center")
t2.pendown()

t2.penup()
t2.goto(0,75)
t2.pendown()
t2.write(("Favorite food: "),font=("Arial",30,"bold"),align="center")
t2.penup()
t2.goto(0,34)
t2.pendown()
t2.write(("1. French fries"),font=("Arial",30,"bold"),align="center")
t2.penup()
t2.goto(0,-20)
t2.pendown()
t2.write(("2. Pizza"),font=("Arial",30,"bold"),align="center")
t2.penup()
t2.goto(0,-225)
t2.pendown()
t2.write(("3. Steak"),font=("Arial",30,"bold"),align="center")

t2.penup()
t2.goto(0,-100)
t2.pendown()
screen.addshape('pizza.gif')
t2.shape('pizza.gif')
t2.stamp()
t2.shape('classic')

t2.penup()
t2.goto(0,-300)
t2.pendown()
screen.addshape('steak.gif')
t2.shape('steak.gif')
t2.stamp()
t2.shape('classic')

round = input("press enter to continue:")

t2.clear()
t2.hideturtle()

screen.bgcolor('lightgreen')

#slide 3
#square

t3.fillcolor("purple")
t3.begin_fill()
t3.penup()
t3.goto(-30,130)
t3.pendown()
t3.forward(55)
t3.left(90)
t3.forward(55)
t3.left(90)
t3.forward(55)
t3.left(90)
t3.forward(55)
t3.left(90)
t3.end_fill()

t3.pencolor('blue')
t3.penup()
t3.goto(-20,250)
t3.write("Click Enter for next slide", font=("arial", 25, "bold italic"), align="center")
t3.pendown()

t3.penup()
t3.goto(0,50)
t3.pendown()
t3.write(("Hobbies: "),font=("Arial",30,"bold"),align="center")
t3.penup()
t3.goto(0,0)
t3.pendown()
t3.write(("1. Tennis"),font=("Arial",30,"bold"),align="center")
t3.penup()
t3.goto(0,-40)
t3.pendown()
t3.write(("2. Baking"),font=("Arial",30,"bold"),align="center")
t3.penup()
t3.goto(0,-80)
t3.pendown()
t3.write(("3. Watching movies"),font=("Arial",30,"bold"),align="center")
t3.penup()
t3.goto(0,-120)
t3.pendown()
t3.write(("4. Taking walks"),font=("Arial",30,"bold"),align="center")

t3.penup()
t3.goto(0,-200)
t3.pendown()
screen.addshape('tennis.gif')
t3.shape('tennis.gif')
t3.stamp()
t3.shape('classic')

t3.penup()
t3.goto(0,-325)
t3.pendown()
screen.addshape('baking.gif')
t3.shape('baking.gif')
t3.stamp()
t3.shape('classic')


round = input("press enter to continue:")

t3.clear()
t3.hideturtle()
screen.screensize(500,500)
screen.bgcolor('yellow')

#slide 4
#triangle

t4.fillcolor("green")
t4.begin_fill()
t4.penup()
t4.goto(-25,130)
t4.pendown()
t4.goto(25,130)
t4.left(135)
t4.goto(0,155)
t4.left(135)
t4.goto(-25,130)
t4.end_fill()


t4.pencolor('blue')
t4.penup()
t4.goto(-20,250)
t4.write("Click Enter for next slide", font=("arial", 25, "bold italic"), align="center")
t4.pendown()

t4.penup()
t4.goto(0,50)
t4.pendown()
t4.write(("Favorite movies: "),font=("Arial",30,"bold"),align="center")
t4.penup()
t4.goto(0,0)
t4.pendown()
t4.write(("1. Home Alone"),font=("Arial",30,"bold"),align="center")
t4.penup()
t4.goto(0,-40)
t4.pendown()
t4.write(("2. The Summer I Turned Pretty"),font=("Arial",30,"bold"),align="center")

t4.penup()
t4.goto(0,-120)
t4.pendown()
screen.addshape('ha.gif')
t4.shape('ha.gif')
t4.stamp()
t4.shape('classic')

t4.penup()
t4.goto(0,-280)
t4.pendown()
screen.addshape('tsi.gif')
t4.shape('tsi.gif')
t4.stamp()
t4.shape('classic')

round = input("press enter to continue:")

t4.clear()
t4.hideturtle()
screen.screensize(500,500)
screen.bgcolor('purple')

#slide 5
#random shape

t5.fillcolor("orange")
t5.begin_fill()
t5.penup()
t5.goto(-25,150)
t5.pendown()
t5.goto(0,130)
t5.goto(25,150)
t5.goto(0,170)
t5.goto(-25,150)
t5.end_fill()

t5.penup()
t5.goto(0,50)
t5.pendown()
t5.write(("Favorite sports: "),font=("Arial",30,"bold"),align="center")
t5.penup()
t5.goto(0,0)
t5.pendown()
t5.write(("1. Tennis"),font=("Arial",30,"bold"),align="center")
t5.penup()
t5.goto(0,-40)
t5.pendown()
t5.write(("2. Volleyball"),font=("Arial",30,"bold"),align="center")

t5.penup()
t5.goto(0,-120)
t5.pendown()
screen.addshape('tennis2.gif')
t5.shape('tennis2.gif')
t5.stamp()
t5.shape('classic')

t5.penup()
t5.goto(0,-280)
t5.pendown()
screen.addshape('volleyball.gif')
t5.shape('volleyball.gif')
t5.stamp()
t5.shape('classic')

t5.hideturtle()








turtle.done()