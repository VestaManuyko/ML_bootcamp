import sys
import time
from rich.progress import Progress

def ft_progress(lst):
	start_time = time.time()
	total = len(lst)
	for i, item in enumerate(lst):
		elapsed = time.time() - start_time
		eta = elapsed / (i+1) * (total - i)
		procent = int((i+1) / total * 100)
		filled = int(((i+1) / total) * 50)
		progress = "#" * filled + " " * (50 - filled)
		print(f"ETA: {eta:.2f} [{procent}%][{progress}] {i+1}/{total} | elapsed time {elapsed:.2f}s", end="\r")
		yield item

def main():
	listy = range(3333)
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		time.sleep(0.001)
	print()
	print(ret)

if __name__ == "__main__":
	main()