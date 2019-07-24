class Encoder:
	"""This is to be used as an encoding tool for scripts"""
	
	def __init__(self, encoding_factor, ax, bx, cx):
		self.encfac = int(encoding_factor)
		
		self.a = int(ax)
		self.b = int(bx)
		self.c = int(cx)
	
	def enc(self):
		to_be_worked_on = input("What do you want to be encoded?: ")
		
		print("The following will be encoded: ", str(to_be_worked_on))
		
		for i in to_be_worked_on:
			character = ord(i)
			
			to_be_added = self.encfac * (
					(int(self.a * (character ** 2))) + (int(self.b * character)) + (int(self.c)))
			
			print(to_be_added)
