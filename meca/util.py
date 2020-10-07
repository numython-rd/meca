# Numython R&D
factors = {
	"km>m":1000,
	"m>km":1/1000,
}

def convert_x_to_y(k, x, y):
	"""
	Convert x to y
	"""
	conv = x + ">" + y
	if conv in factors:
		f = factors[conv]
	else:
		raise ValueError("Not valid conversion")
	return k*f

if __name__ == '__main__':
	print( convert_x_to_y(10,"m","km") )