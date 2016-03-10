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
	letters = sorted(letters)
	for i in reversed(range(MIN_RANGE,MAX_RANGE)):
		result = set()
		for permutations in combinations(letters,i): #itertools.combinations()
			sortedWord = ''.join(permutations)
			if(sortedWord in wordmap):
				for word in wordmap[sortedWord]:
					result.add(word)
		if(result):
			return result #we fond the longest
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
	mode=GENERATE_CONUNDRUM;
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
	word = "ioeecdrln"
	#word = generateWord()#this function is implemented in conundrumGenerator.py. We are reusing the function.
	print("\nBelow is the result of the longest anagrams of random conundrum: ",word)
	tempResult = solver(word)
	#tempResult2 = solver2(word) ## UNCOMMENT the myCombinations() and solver2() and only uncomment this line
	print("\nNumber of longest anagrams found: ", len(tempResult))
	print(tempResult)
	
optionsMenu()
	
##from countdownV2Perm import beginProcess
##print(timeit.timeit('beginProcess()', setup='from countdownV2Perm import beginProcess', number=1000))

##[01]https://docs.python.org/2/library/itertools.html#itertools.combinations