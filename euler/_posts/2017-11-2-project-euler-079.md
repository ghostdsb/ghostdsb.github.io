---
layout: post-euler
title:  "Project Euler Solution 079"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Passcode derivation</h2>
<div><p>A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.</p><p>The text file, <a>keylog.txt</a>, contains fifty successful login attempts.</p><p>Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.</p></div>

### Solution

{% highlight python %}
with open("C:\\Users\\Dibyanshu\\Desktop\\Project Euler\\p079_keylog.txt") as n:
	numbers = n.read().split("\n")
	
numbers = list(set(numbers[:-1]))
code = ''
numbefore = {}
numafter  = {}
for i in range(10):
	numbefore[i] = []
	numafter[i]  = []

for i in range(10):
	for num in numbers:
		if str(i) in str(num):
			idx = 0
			while str(num)[idx]!=str(i):
				if str(num)[idx] not in numbefore[i]:
					numbefore[i] += [str(num)[idx]]
				idx += 1
			idafter = str(num).index(str(i))
			while idafter < 3:
				if str(num)[idafter] not in numafter[i]:
					numafter[i] += [str(num)[idafter]]
				idafter += 1
				

for i in range(10):
	numbefore[i] = len(numbefore[i])
	numafter[i]  = len(numafter[i])

possible_digits = {}

for i in range(10):
	if numbefore[i]>0 or numafter[i]>0:
		possible_digits[i] = numbefore[i]
		
c = sorted([(k,v) for (v,k) in possible_digits.items()])

for i in range(len(c)):
	code += str(c[i][1])
print(code)


				



{% endhighlight %}
