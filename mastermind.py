# A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”.

# --------------------------------------------

# ## Example
# Enter your four digit guess code: 7377
# BYBB
# Enter your four digit guess code: 3333
# YYYR
# Enter your four digit guess code: 5673
# YBBR
# Enter your four digit guess code: 5553
# YRYR
# Enter your four digit guess code: 8593
# YRBR
# Enter your four digit guess code: 1583
# You guessed it ! [1, 5, 8, 3]

import random


# generates a four-digit code
def gen_code():
	set_code = []
	
	for i in range(4):
		val = random.randint(0, 9)
		set_code.append(val)
		
	return set_code
	
# asks for input from the user
def input_code():
	code = input("Enter your four digit guess code: ")
	return code


# plays the game
def mastermind():
	
	genCode = gen_code()
	i = 0
	
	while i < 10:
		result = ""
		inputCode = [int(c) for c in input_code()]
		
		if len(inputCode) != 4:
			print("Enter only 4 digit number")
			continue
		
		if inputCode == genCode:
			print("You guessed it !", genCode)
			break
			
		for i,element in enumerate(inputCode):
			
			if element in genCode:
				
				if inputCode[i] == genCode[i]:
					result+="R"
				else:
					result+="Y"
			else:
				result+="B"
		print(result)
		
		i += 1
	else:	
		print("You ran out of trys !", genCode)	
		
		
# Driver Code
mastermind()

