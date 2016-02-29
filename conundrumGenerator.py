from random import sample, randint
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