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
		for permutations in combinations(letters,i):
			sortedWord = ''.join(permutations)
			if(sortedWord in wordmap):
				for word in wordmap[sortedWord]:
					result.add(word)
		if(result):
			return result #we fond the longest
	return result
	
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

def beginProcess():
	word = generateWord()#this function is implemented in conundrumGenerator.py. We are reusing the function.
	print("\nBelow is the result of the longest anagrams of random conundrum: ",word)
	tempResult = solver(word)
	print("\nNumber of longest anagrams found: ", len(tempResult))
	print(tempResult)
	
#beginProcess()
optionsMenu()
	
##from countdownV2Perm import beginProcess
##print(timeit.timeit('beginProcess()', setup='from countdownV2Perm import beginProcess', number=1000))