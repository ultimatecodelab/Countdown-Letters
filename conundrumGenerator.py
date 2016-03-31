from random import sample, randint
from random import shuffle
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
	shuffle(letters)
	word = ''.join(letters)
	return word
	
#rule checking
def checkForRules(word):
	vowels = ['a','e','i','o','u']
	vowelsCount = 0
	consonantCount = 0 
	
	wrdList = list(word)
	for i in range(0,len(wrdList)):
		if(wrdList[i] in vowels):
			vowelsCount+=1
		else:
			consonantCount+=1
		
	if(vowelsCount>=3 and consonantCount>=3):
		return True
	else:
		return False
		
#user entered word.
def userEnteredConundrum():	
	userWord = input("\nEnter your random word of length 9,Min Vowels(3) min consonants (3): ")
	status = checkForRules(userWord)
	
	while(len(userWord)!=9 or status==False):
		userWord = input("\nEnter your random word of length 9,Min Vowels(3) min consonants (3): ")
		status = checkForRules(userWord)
	return userWord
	