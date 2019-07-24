class Decoder:
	"""This is to be used as an decoding tool for the encoding tool up above"""
	
	def __init__(self, decoding_factor, ax, bx, cx):
		self.decfac = int(decoding_factor)
		
		self.a = int(ax)
		self.b = int(bx)
		self.c = int(cx)
	
	def dec(self):
		import math as m
		will_be_decoded = (int(input("What is to be decoded?: ")) / self.decfac)
		
		print("The following will be decoded: ", will_be_decoded)
		
		to_be_printed = int(
			(-self.b + m.sqrt((self.b ** 2) - (4 * self.a * (self.c - will_be_decoded)))) / (2 * self.a))
		# to_be_printed_m = ((-self.b - m.sqrt((self.b ** 2) - 4 * self.a * (self.c - will_be_decoded))) / (2 * a))
		
		print(int(to_be_printed))
		print(chr(to_be_printed))
		# print(chr(int(to_be_printed_m)))
		
		Decoder.dec(self)
