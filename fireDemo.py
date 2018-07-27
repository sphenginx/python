# 基于 fire 库的  cli 模式
# python fireDemo.py add 5 6 
# python fireDemo.py multify 5 6 
# …… 
# 
import fire

class Calculator(object):
	def add(self, x, y):
		return x + y

	def multify(self, x, y):
		return x * y

	def reduce(self, x, y):
		return x - y

	def divide(self, x, y):
		if y == 0:
			return '除数不能是0'
		return x / y

if __name__ == '__main__':
	fire.Fire(Calculator)
