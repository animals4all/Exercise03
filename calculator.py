"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *

def main():
	# Your code goes here
	quit = False
	while not quit:
		command = raw_input().split()
		if command[0] in ("+", "-", "*", "/", "pow", "mod"):
			try:
				num1, num2 = int(command[1]), int(command[2])
				if command[0] == "+":
					print add(num1, num2)
				elif command[0] == "-":
					print subtract(num1, num2)
				elif command[0] == "*":
					print multiply(num1, num2)
				elif command[0] == "/":
					print divide(num1, num2)
				elif command[0] == "pow":
					print power(num1, num2)
				elif command[0] == "mod":
					print mod(num1, num2)
			except ValueError:
				print "I don't know what that means."
		elif command[0] in ("square", "cube"):
			try:
				num1 = int(command[1])
				if command[0] == "square":
					print square(num1)
				elif command[0] == "cube":
					print cube(num1)
			except ValueError:
				print "I don't know what that means."
		elif command[0] == "q":
			quit = True
		else:
			print "I don't know what that means."

if __name__ == '__main__':
    main()
