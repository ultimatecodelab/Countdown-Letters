#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Allows user to enter the min word(length), they would like to extract
#from the original word.
#Arjun Kharel - Software Development (GMIT)

import pickle
import timeit
import operator
from conundrumGenerator import generateWord
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
	
def beginProcess():
	word = generateWord()
	countdownLetters = solver(word,1)
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