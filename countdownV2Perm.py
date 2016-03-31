#Arjun Kharel - Software Development (GMIT) 
#Countdown Solver by generating permutations
#Significantly faster than countdownV1Recursive
#Please also check countdownV1Recursive.py. I have solved the countdown solver in two different algorithms and both
#have their pros and cons. Please check out the Github/Gist readme for more details.

import pickle
from conundrumGenerator import generateWord,userEnteredConundrum #coming from conundrumGenerator.py **(please check).
from itertools import combinations
import timeit

pickle_in = open("dict.pickle","rb")
wordmap = pickle.load(pickle_in)
MIN_RANGE = 4
MAX_RANGE = 10
TERMINATE = 0
GENERATE_CONUNDRUM = 1
RANDOMLY_GENERATED_CONUNDRUM = 1 #9 letters will be generated randomly
USER_GENERATED_CONUNDRUM = 2 #User can specify their own 9 letters word, the program will only accept if word satisfies the requirement
							  #of the program. 3 Min Vowels , 3 Min Consonants.

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
	
##The below function mycombinations(k,available,used) can also be used for  generating permutations. This is slower than
##the original python implementation. Original itertools.combinations functions 
##semms to be significantly faster if you timeit for 1000 of times otherwise you cannot really see any difference.
##You can simply comment the solver() function and uncomment myCombinations(),solver2(),tempResult2 = solver2(word) and 
##comment tempResult = solver(word) in beginProcess() to test and see the differences in running
##time of these different approaches. You won't see really see the difference if you are is running only ONE time but
##if you timeit for 1000 you can see the differences in running time. mycombinations(k,available,used) takes 
##approximately 3 seconds (timeit = 1000), whereas itertools.permutations finishes in less than a second.

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
#game menu
def optionsMenu():
	mode=GENERATE_CONUNDRUM; #flag
	while(mode != TERMINATE):
		try:
			print('-----------------------------------------------------------------------')
			mode=int(input('Enter 1 to generate the random conundrum, OR 2 to enter your own OR 0 to exit the game:'))
			if(mode==RANDOMLY_GENERATED_CONUNDRUM):
				beginProcess(RANDOMLY_GENERATED_CONUNDRUM)
			elif(mode==USER_GENERATED_CONUNDRUM):
				beginProcess(USER_GENERATED_CONUNDRUM)
			else:
				print("GoodBye...")
		except ValueError:
			print ("Enter 1 to generate the random conundrum or 0 to exit:")

def beginProcess(option):
	if(option==RANDOMLY_GENERATED_CONUNDRUM):	
		word = generateWord() #this function is implemented in conundrumGenerator.py. We are reusing the function.
	elif(option==USER_GENERATED_CONUNDRUM):
		word = userEnteredConundrum()

	print("Randomly generated conundrum is: ",list(word))
	
	tempResult = solver(word)
	#tempResult2 = solver2(word) ## UNCOMMENT the myCombinations() and solver2() and only uncomment this line
	if(tempResult):
		print("\nBelow is the result of the longest anagrams of random conundrum: ",word)
		print("\nNumber of longest anagrams found: ", len(tempResult))
		print(tempResult)
		
optionsMenu()
##test for time - please uncomment the below code and comment all the print statements. Also check the timing section in github/gist readme. 
##I have done the detailed analysis of efficiency performance and scalability
#from countdownV2Perm import beginProcess
#print(timeit.timeit('beginProcess(1)', setup='from countdownV2Perm import beginProcess', number=1000))

##https://docs.python.org/2/library/itertools.html#itertools.combinations
##http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
#http://www.thecountdownpage.com/letters.htm letter frequencies
##https://docs.python.org/2/library/random.html#random.sample
##https://docs.python.org/2/library/operator.html
##http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
##http://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python
##http://stackoverflow.com/questions/280243/python-linked-list