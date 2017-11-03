#Mensun Wang Main File
import turtle
turtle.colormode(255)
from myFunctions import*
bob=turtle.Turtle()
bob.speed(0)

black=(0,0,0)
red_one=(180,0,10)
red_two=(140,0,10)
red_three=(90,0,10)
red_four=(50,0,10)
white_one=(255,255,255)
white_two=(245,245,245)
turtle.bgcolor(black)

#background design
bob.begin_fill()
for times in range(255):
    bob.color(times*1+1,times*1+1,times*1+1)
    bob.circle(times*1+500)
    bob.right(60)
bob.begin_fill()

bob.right(180)

teleport(bob,-200,450)


#width 20, length 40
black_repeat_five(bob,430)
#first red(4)

teleport(bob,-200,350)
for times in range(17):
    box(bob,black)
box(bob,red_four)
box(bob,black)
box(bob,black)

teleport(bob,-200,330)
for times in range(17):
    box(bob,black)
box(bob,red_four)
box(bob,black)
box(bob,black)

teleport(bob,-200,310)
for times in range(16):
    box(bob,black)
box(bob,red_three)
box(bob,red_three)
box(bob,black)
box(bob,black)

teleport(bob,-200,290)
for times in range(16):
    box(bob,black)
box(bob,red_three)
box(bob,red_three)
box(bob,black)
box(bob,black)

teleport(bob,-200,270)
for times in range(15):
    box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_three)
box(bob,black)
box(bob,black)

teleport(bob,-200,250)
for times in range(15):
    box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_three)
box(bob,black)
box(bob,black)

teleport(bob,-200,230)
for times in range(14):
    box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_one)
box(bob,red_three)
box(bob,black)
box(bob,black)

teleport(bob,-200,210)
for times in range(14):
    box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_two)
for times in range(3):
    box(bob,black)

teleport(bob,-200,190)
for times in range(13):
    box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_one)
box(bob,red_two)
for times in range(3):
    box(bob,black)

teleport(bob,-200,170)
for times in range(13):
    box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_two)
for times in range(4):
    box(bob,black)

#first white

teleport(bob,-200,150)
for times in range(7):
    box(bob,black)
box(bob,white_two)
for times in range(4):
    box(bob,black)
box(bob,white_two)
box(bob,red_one)
box(bob,red_one)
box(bob,red_two)
for times in range(4):
    box(bob,black)

teleport(bob,-200,130)
for times in range(6):
    box(bob,black)
box(bob,white_two)
box(bob,white_two)
for times in range(4):
    box(bob,black)
box(bob,white_two)
box(bob,white_two)
box(bob,red_two)
for times in range(5):
    box(bob,black)

teleport(bob,-200,110)
for times in range(5):
    box(bob,black)
box(bob,white_two)
box(bob,white_one)
box(bob,white_one)
box(bob,white_two)
box(bob,black)
box(bob,black)
box(bob,white_two)
box(bob,white_one)
box(bob,white_one)
box(bob,white_two)
for times in range(5):
    box(bob,black)

teleport(bob,-200,90)
for times in range(5):
    box(bob,black)
box(bob,white_two)
box(bob,white_one)
box(bob,white_one)
box(bob,white_two)
box(bob,black)
box(bob,black)
box(bob,white_two)
box(bob,white_one)
box(bob,white_one)
box(bob,white_two)
for times in range(5):
    box(bob,black)

teleport(bob,-200,70)
for times in range(4):
    box(bob,black)
box(bob,white_two)
for times in range(4):
    box(bob,white_one)
box(bob,white_two)
box(bob,white_two)
for times in range(4):
    box(bob,white_one)
box(bob,white_two)
for times in range(4):
    box(bob,black)

teleport(bob,-200,50)
for times in range(4):
    box(bob,black)
box(bob,white_two)
for times in range(10):
    box(bob,white_one)
box(bob,white_two)
for times in range(4):
    box(bob,black)

teleport(bob,-200,30)
for times in range(5):
    box(bob,black)
box(bob,white_two)
for times in range(8):
    box(bob,white_one)
box(bob,white_two)
for times in range(5):
    box(bob,black)

teleport(bob,-200,10)
for times in range(5):
    box(bob,black)
box(bob,white_two)
for times in range(8):
    box(bob,white_one)
box(bob,white_two)
for times in range(5):
    box(bob,black)

teleport(bob,-200,-10)
for times in range(5):
    box(bob,black)
box(bob,red_two)
box(bob,white_two)
for times in range(6):
    box(bob,white_one)
box(bob,white_two)
for times in range(6):
    box(bob,black)

teleport(bob,-200,-30)
for times in range(4):
    box(bob,black)
box(bob,red_two)
box(bob,red_one)
box(bob,red_one)
box(bob,white_two)
box(bob,white_two)
box(bob,white_one)
box(bob,white_one)
box(bob,white_two)
box(bob,white_two)
for times in range(7):
    box(bob,black)

teleport(bob,-200,-50)
for times in range(4):
    box(bob,black)
box(bob,red_two)
box(bob,red_one)
box(bob,red_three)
box(bob,black)
box(bob,black)
box(bob,white_two)
box(bob,white_two)
for times in range(9):
    box(bob,black)

teleport(bob,-200,-70)
for times in range(3):
    box(bob,black)
box(bob,red_two)
box(bob,red_one)
box(bob,red_one)
box(bob,red_three)
for times in range(13):
    box(bob,black)

teleport(bob,-200,-90)
for times in range(3):
    box(bob,black)
box(bob,red_two)
box(bob,red_one)
box(bob,red_three)
for times in range(14):
    box(bob,black)

teleport(bob,-200,-110)
box(bob,black)
box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_one)
box(bob,red_three)
for times in range(14):
    box(bob,black)

teleport(bob,-200,-130)
box(bob,black)
box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_three)
for times in range(15):
    box(bob,black)

teleport(bob,-200,-150)
box(bob,black)
box(bob,black)
box(bob,red_three)
box(bob,red_one)
box(bob,red_three)
for times in range(15):
    box(bob,black)

teleport(bob,-200,-170)
box(bob,black)
box(bob,black)
box(bob,red_three)
box(bob,red_three)
for times in range(16):
    box(bob,black)

teleport(bob,-200,-190)
box(bob,black)
box(bob,black)
box(bob,red_three)
box(bob,red_three)
for times in range(16):
    box(bob,black)

teleport(bob,-200,-210)
box(bob,black)
box(bob,black)
box(bob,red_four)
for times in range(17):
    box(bob,black)

teleport(bob,-200,-230)
box(bob,black)
box(bob,black)
box(bob,red_four)

for times in range(17):
    box(bob,black)

black_repeat_five(bob,-250)

