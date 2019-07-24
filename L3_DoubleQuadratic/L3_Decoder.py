def __init__(self, decoding_factor, ax, bx, cx):
	self.decfac = int(decoding_factor)
	
	an = 8027
	bn = 83542
	cn = 755
	
	self.a = an * ax
	self.b = bn * bx
	self.c = cn * cx


def dec(self):
	import math as m
	
	will_be_decoded = (int(input("What is to be decoded?: ")) / self.decfac) - 1
	
	print("The following will be decoded: ", will_be_decoded)
	
	part_a = ((int((-self.b + m.sqrt((self.b ** 2) - (4 * self.a * (self.c - will_be_decoded)))) / (
			2 * self.a))) / self.decfac)
	part_b = int((-self.b + m.sqrt((self.b ** 2) - (4 * self.a * (self.c - part_a)))) / (2 * self.a))
	
	print(int(part_b))
	print(chr(part_b))
	# print(chr(int(to_be_printed_m)))
	
	dec(self)
