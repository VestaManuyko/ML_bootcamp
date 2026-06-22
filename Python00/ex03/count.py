import sys
import string

def text_analyzer(args = None):
	"""This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""
	if (args == None):
		print("What is the text to analyze?")
		args = input(">>")
	upper = sum(c.isupper() for c in args)
	lower = sum(c.islower() for c in args)
	digits = sum(c.isdigit() for c in args)
	spaces = sum(c.isspace() for c in args)
	printable = sum(c.isprintable() for c in args)
	punctuation = sum(c in string.punctuation for c in args)

	print("The text contains", printable, "characters:")
	print("Uppercase:", upper)
	print("Lowercase:", lower)
	print("Punctuation marks:", punctuation)
	print("Spaces:", spaces)

if __name__ == "__main__":
	if not sys.argv[1:]:
		print("No args")
	if (len(sys.argv[1:]) > 1):
		print("too many args")
	text_analyzer(sys.argv[1])