import pickle
from itertools import combinations
import timeit
pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)
MIN_RANGE = 4
MAX_RANGE = 10

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
#print(solver("education"))
def beginProcess():
	print(solver("education"))
beginProcess()
	
#from countdownV2Perm import beginProcess
#print(timeit.timeit('beginProcess()', setup='from countdownV2Perm import beginProcess', number=10000))