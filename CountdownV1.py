#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Arjun Kharel - Software Development (GMIT)

def preprocessing():
	wordsList = [line.rstrip('\n') for line in open('words.txt')]
	for word in wordsList:
		#generate the key #generate the value
		key = sum(bytearray(word,'utf8')) #sum of the word, ascii value
	print("preprocessing completed")
#end of preprocessing
preprocessing()