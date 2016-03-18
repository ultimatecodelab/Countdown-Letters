
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

Now at this point I was ready to start programming the countdown solver.



## Words list
Words were grabbed from multiple sources [5, 6]. Please check the link below. 

## Python scripts
    •countdownV1Recursive.py
    
    •countdownV2Perm.py
    
    •conundrumGenerator.py
    
    •pickler.py
    
I solved this problem using two different approaches (1: **recursive** and 2: by generating **permutations of letters**) and both have their own pros and cons.  The first and initial approach was using recursion to solve it because it suited well for this problem. The algorithm below will clarify why I chose to solve this problem recursively.  During my theory of algorithms class I implemented an anagram finder.  I basically modified my existing anagram solver and adapted well to solve countdown solver too. There was one very important change I had make which is, if there are no anagrams of original 9 randomise letters I had to check of 8 letters and so on and so forth.  Please check the actual countdownV1Recursive.py . The script has been heavily commented.  In this readme I am going to talk little bit about the important section of countdownV1Recursive.py.

###countdownV1Recursive.py (version 1)
This is the most important section of this algorithm.

```
def solver(word):
	sortedWord = sorted(word)
	key = ''.join(sortedWord)
	if(len(word)>=MIN_WORD_LENGTH):
		countdownLetters = wordmap.get(key)
		if(key in wordmap):
			for str in countdownLetters:
				if sortedWord==sorted(str) and str not in result: #checking sortedWord is same as the words in resultset
					result.update({str:len(str)})
					
		tempList = deque(word)#This is exactly I needed for this particular problem. I wanted to take the append/pop from both ends.
		#This can be done using deque data structure at O(1) cost.
		for i in range(len(tempList)):
			charTmp = tempList.popleft()#popping out from the left of the deque o(1)
			wordStr =''.join(tempList)
			tempList.append(charTmp)#inserting at the right
			solver(wordStr)##recursively calling the solver function
	return result
```

*Initially I was using tempList = list() and I soon realise this was a bad approach. If you check the for loop in above code you can
see I am inserting to the front and removing from the end. ***THIS IS A DISASTER** when you are repeatedly exceuting the expensive statements like in the above for loop. The main problem with list as It needed to do a lot of **shifting** of the elements which significantly impacted on the performane. By using list, it was taking approximately 3-4 seconds to bring all the anagrams of randomly generated 9 letters conundrum AND  **all other subsets of the original 9 letters up to the specified recursion depth (minimum word length)**.  I was not happy with it. When I was not impressed with the performance I did some research on a data structure that would allow me to solve the above issue more efficently. 

I came to discover python has a data structure called a **deque** which allows appends/pops from both ends at almost constant time. *list-like container with fast appends and pops on either end* . This is exactly what I needed in my case and I easily adapted the code to deque  from list and the performance was literally improved by more than 50% and algorithm ran under half a seconds in worst case. **Official python docs says *Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.* ** 

##countdownV2Perm.py (version 2)
Once I fully implemented the above recursive solution. I wanted to try the second version, just to experiment which version performs
better or worse. In the second version I decided to generate the **permutations** of 9 randomly generated alphabets and brute force the whole thing as efficiently as possible.  My main challenge in this version was to generate the permutations as fast as possible. I tried few different permutations generation algorithms and you can see this in the actual script. I have commented out in the script.
I generated permutations using **itertools.combinations**. This is the fastest of all and it is a built in python function. Yes, I said the fastest, but not the best :), and the reason is it does not **SCALE** well. To generate the permutations of length less than =<10, it is superb but the main problem is, if we have to generate the permutations of 12-13 letters, it would not be offensive to mention that It would be slow as hell.But remember, this version is way way way faster than recursive version provided the word length or letters are no more than 10. Scalability is the main issue in this version. 

This is the most important section of this algorithm.

```
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
```


**So which one is better?**
Well, the anwer is, it depend. The countdownV1Recursive.py is certainly more scalable than countdownV2Perm.py because in the recursive version, we are not generating the permutations at all.  countdownV1Recursive.py brings the anagrams of 9 letters and all other subsets up to the recursive depth (the min word length ) - in another word the stop condition for recursive function. The countdownV2Perm.py stops when it finds the longest possible anagrams of randomly generated alphabets, but if you want it to bring all other subsets then you should uncomment the  return statement in the algorithms and your sound. Most of the online countdown solver game returns anagrams of all other subsets of original 9 letters up to the length 4-5 therefore, I choose to implement the same in recursive version and slightly different in other version where I am generating permutations.

Anyway finally to answer which one is better, if you want something that scales well, recursive version is the best, but if you want the fastest that works only for 9-10 letters than countdownV2Perm.py is for you.  Infact when you run the program once you wont see any difference in performance from both algorithms but you will see the difference when you timeit for 1000 times. We will discuss timing in another section. :)

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



Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References

[1]: https://www.youtube.com/watch?v=E3vmoac0R2Y

[2]: https://en.wikipedia.org/wiki/Letter_frequency

[3]:https://upload.wikimedia.org/wikipedia/commons/d/d5/English_letter_frequency_%28alphabetic%29.svg

[4]: http://www.thecountdownpage.com/letters.htm

[5]: http://www.bestwordlist.com/9letterwords.txt

[6]: http://www.mieliestronk.com/corncob_lowercase.txt
