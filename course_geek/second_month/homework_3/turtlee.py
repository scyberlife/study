import turtle

tt=turtle.Turtle()
turtle.bgcolor("orange")
tt.pencolor("black")
tt.speed(0.5)
tt.penup()
tt.goto(0,200)
tt.pendown()
forDis=0
dR=5

while(True):
    tt.forward(forDis)
    tt.right(dR)
    forDis+=3
    dR+=1
    if dR==210:
        break
    tt.hideturtle()
turtle.done()
turtle.exitonclick()