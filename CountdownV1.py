#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Arjun Kharel - Software Development (GMIT)

import pickle
import operator
from random import sample, randint

result = dict()
MIN_WORD_LENGTH = 6
pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)
tempList = list()
maxLength = 0


def solver(word):
	convertedKey = sum(bytearray(word,'utf8'))
	if(len(word)>=MIN_WORD_LENGTH):
		countdownLetters = wordmap.get(convertedKey)
		if(convertedKey in wordmap):
			for str in countdownLetters:
				if sorted(word)==sorted(str) and str not in result:
					result.update({str:len(str)})
		tempList = list(word)
		for i in range(len(tempList)):
			charTmp = tempList.pop()
			wordStr =''.join(tempList)
			tempList.insert(0,charTmp)
			solver(wordStr)##
	return result
	
def generateWord():
	"""
	random.sample(population, k)
	Returns a new list containing elements from the population while leaving the original population unchanged. 
	The resulting list is in selection order so that all sub-slices will also be valid random samples. This allows 
	raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).
	Members of the population need not be hashable or unique. If the population contains repeats, then each occurrence
	is a possible selection in the sample.
	https://docs.python.org/2/library/random.html#random.sample
	"""
	VOWELS = 'eeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaiiiiiiiiiiiiiooooooooooooouuuuu'
	CONSONANTS = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'
	n_vowels = randint(3,5)
	vowels = sample(VOWELS, n_vowels)
	consonants = sample(CONSONANTS, 9 - n_vowels)
	letters = vowels+consonants
	print(letters)
	word = ''.join(letters)
	#print(word)
	return word
	
def beginProcess():
	#end of preprocessing
	#preprocessing()
	word = generateWord()
	countdownLetters = solver(word)
	if(countdownLetters):
		#sort the words from highest length to lowest (big to small)
		sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse = True)
		print(sorted_x)
	
beginProcess()
##References
#http://www.thecountdownpage.com/letters.htm letter frequencies
##https://docs.python.org/2/library/random.html#random.sample