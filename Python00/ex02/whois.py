import sys

def main(*args):
	if not args:
		return
	if (len(args) > 1):
		print("more than 1 argument is provided")
		return
	try:
		int(args[0])
	except ValueError:
		print("argument is not an integer")
		return
	if (int(args[0]) == 0):
		print("I am Zero.")
	elif (int(args[0]) % 2 == 1):
		print("I am Odd.")
	else:
		print("I am Even.")

if __name__ == "__main__":
    main(*sys.argv[1:])