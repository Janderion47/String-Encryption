def __init__(self, decoding_factor):
	self.decfac = int(decoding_factor)


def dec(self):
	will_be_decoded = int(input("What is to be decoded?: "))
	
	print("The following will be decoded: ", will_be_decoded)
	
	to_be_printed = chr(int(int(will_be_decoded) / int(self.decfac)))
	print(to_be_printed)
	
	dec(self)
