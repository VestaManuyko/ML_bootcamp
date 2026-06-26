import sys
import string

def main(arg, max_length):
	cleaned = (''.join(c for c in arg if c not in string.punctuation)).split()
	result = [word for word in cleaned if len(word) > max_length]
	print(result)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Error, incorrect nbr of args")
		exit()
	try:
		arg = int(sys.argv[2])
	except ValueError:
		print("Error, second arg must be int")
		exit()
	main(sys.argv[1], arg)