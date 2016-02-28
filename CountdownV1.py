#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Arjun Kharel - Software Development (GMIT)

import pickle
result = dict()
MIN_WORD_LENGTH = 6
pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)
tempList = list()
maxLength = 0

def solver(word):
	#trackerCount = len(word
	convertedKey = sum(bytearray(word,'utf8'))
	if(len(word)>=MIN_WORD_LENGTH):
		countdownLetters = wordmap.get(convertedKey)
		if(convertedKey in wordmap):
			for str in countdownLetters:
				if sorted(word)==sorted(str) and str not in result:
					result.update({str:len(str)})
		
		if(len(word)==9 and len(result)>0):
			return result
		tempList = list(word)
		for i in range(len(tempList)): #eoibklhlr software
			charTmp = tempList.pop()
			wordStr =''.join(tempList)
			tempList.insert(0,charTmp)
			solver(wordStr)
	return result
	
def beginProcess():
	#end of preprocessing
	#preprocessing()
	print(len(wordmap))
	print(solver("edumation"))
	
beginProcess()