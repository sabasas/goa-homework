#Turtle ბიბლიოთეკის დახმარებით დახატეთ ფასანაურული ხინკალი

from turtle import *
#we want to paint  fasanauruli khinkali
speed(80)
width(3)

forward(200)
color("gray")
begin_fill()
left(810)
circle(170,50)
right(770)

forward(40)
left(810)
forward(70)
left(810)

forward(40)
right(810)
circle(10,50)          #heigt of fasanauruli khinkali
forward(100)

left(760)
forward(50)
left(810)
forward(10)
right(810)
end_fill()

color("black")
penup()
goto(100,100)
pendown()
forward(70)

penup()
goto(70,100)
pendown()
left(320)
forward(70)

penup()
goto(130,100)
pendown()
right(280)
forward(70)

#end of fasanauruli khinkali

exitonclick()