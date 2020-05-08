from sys import argv as args

def getSleepingMan():
	if not args:
		print("Please enter an argument of number as length")
		return
	try:
		print(f"[(:D|{'-'*int(args[0])}]")
	except ValueError:
		print("Please enter a valid number as argument")

getSleepingMan()
