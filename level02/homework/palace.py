from turtle import *
# we want to paint palace
speed(100)
width(5)

forward(400)

right(810)
forward(220)
right(810)           #height Of square
forward(400)
right(810)
forward(220)

     

penup()
goto(100,5)
pendown()

forward(50)
right(810)
forward(50)
right(810)

forward(50)
penup()
goto(200,0)      
pendown()

right(810)
right(810)
forward(55)
right(810)
forward(50)
right(810)
forward(55)



#and of square

penup()
goto(0,200)
pendown()

forward(420)


right(810)
forward(100)
right(810)       #height of roof

forward(420)
right(810)
forward(150)
left(810)



forward(100)
left(810)
forward(200)
left(810)

forward(100)   #height of roof
left(810)
forward(100)
left(810)




penup()
goto(10,300)
pendown()



forward(50)
left(810)
forward(120)
left(810)
forward(50)



 #end of first roof
 
 
penup()
goto(400,200)
pendown()


forward(420)
left(810)
forward(100)
left(810)

forward(420)
left(810)
forward(100)
left(810)         #heihgt of second roof
                        
penup()
goto(500,200)
pendown()

left(810)
forward(20)
left(130)
forward(120)

left(100)
forward(120)
right(230)
forward(50)

#end of second roof

penup()
goto(443,295)
pendown()


left(810)
forward(60)
right(830)         #height of flag
forward(60)
right(860)
forward(60)
left(790)


#end of flag

penup()
goto(150,100)
forward(320)
pendown()


right(810)
right(810)     #height of door
forward(100)
right(810)

forward(100)
right(810)
forward(100)

#end of door

penup()
goto(425,100)
pendown()
forward(50)      #height of window
left(810)
forward(50)
left(810)

forward(50)
left(810)
forward(50)
#end of window


penup()
goto(425,0)
pendown()

left(810)
forward(50)
left(810)
forward(50)    #height  of second window

left(810)
forward(50)
left(810)
forward(50)
#end of second window

penup()
goto(100,100)
forward(125)
pendown()

forward(50)
left(810)
forward(50)
left(810)        #height of third
forward(50)
left(810)
forward(50)
#end of third window




exitonclick()