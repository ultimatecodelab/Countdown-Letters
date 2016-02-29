#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Allows user to enter the min word(length), they would like to extract
#from the original word.
#Arjun Kharel - Software Development (GMIT)

import pickle
import timeit
import operator
from random import sample, randint
from collections import deque ##You can add and remove items on both ends of a deque at O(1) cost.

result = dict()
MIN_WORD_LENGTH = 6 #the depth you want to do down..
pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)
maxLength = 0

def solver(word,iteration):
	sortedWord = sorted(word)
	key = ''.join(sortedWord)
	if(len(word)>=MIN_WORD_LENGTH):
		countdownLetters = wordmap.get(key)
		if(key in wordmap):
			for str in countdownLetters:
				if sortedWord==sorted(str) and str not in result:
					result.update({str:len(str)})
		
		tempList = deque(word)
		for i in range(len(tempList)):
			charTmp = tempList.pop()
			wordStr =''.join(tempList)
			tempList.insert(0,charTmp)
			solver(wordStr,(i+1))##recursively calling the solver function
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
	word = ''.join(letters)
	return word
	
def beginProcess():
	word = generateWord()
	countdownLetters = solver("iaapxmkhs",1)
	if(countdownLetters):
		#sort the words from highest length to lowest (big to small)
		sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse = True)
		print(sorted_x)
	
beginProcess()
##from countdownV1 import beginProcess
##print(timeit.timeit('beginProcess()', setup='from countdownV1 import beginProcess', number=100))

##References
#http://www.thecountdownpage.com/letters.htm letter frequencies
##https://docs.python.org/2/library/random.html#random.sample
##https://docs.python.org/2/library/operator.html
##http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
##http://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python
##http://stackoverflow.com/questions/280243/python-linked-list