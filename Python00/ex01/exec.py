import sys

def main(*args):
	if not args:
		print("Usage:input a string!")
		return
	joined = " ".join(args).swapcase()
	print(joined[::-1])

if __name__ == "__main__":
    main(*sys.argv[1:])