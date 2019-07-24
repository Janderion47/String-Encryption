def __init__(self, factor, cod_a, cod_b, cod_c):
	an = 1
	bn = 1
	cn = 1
	
	self.decfac = int(factor)
	self.a = an * cod_a
	self.b = bn * cod_b
	self.c = cn * cod_c


def dec(self):
	import math as m
	a = int(self.a)
	b = int(self.b)
	c = int(self.c)
	decn = int(self.decfac)
	
	numbers = input("What is the set you wish to decode master?: ")
	
	to_be_decoded = list(numbers.split(" "))
	
	export_list = []
	for num in to_be_decoded:
		will_be_decoded = ((int(num) + 9999999999999999) / decn)
		
		part_a = ((int((-b + m.sqrt((b ** 2) - (4 * a * (c - will_be_decoded)))) / (2 * a))) / decn)
		part_b = int((-b + m.sqrt((b ** 2) - (4 * a * (c - part_a)))) / (2 * a))
		
		a += 1
		b += 1
		c += 1
		
		export_list.append(chr(part_b))
	for letter in export_list:
		print(letter, end = "")
