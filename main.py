import turtle
import math

side = int (input('How many sides:'))
a = int (input('How long is each side:')) #sidelength
column = int (input('How many columns:'))
row =int  (input('How many rows:'))
gap = 10

#check input
if 3 > side > 12:
  print ("Error,side must be between 3-12")
#width/height calc
if side == 3:
  width = a
  height = math.sqrt(3)/2*a
elif side == 4:
  width = a
  height = a 
elif side == 5:
  width = (a/2)*(1+math.sqrt(5))
  height = a*math.sqrt(5+2*math.sqrt(5))/2
elif side == 6:
  width = 2*a
  height = 2*a
elif side == 7:
  width =a/(2*math.sin(math.pi/2/7))
  height =a/(2*math.tan(math.pi/2/7))
elif side == 8:
  width = a*(1+math.sqrt(2))
  height = a*(1+math.sqrt(2))
elif side == 9:
  rc = (a/2)*(1/math.sin(math.pi/9))
  ri = (a/2)*(1/math.tan(math.pi/9))
  width = 2*rc*math.sin(2*math.pi/9)
  height = rc*ri
elif side == 10:
  width = a*(1+math.sqrt(5))
  height = a*math.sqrt(5+2*math.sqrt(5))
elif side == 11:
  width = a*math.sin(math.pi*5/11)/math.sin(math.pi/11)
  height = a/(2*math.tan(math.pi/2/11))
elif side == 12:
  width = a/math.sin(math.pi/16)
  height = a/math.sin(math.pi/16)

def draw():
  for x in range(side):
    turtle.forward(a)
    turtle.left(360/side)

ystart = 0
for x in range(column):
  ystart = ystart - height - gap
  for x in range(row):
    turtle.pu()
    turtle.forward(width+gap)
    turtle.pd()
    draw()
  turtle.pu()
  turtle.goto (0,ystart)
  turtle.pd()
  
