"""
TurtleArtStarter
Original author: UTeach CSA
Modified by: Alex Wolfe
Student Name: 
Core: 

"""
#This program will be completed to draw your Turtle Art
import turtle

#create the turtle object, set the speed and hide the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

#set the position (x,y coordinate) of the turtle to begin drawing
#set the turtle facing right
t.setpos(10,-90)    #set the position (x, y)
t.setheading(0)     #set the heading (direction) to 0 degrees (right)
t.pencolor("black") #set the pencolor - this can be changed
t.pensize(6)        #set the pensize - this can be changed
t.pendown()         #set the pen down to begin drawing
