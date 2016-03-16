
###Arjun Kharel - G00298984 - Theory of Algorithms - Year 4 (GMIT)


#Table of contents

###1: Introduction
###2: Background
###3: Words List
###4: Files and Scripts 
###4: Algorithms (Two versions)
    -countdownV1Recursive.py
    
    -countdownV2Perm.py
###5: Compare and Contrast of both algorithms
###6: References
 
##1: Introduction
 The idea of this project was to demonstrate the understand of different data structures and algorithms. This is a college project
 and it is about solving the countdown letters game as efficient as we could along with the detailed analysis of the chosen  approach/algorithm
 to solve this particular problem.

## Background
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Cool Project name][2] and [Cool Solver][3].

## Words list
My words list is in the file [wordslist.txt](wordslist.txt) in this repoistory/gist.
I got my words list from the [Oxford Learner's Dictionaries][1] website.

## Python script
My script is in the files [solver.py](solver.py) in this repository and it works as follows.
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead. I am using python pickle module to   for serializing and de-serializing my dictionary. It gives almost constant time to load the dictionary. I have saved the whole 
dict() object and dumped it. When starts off I am simply loading the pickled file. This is how the preprocessing is done.
'''
    import pickle
    wordmap = dict()
    
    def preprocessing():
    	wordsList = [line.rstrip('\n') for line in open('words.txt')]
    	for word in wordsList:
    		#generate the key #generate the value
    		#key = sum(bytearray(word,'utf8')) #sum of the word, ascii value
    		key = sorted(word)
    		sortedKey = ''.join(key)
    		addToMap(sortedKey,word)
    
    #adding ascii value as a key and list of words as values
    def addToMap(key,value):
    	if(len(key)>=4 and len(key)<=9):
    		if key in wordmap:
    			wordmap.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
    		else:
    			wordmap.update({key:[value]})
    		
    preprocessing()	
    pickle.dump(wordmap, open('dict.pickle', 'wb'), -1)

**When you run the above code snippt it will create dict.pickle and you can load in your script like this**

```
    pickle_in = open("dict.pickle","rb")
    
    wordmap = pickle.load(pickle_in)
```
    
**That's all, wordmap (dict) contains all the keys and value :)**
**countdownV2Perm.py and countdownV1Recursive.py , both are using the same dictonary file. The same pickled file is loaded in both versions**

## Efficiency comparasion of countdownV2Perm.py and countdownV1Recursive.py
**countdownV2Perm.py** : This version of algorithms generates the permutations of 9 letters word and for each generated word it checks
against the dictionary. The key in the dictionary is sorted so whenever the permutations is computed I am first sorting the word and I'm
checking against the dictionary. If sorted word equals the key in dict, I am iterating through the value(set).




Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References
