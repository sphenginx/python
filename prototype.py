#turtle prototype
import turtle as t
t.shape('turtle')
t.color("purple")
def squre():
	t.left(60)
	t.forward(100)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(100)

for i in range(12):
	squre()

t.exitonclick()