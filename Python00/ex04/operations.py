import sys

def main(*args):
	if not args:
		return
	if (len(args) != 2):
		print("Incorrect number of args")
		return
	try:
		a = int(args[0])
		b = int(args[1])
	except ValueError:
		print("args are not integers")
		return
	print("Sum:", a+b)
	print("Difference:", a-b)
	print("Product:", a*b)
	try:
		a/b
	except ZeroDivisionError:
		print("Quotient: ERROR")
		print("Remainder: ERROR")
		return
	print("Quotient:", a/b)
	print("Remainder:", a%b)

if __name__ == "__main__":
    main(*sys.argv[1:])