#Arjun Kharel - Software Development (GMIT) - Theory  of Algorithms
#countdown letters implementation using recursion - We are NOT generating permutations of a word

import pickle
import timeit
import operator
from conundrumGenerator import generateWord #importing generateWord() function from  conundrumGenerator.py 
from random import sample, randint
from collections import deque ##You can add and remove items on both ends of a deque at O(1) cost.

result = dict()#dict to hold the countdown letters. key will be the word itself and value will be the length of the words.
MIN_WORD_LENGTH = 6 #the depth you want to do down in the recusion..
TERMINATE = 0
GENERATE_CONUNDRUM = 1

pickle_in = open("dict.pickle","rb") 
wordmap = pickle.load(pickle_in)#loading the(pickeled) dictionary

def solver(word):
	sortedWord = sorted(word)
	key = ''.join(sortedWord)
	if(len(word)>=MIN_WORD_LENGTH):
		countdownLetters = wordmap.get(key)
		if(key in wordmap):
			for str in countdownLetters:
				if sortedWord==sorted(str) and str not in result: #checking sortedWord is same as the words in resultset
					result.update({str:len(str)})
					
		tempList = deque(word)#This is exactly I needed for this particular problem. I wanted to take the element from tail and append to
		#the head. This can be done using deque data structure at O(1) cost.
		for i in range(len(tempList)):
			charTmp = tempList.pop()#popping from the end of the deque
			wordStr =''.join(tempList)
			tempList.insert(0,charTmp)#inserting to head
			solver(wordStr)##recursively calling the solver function
	return result

def optionsMenu(): #this displays the menu and when valid option is selected it calls beginProcess()
	mode=GENERATE_CONUNDRUM; #flag
	while(mode != TERMINATE):
		try:
			mode=int(input('Enter 1 to generate the random conundrum or 0 to exit:'))
			if(mode==1):
				beginProcess()
			else:
				print("GoodBye...")
		except ValueError:
			print ("Enter 1 to generate the random conundrum or 0 to exit:")
	
def beginProcess():
	word = generateWord() #generates random word
	countdownLetters = solver(word)
	if(countdownLetters):
		print("\nBelow is the result of the longest anagrams of random conundrum: ",word)
		
		#sorted_x will be a list of tuples sorted by the second element(value) in each tuple.
		sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse = True) #
		
		#sorted_x= sorted(result.items(), key=lambda x: x[1], reverse=True) 
		#could use lambda key=lambda x: x[1] to sort as well. Tested with both ways but THERE is not much difference at all.
		
		print("Total words found: " , len(sorted_x),' with recursion depth (min word length) of : ',MIN_WORD_LENGTH,'\n')
		print(sorted_x)
		print('------------------------------------------------------------------------------------------------------')
		result.clear()
	else:
		print("Ooops, couldn't find the countdown letters/anagrams for the word: " ,word)

optionsMenu() #program starts from here...

#beginProcess()
#uncomment the print statements if you would like to test the time 
#from countdownV1Recursive import beginProcess
#print(timeit.timeit('beginProcess()', setup='from countdownV1Recursive import beginProcess', number=100))

##References
#http://www.thecountdownpage.com/letters.htm letter frequencies
##https://docs.python.org/2/library/random.html#random.sample
##https://docs.python.org/2/library/operator.html
##http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
##http://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python
##http://stackoverflow.com/questions/280243/python-linked-list
##http://stackoverflow.com/questions/4690416/sorting-dictionary-using-operator-itemgetter