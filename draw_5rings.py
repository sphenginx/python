# 基于 turtle 库， 画一个五环
from turtle import *
colors = ['blue', 'black', 'red', 'yellow', 'green']
for i in range(5): 
	x = -100+100*i if i < 3 else 50*(-1)**i
	y = 50 if i < 3 else 0
	up()
	goto(x, y)
	width(5)
	down() 
	color(colors[i]) 
	circle(40)

'''
标注
'''
color('pink')
up()
goto(-80, -80)
down()
write("the Olympic Rings", font=("Aril", 18, 'bold'))
done()
