#Arjun Kharel - Software Development (GMIT) 
#Countdown Solver by generating permutations
#Significantly faster than countdownV1Recursive
#please read through the github readme. I have compare and constrasted
#both algorithms.

import pickle
from conundrumGenerator import generateWord
from itertools import combinations
import timeit

pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)
MIN_RANGE = 4
MAX_RANGE = 10
TERMINATE = 0
GENERATE_CONUNDRUM = 1

def solver(letters):
	letters = sorted(letters) ##sorting alphabets
	for i in reversed(range(MIN_RANGE,MAX_RANGE)): #reverse means we are starting from high to low value. Decending order.
		result = set() #set to hold the result (countdown letters)
		for permutations in combinations(letters,i): #itertools.combinations()
			#we are looping through the list returned by the combinations function from itertools. 
			#"Return r length subsequences of elements from the input iterable."
			
			sortedWord = ''.join(permutations)
			if(sortedWord in wordmap):
				for word in wordmap[sortedWord]:
					result.add(word)
		if(result):
			return result #we fond the longest
		#if you want to get all the words from length max (9) to min(4) than
		#comment if(result) then you can see all the words in decending order.
	return result
	
##This function mycombinations(k,available,used) can also be used for  generating permutations. This is slower than
##the original python implementation. Original itertools.combinations functions 
##semms to be significantly faster.  You can simply comment the solver() function
##and uncomment myCombinations() and solver2(), and tempResult = solver(word) in beginProcess() and 
##comment tempResult = solver(word) in beginProcess() to test and see the differences in running
##time of these different approaches.

'''def mycombinations(k,available,used):
	if len(used)==k:
		yield tuple(used)
	elif len(available)== 0:
		pass
	else:
		head = available.pop(0)
		used.append(head)
		for c in mycombinations(k, available,used):
			yield c
		used.pop(-1)
		for c in mycombinations(k,available,used):
			yield c
		available.insert(0,head)

##solver two calls the the above mycombinations function.
def solver2(letters):
	letters = sorted(letters)
	for i in reversed(range(MIN_RANGE,MAX_RANGE)):
		result = set()
		for perm in mycombinations(i,letters,[]):
			sortedWord = ''.join(perm)
			if(sortedWord in wordmap):
				for word in wordmap[sortedWord]:
					result.add(word)
		if(result):
			return result #we fond the longest word/words
	return result
'''
def optionsMenu():
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

##TEST Word : ioeecdrln
def beginProcess():
	##word = "ioeecdrln"
	word = generateWord()#this function is implemented in conundrumGenerator.py. We are reusing the function.
	print("\nBelow is the result of the longest anagrams of random conundrum: ",word)
	tempResult = solver(word)
	#tempResult2 = solver2(word) ## UNCOMMENT the myCombinations() and solver2() and only uncomment this line
	print("\nNumber of longest anagrams found: ", len(tempResult))
	print(tempResult)
	
optionsMenu()

## test for time - please uncomment the below code and comment all the print statements
##from countdownV2Perm import beginProcess
##print(timeit.timeit('beginProcess()', setup='from countdownV2Perm import beginProcess', number=1000))

##https://docs.python.org/2/library/itertools.html#itertools.combinations
#http://www.thecountdownpage.com/letters.htm letter frequencies
##https://docs.python.org/2/library/random.html#random.sample
##https://docs.python.org/2/library/operator.html
##http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
##http://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python
##http://stackoverflow.com/questions/280243/python-linked-list