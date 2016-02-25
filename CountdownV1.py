#countdown letters implementation using recursion 
#Countdown Solver without generating permutations
#Arjun Kharel - Software Development (GMIT)

wordmap = dict()

def preprocessing():
	wordsList = [line.rstrip('\n') for line in open('words.txt')]
	for word in wordsList:
		#generate the key #generate the value
		key = sum(bytearray(word,'utf8')) #sum of the word, ascii value
		addToMap(key,word)
	print("preprocessing completed")

#adding ascii value as a key and list of words as values
def addToMap(key,value):
	if key in wordmap:
		wordmap.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
	else:
		wordmap.update({key:[value]})

def beginProcess():
	#end of preprocessing
	preprocessing()
	print(len(wordmap))
	
beginProcess()