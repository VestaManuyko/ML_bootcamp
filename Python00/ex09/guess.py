import sys
import random

def main():
	print("This s an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game.\nGood luck!\n")
	nbr_of_trials = 0
	secret_nbr = random.randint(1, 99)
	while True:
		nbr_of_trials += 1
		print("What's your guess?")
		answer = input(">>")
		if answer == "exit":
			print("Goodbye!")
			exit()
		try:
			answer = int(answer)
		except ValueError:
			print("Bro comon, I said a number\n")
			continue
		if answer > secret_nbr:
			print("Too high!\n")
			continue
		if answer < secret_nbr:
			print("Too low!\n")
			continue
		else:
			print("Congrats, you won!\n")
			if answer == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.\n")
			if nbr_of_trials == 1:
				print("Wow! From the first attempt, impressive!\n")
			else:
				print("It took you", nbr_of_trials, " attempts!\n")
			exit()


if __name__ == "__main__":
	main()