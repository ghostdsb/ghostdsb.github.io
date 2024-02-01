---
layout: post-euler
title:  "Project Euler Solution 042"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Coded triangle numbers</h2>
<div><p>The <i>n</i><sup>th</sup> term of the sequence of triangle numbers is given by, <i>t<sub>n</sub></i> = ½<i>n</i>(<i>n</i>+1); so the first ten triangle numbers are:</p><p>1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...</p><p>By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = <i>t</i><sub>10</sub>. If the word value is a triangle number then we shall call the word a triangle word.</p><p>Using <a>words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?</p></div>

### Solution

{% highlight python %}
#pe042
def wordval(word):
	score = 0
	for letter in word:
		score += (ord(letter)-64)
	return score

with open(r'C:\Users\Dibyanshu\Desktop\Project Euler\my_solutions\p042_words.txt') as w:
	wordlist = w.read().split(",")
#wordlist = [[w.split('"')] for w in words.split(",")]
#print(wordlist)
maxlen = -1
ans = ''
for word in wordlist:
	if len(word)>maxlen:
		maxlen = len(word)
		ans = word
print(ans,maxlen)
limit = 26*maxlen
print(limit)

triangle_list = []
d = 1
j = 2
while d<limit:
	triangle_list.append(d)
	d += j
	j += 1
print(triangle_list)
counter = 0
for w in wordlist:
	word = w[1:-1]
	if wordval(word) in triangle_list:
		counter += 1
		print(word,wordval(word))
print(counter)
#print(wordlist[1][1:-1],wordval(wordlist[1][1:-1]))

{% endhighlight %}
