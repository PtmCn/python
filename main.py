import turtle
import math

side = int (input('How many sides:'))
sidelength = int (input('How long is each side:'))
column = int (input('How many columns:'))
row =int  (input('How many rows:'))
"""
def find_xmax():
  k = 0
  if turtle.xcor() > k: 
    k = turtle.xcor()
  return k
"""

def draw_shape():
  turtle.forward(sidelength)
  for x in range(side-1):
    turtle.left(360/side)
    turtle.forward(sidelength)
    #find_xmax()

ystart=0
height = sidelength #math.radians(30)*sidelength
gap = 10
xmax = sidelength
for x in range(column):
  xstart =  0
  ystart = ystart - height - gap
  for x in range(row):
    turtle.pu()
    turtle.left(360/side)
    turtle.goto(xstart,ystart)
    turtle.pd()  

    draw_shape()

    xstart = xstart + xmax + gap

  turtle.pu()
  turtle.goto(0,ystart)
  turtle.pd()

turtle.done()
