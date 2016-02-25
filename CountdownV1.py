#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Arjun Kharel - Software Development (GMIT)

import pickle
result = dict()
MIN_WORD_LENGTH = 4
pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)

def solver(word):
	convertedKey = sum(bytearray(word,'utf8'))
	if(len(word)>=MIN_WORD_LENGTH):
		countdownLetters = wordmap.get(convertedKey)
		if(convertedKey in wordmap):
			for str in countdownLetters:
				if sorted(word)==sorted(str) and str not in result:
					result.update({str:len(str)})
					
	##lets use recursion to loop through each character
	#we will rearrange the original word and recursively
	##call this solver() function to find other matching words.	
	
	return result
	
def beginProcess():
	#end of preprocessing
	#preprocessing()
	print(len(wordmap))
	print(solver("education"))
	
beginProcess()