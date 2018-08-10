#Fibonacci
def fibonacci(n):
	a, b = 0, 1
	if n <= 1:
		print("参数不得小于1")
		pass
	while b < n:
		print(b)
		a, b = b, a + b


# 100 以内的斐波纳契数列
fibonacci(100)