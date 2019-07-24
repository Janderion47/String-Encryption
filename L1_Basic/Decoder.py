class Decoder:
	"""This is to be used as an decoding tool for the encoding tool up above"""
	
	def __init__(self, decoding_factor):
		self.decfac = int(decoding_factor)
	
	def dec(self):
		will_be_decoded = int(input("What is to be decoded?: "))
		
		print("The following will be decoded: ", will_be_decoded)
		
		to_be_printed = chr(int(int(will_be_decoded) / int(self.decfac)))
		print(to_be_printed)
		
		Decoder.dec(self)
