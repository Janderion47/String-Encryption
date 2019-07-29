class Decoder:
	def __init__(self, a, b, c, steps = 5):
		self.a = a[0]
		self.b = b[0]
		self.c = c[0]
		self.add = [a[1], b[1], c[1]]
		self.steps = steps
	
	def dec(self):
		import math as m
		a = int(self.a)
		b = int(self.b)
		c = int(self.c)
		
		numbers = input("What is the set you wish to decode my lord?: ")
		
		to_be_decoded = list(numbers.split(" "))
		
		def do_over(steps, x, a, b, c):
			memory = x
			step = 1
			while step <= steps:
				memory = int((-b + m.sqrt((b ** 2) - (4 * a * (c - memory)))) / (2 * a))
				step += 1
			
			return memory
		
		export_list = []
		for num in to_be_decoded:
			out = do_over(self.steps, int(num), a, b, c)
			
			a += self.add[0]
			b += self.add[1]
			c += self.add[2]
			
			export_list.append(chr(out))
		for letter in export_list:
			print(letter, end = "")
