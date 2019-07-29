class Encoder:
	def __init__(self, factor, a, b, c):
		self.encfac = int(factor)
		self.a = a[0] * a[1]
		self.b = b[0] * b[1]
		self.c = c[0] * c[1]
		self.add = [a[2], b[2], c[2]]
	
	def enc(self):
		a = self.a
		b = self.b
		c = self.c
		eff = self.encfac
		
		to_be_encoded = input("What do you wish to be encoded master?: ")
		
		for i in to_be_encoded:
			character = int(ord(i))
			
			part_a = (eff * ((a * (character ** 2)) + (b * character) + c))
			part_b = (eff * ((a * (part_a ** 2)) + (b * part_a) + c)) - 9999999999999999
			
			a += self.add[0]
			b += self.add[1]
			c += self.add[2]
			
			print(part_b)
