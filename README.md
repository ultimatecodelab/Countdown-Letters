
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

## Background Research 

The first thing that I did after I got the project is did some research on the problem. My first task was to actually understand the countdown game. I knew about the game but wasn’t sure about all the aspect of it, example: frequency analysis of alphabets and also the winning conditions for a player. I went to YouTube and searched for “countdown letter game”. I ended up clicking [1].At the end of the video, I got full knowledge of game itself, and how it’s played. 

Now at this point, I understood the game and what I am trying to solve. I am ready to do more search on other aspects of game.  The very first and important thing I wanted to find next was the randomised letters. I was not sure about the frequency of the alphabets I am supposed to use for this game.  I quickly googled and I ended up in this wikipedia page [3].

**Wikipedia alphabets frequency**

![Alt text](https://upload.wikimedia.org/wikipedia/commons/d/d5/English_letter_frequency_%28alphabetic%29.svg "Optional title")

I now have the frequency of English alphabets. I googled again and this time I searched for the alphabets frequency of countdown letters game.  I found this source [4] to be useful for the particular problem I am trying to solve and it also has greater distribution of alphabets (67 Vowels and 76 Consonants . This source has the frequency for a countdown letter game. Therefore I decided to use this in my project for doing alphabets frequency analysis.  Adapted from [4] - *This is the standard letter distribution used on Countdown, as supplied by Art Director Demelza Sampson in January 2009, and kindly passed on to me by Charlie Reams. Please note that letters are added and removed from time to time by the producers, so this list does not necessarily reflect the letters used in any particular edition of the programme. For example, an analysis of the first few weeks of Series 63 highlights the fact that the number of G's, V's and W's are all currently increased by 1 and that there may be one fewer N.*

I am not yet ready to start programming. I needed a list of English words.  Myself, Vlad, John Walsh, we combined the multiple wordlists into one gigantic wordlist. We worked collaboratively and spent some time to find the best wordlist as possible. I was searching to find the best source as possible and eventually I forwarded this link to Vlad and John [5] .  When the wordlist was combined, Vlad sent me words.txt and I decided to use this in my project and contains **267751** words. 

So, what did I accomplish from this background research?

•	I fully understood the problem I was going to solve

•	I understood the game rules

•	I knew the frequency of countdown alphabets I needed to use. 

•	I have a wordlist to get started. 

Now I am ready to start programming the countdown solver.



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

[1]: https://www.youtube.com/watch?v=E3vmoac0R2Y

[2]: https://en.wikipedia.org/wiki/Letter_frequency

[3]:https://upload.wikimedia.org/wikipedia/commons/d/d5/English_letter_frequency_%28alphabetic%29.svg

[4]: http://www.thecountdownpage.com/letters.htm

[5]: http://www.bestwordlist.com/9letterwords.txt

