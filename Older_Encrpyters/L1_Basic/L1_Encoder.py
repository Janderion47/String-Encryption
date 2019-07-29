class Encoder:
	def __init__(self, encoding_factor):
		self.encfac = int(encoding_factor)
	
	def enc(self):
		to_be_worked_on = input("What do you want to be encoded?: ")
		if to_be_worked_on == "That is it":
			exit()
		else:
			print("The following will be encoded: ", str(to_be_worked_on))
			
			for i in to_be_worked_on:
				to_be_added = int(ord(i) * int(self.encfac))
				
				print(to_be_added)
