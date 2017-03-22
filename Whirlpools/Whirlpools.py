#Imports the "Whirlpool" Function from myFunction -> Design5
from WhirlpoolFunction import *
#Imports the turtle into the program to use
import turtle
#Gives the turtles names, so the turtles know which commands to follow and which commands not to follow
bob = turtle.Turtle()
bobb = turtle.Turtle()
bobbb = turtle.Turtle()
#Set's the turtle's speeds to "0" (Fastest)
bob.speed(0)
bobb.speed(0)
bobbb.speed(0)
#Makes the turtles not draw a line when moving
bob.penup()
bobb.penup()
bobbb.penup()
#Allows the turtles to use color
turtle.colormode(255)
#The following code from lines 18 -> line 22 are putting the turtles in their starting position
bob.forward(300)
bobb.left(120)
bobb.forward(450)
bobbb.left(240)
bobbb.forward(350)
#Makes the turtles draw a line when moving positions
bob.pendown()
bobb.pendown()
bobbb.pendown()

#Makes the background Blue
turtle.bgcolor("Blue")
#"for times in range(256):" tells the turtles to do the following indented commands 256 times each
for times in range(256):
    #Tells the turtles to draw circles that are steadily increasing in size
    bob.circle(times)
    bobb.circle(times)
    bobbb.circle(times)
    #Defines the variable "c" so it is easier to give the turtles color
    c = (0, 255-times, times)
    #Tells the turtles to use the color "c" that is defined above
    bob.color(c)
    bobb.color(c)
    bobbb.color(c)
    #Tells the program to tell us what color it is currently using in the shell file
    print(c)
    #Whirlpool is explained in function file
    #bob.left and bob.forward turn the turtle and make the turtle move forward respectively
    Whirlpool(bob, 10, 10, 5)
    bob.left(30)
    bob.forward(150)
    Whirlpool(bobb, 10, 10, 5)
    bobb.left(30)
    bobb.forward(150)
    Whirlpool(bobbb, 10, 10, 5)
    bobbb.left(30)
    bobbb.forward(150)

#Hides the turtle after all the program is done running    
bob.ht()
bobb.ht()
bobbb.ht()
