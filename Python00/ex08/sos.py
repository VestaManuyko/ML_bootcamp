import sys

morsecode ={
	'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def main(*arg):
	if len(arg) > 1:
		for item in arg:
			if any(not c.isalnum() and not c.isspace() for c in item):
				print("Error")
				return
		arg = ' '.join(item for item in arg)
	else:
		if any(not c.isalnum() and not c.isspace() for c in arg[0]):
			print("Error")
			return
		arg = arg[0]
	arg = arg.replace(" ", "/")
	result = ""
	for c in arg:
		if c != "/":
			result += morsecode.get(c.upper())
			result += " "
		else:
			result += "/ "
	print(result)

if __name__ == "__main__":
	main(*sys.argv[1:])