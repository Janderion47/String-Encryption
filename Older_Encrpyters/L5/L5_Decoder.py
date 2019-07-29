class Decoder:
	def __init__(self, factor, a, b, c):
		self.decfac = int(factor)
		self.a = a[0] * a[1]
		self.b = b[0] * b[1]
		self.c = c[0] * c[1]
		self.add = [a[2], b[2], c[2]]
	
	def dec(self):
		import math as m
		a = int(self.a)
		b = int(self.b)
		c = int(self.c)
		decn = int(self.decfac)
		
		numbers = input("What is the set you wish to decode my lord?: ")
		
		to_be_decoded = list(numbers.split(" "))
		
		export_list = []
		for num in to_be_decoded:
			will_be_decoded = ((int(num) + 9999999999999999) / decn)
			
			part_a = ((int((-b + m.sqrt((b ** 2) - (4 * a * (c - will_be_decoded)))) / (2 * a))) / decn)
			part_b = int((-b + m.sqrt((b ** 2) - (4 * a * (c - part_a)))) / (2 * a))
			
			a += self.add[0]
			b += self.add[1]
			c += self.add[2]
			
			export_list.append(chr(part_b))
		for letter in export_list:
			print(letter, end = "")
