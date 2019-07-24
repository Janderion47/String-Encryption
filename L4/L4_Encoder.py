def __init__(self, factor, cod_a, cod_b, cod_c):
	an = 1
	bn = 1
	cn = 1
	
	self.encfac = int(factor)
	self.a = an * cod_a
	self.b = bn * cod_b
	self.c = cn * cod_c


def enc(self):
	a = int(self.a)
	b = int(self.b)
	c = int(self.c)
	eff = int(self.encfac)
	
	to_be_encoded = input("What do you wish to be encoded master?: ")
	
	for i in to_be_encoded:
		character = int(ord(i))
		
		part_a = (eff * ((a * (character ** 2)) + (b * character) + c))
		part_b = (eff * ((a * (part_a ** 2)) + (b * part_a) + c)) - 9999999999999999
		
		a = a + 1
		b = b + 1
		c = c + 1
		
		print(part_b)
