from turtle import *

#we want to paint a house

width(5)
speed(30)
begin_fill()
color("green")
forward(200)
left(90)

forward(200)  
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

forward(70)
color("red")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end the door

penup()
goto(200,200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200) #height OF the roof
left(120)
forward(200)
end_fill()
#end the roof

#drawing a window
left(30)
color("black")
begin_fill()
penup()
goto(0,130)
pendown()


left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()
#end the one window

#drawing a second window

penup()
goto(200,200)

forward(15)
color("black")
begin_fill()
forward(55)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()
pendown()
#end a second window



exitonclick()
