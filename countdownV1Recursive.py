#Arjun Kharel G00298984 - Software Development (GMIT) - Theory  of Algorithms

#countdown letters implementation using recursion - We are NOT generating permutations of a word therefore this version can scale up
#very well than the other version where I have generated the permutations of different letters. If the game rule changes from 9 letters to lets say
#12-14 letters we will have scalability issues with "countdownV2Perm.py" version. CountdownV2Perm.py is extremly fast compare 
#to this "countdownV1Recursive.py" version, provided the number of letters are <=10, but It can't scale up well when number of letters goes 
#above 12/13 and therefore I have completed this project in two different approaches so we can compare and contrast both algorithms
#based on performance/efficiency/scalability.

import pickle
import timeit
import operator
from conundrumGenerator import generateWord,userEnteredConundrum #importing generateWord() and userEnteredConundrum() function from  conundrumGenerator.py 
from random import sample, randint
from collections import deque ##You can add and remove items on both ends of a deque at O(1) cost.

result = dict()#dict to hold the countdown letters. key will be the word itself and value will be the length of the words.
MIN_WORD_LENGTH = 6 #the depth you want to do down in the recusion..
MAX_RANGE=10 #word max length -1
TERMINATE = 0 #terminate the program
GENERATE_CONUNDRUM = 1 
RANDOMLY_GENERATED_CONUNDRUM = 1 #9 letters will be generated randomly
USER_GENERATED_CONUNDRUM = 2 #User can specify their own 9 letters word, the program will only accept if word satisfies the requirement
							  #of the program. 3 Min Vowels , 3 Min Consonants.

pickle_in = open("dict.pickle","rb") 
wordmap = pickle.load(pickle_in)#loading the(pickeled) dictionary - this is extremly fast

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
			mode=int(input('Enter 1 to generate the random conundrum, OR 2 to enter your own OR 0 to exit the game:'))
			if(mode==RANDOMLY_GENERATED_CONUNDRUM):
				beginProcess(RANDOMLY_GENERATED_CONUNDRUM)
			elif(mode==USER_GENERATED_CONUNDRUM):
				beginProcess(USER_GENERATED_CONUNDRUM)
			else:
				print("GoodBye...")
		except ValueError:
			print ("Enter 1 to generate the random conundrum, OR 2 to enter your own OR 0 to exit the game:")
	
def beginProcess(option):
	if(option==RANDOMLY_GENERATED_CONUNDRUM):	
		word = generateWord()#this function is implemented in conundrumGenerator.py. We are reusing the function.
	elif(option==USER_GENERATED_CONUNDRUM):
		word = userEnteredConundrum()
	print("Randomly generated conundrum is: ",list(word))
	countdownLetters = solver(word)
	
	if(countdownLetters):
		print("\nBelow is the result of the longest anagrams of random conundrum: ",word)
		#sorted_x will be a list of tuples sorted by the second element(value) in each tuple.
		sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse = True) 
		#sorted_x= sorted(result.items(), key=lambda x: x[1], reverse=True) 
		#could use lambda key=lambda x: x[1] to sort as well. Tested with both ways but THERE is not much difference at all.
		#print('------------------------------------------------------------------------------------------------------')
		print("Total words found: " , len(sorted_x),' with recursion depth (min word length) of : ',MIN_WORD_LENGTH,'\n')
		print(sorted_x)
	else:
		print("Ooops, couldn't find the countdown letters/anagrams for the word: " ,word)
	result.clear()


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