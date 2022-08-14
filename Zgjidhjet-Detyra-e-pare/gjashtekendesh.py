import turtle

gjashtekendesh = turtle.Turtle()
gjashtekendesh.pencolor("black")

for i in range(6):
    gjashtekendesh.forward(100)
    gjashtekendesh.left(60)
# You can also write: gjashtekendesh.right(60), it is about the direction
# It only starts in right direction
# The reason why the angle is 60??
# The reason why the angle is 60, is because 360/6=60

# Now let's draw the hexagonal
print(" ")
print("             ________________")
print("            /                \\")
print("           /                  \\")
print("          /                    \\")
print("         /                      \\")
print("        /                        \\")
print("        \                        /")
print("         \                      /")
print("          \                    /")
print("           \                  /")
print("            \________________/")
print(" ")
