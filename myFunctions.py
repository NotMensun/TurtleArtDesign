#Mensun Wang, Functions
def polygon(t,sides,distance):
    angle = 360/sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.right(angle)

    t.end_fill()

def teleport(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def box(t,c):
    t.begin_fill()
    for times in range(4):
        t.color(c)
        t.forward(20)
        t.right(90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.end_fill()

#function within function for extra credit

def black_repeat_five(t,z):
    for times in range(5):
        teleport(t,-200,1+times*-20+z)
        for times in range(20):
            box(t,"black")
    





    
