kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main(arg):
	for key, value in arg.items():
		print(key, "was created by", value)

if __name__ == "__main__":
    main(kata)