import turtle
t=turtle.Turtle()
t.pencolor("red")
t.speed(2)
s=turtle.Screen()
s.bgcolor("black")

for i in range(4):
    t.forward(100)
    t.left(90)
    
t.penup()
t.goto(50 ,50)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)
   
t.penup()
t.goto(0,100)
t.pendown()
t.goto(50,150)

t.penup()
t.goto(0,0)
t.pendown()
t.goto(50,50)

t.penup()
t.goto(100,0)
t.pendown()
t.goto(150,50)

t.penup()
t.goto(100,100)
t.pendown()
t.goto(150,150)
  


#My first 3D drawing 
    