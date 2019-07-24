def __init__(self, encoding_factor, ax, bx, cx):
	self.encfac = int(encoding_factor)
	
	an = 8027
	bn = 83542
	cn = 755
	
	self.a = an * ax
	self.b = bn * bx
	self.c = cn * cx


def enc(self):
	to_be_worked_on = input("What do you want to be encoded?: ")
	
	print("The following will be encoded: ", str(to_be_worked_on))
	
	for i in to_be_worked_on:
		character = ord(i)
		
		part_a = (self.encfac * (
				(int(self.a * (character ** 2))) + (int(self.b * character)) + (int(self.c))))
		part_b = (self.encfac * (
				(int(self.a * (part_a ** 2))) + (int(self.b * part_a)) + (int(self.c)))) + 1
		
		print(part_b)
