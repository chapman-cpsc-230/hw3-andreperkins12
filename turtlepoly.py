import turtle

### MAM: You did not sk the user for the number of sides and length of side, per the intructions.
### Same problem in turtlestart1.py.

# Now create a graphics window.
t = turtle.Pen()
for j in range(1):
    for i in range(5):
        t.forward(100)
        t.left(72)
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
