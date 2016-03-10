import turtle



# Now create a graphics window.
t = turtle.Pen()
for j in range(1):
    for i in range(11):
        t.forward(200)
        t.left(163.65)
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
