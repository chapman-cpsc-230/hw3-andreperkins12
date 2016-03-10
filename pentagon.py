import turtle



# Now create a graphics window.
t = turtle.Pen()
for j in range(1):
    for i in range(5):
        t.forward(100)
        t.left(72)
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
