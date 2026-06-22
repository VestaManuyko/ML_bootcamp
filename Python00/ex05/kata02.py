kata = (2019, 9, 25, 3, 30)

def main(arg):
	print(f"{kata[1]:02d}/{kata[2]}/{kata[0]} {kata[3]:02d}:{kata[4]}")

if __name__ == "__main__":
    main(kata)