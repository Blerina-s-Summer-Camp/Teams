import turtle

shtepia = turtle.Turtle()
shtepia.pencolor("black")

for i in range(3):
    shtepia.forward(100)
    shtepia.left(120)
# 360/3=120

for i in range(4):
    shtepia.forward(100)
    shtepia.right(90)
#360/4=90

for i in range(4):
    shtepia.forward(30)
    shtepia.right(90)

shtepia.forward(70)

for i in range(4):
    shtepia.forward(30)
    shtepia.right(90)

shtepia.forward(30)
shtepia.right(90)
shtepia.forward(100)
shtepia.right(90)
shtepia.forward(40)

# You can draw the door using the for loop below
#for i in range(4):
#    shtepia.left(90)
#    shtepia.backward(45)

# But I will write another way of solving this
# Because in this below code we avoid the square door
# We will try making the door like a rectangular, with dimension 40x50

shtepia.forward(30)
shtepia.left(90)
shtepia.backward(50)
shtepia.left(90)
shtepia.forward(40)
shtepia.right(90)
shtepia.forward(50)
shtepia.left(90)
shtepia.forward(40)


# Now let's draw the house
print(" ")
print("                    /\\")
print("                   /  \\")
print("                  /    \\")
print("                 /      \\")
print("                /        \\")
print("               /          \\")
print("              /            \\")
print("             /--------------\\")
print("            |                |")
print("            |                |")
print("            |                |")
print("            |        --      |")
print("            |      |    |    |")
print("            |      |    |    |")
print("            |      |    |    |")
print("            |______|____|____|")
print(" ")