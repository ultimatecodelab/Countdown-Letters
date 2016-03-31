import pickle
wordmap = dict()

def preprocessing():
	wordsList = [line.rstrip('\n') for line in open('words.txt')]
	for word in wordsList:
		key = sorted(word)
		sortedKey = ''.join(key)
		addToMap(sortedKey,word)

#adding to map
def addToMap(key,value):
	if(len(key)>=4 and len(key)<=9):
		if key in wordmap:
			wordmap.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
		else:
			wordmap.update({key:[value]})
		
preprocessing()	
pickle.dump(wordmap, open('dict.pickle', 'wb'), -1)