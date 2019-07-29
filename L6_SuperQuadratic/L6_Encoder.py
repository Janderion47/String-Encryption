class Encoder:
	def __init__(self, a, b, c, steps = 5):
		self.a = a[0] * a[1]
		self.b = b[0] * b[1]
		self.c = c[0] * c[1]
		self.add = [a[2], b[2], c[2]]
		self.steps = steps
	
	def enc(self):
		a = self.a
		b = self.b
		c = self.c
		
		def do_over(steps, x, a, b, c):
			memory = x
			step = 1
			while step <= steps:
				memory = int((a * (memory ** 2)) + (b * memory) + c)
				step += 1
			
			return memory
		
		to_be_encoded = input("What do you wish to be encoded master?: ")
		
		for i in to_be_encoded:
			k = int(ord(i))
			
			out = do_over(self.steps, k, a, b, c)
			a += self.add[0]
			b += self.add[1]
			c += self.add[2]
			
			print(out)
