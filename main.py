import turtle
gap = 10
side = int (input('How many sides:'))
sidelength = int(input('How long is each side:'))
row = int (input('How many rows:'))
#column =int  (input('How many columns:'))
"""
for x in range(row):
  for x in range(column):
    print ('* ', end = '')
  print ('\n')  
"""
turtle.goto(0,0)
for x in range(row):
  turtle.forward(sidelength) # draw base

  turtle.left(180-(180/side))
  turtle.forward(sidelength)

  turtle.left(180 - (180 / side))
  turtle.forward(sidelength)

  turtle.pu()
  turtle.left(180-(180/side))
  turtle.forward(sidelength+gap)  
  turtle.pd()

turtle.done()
