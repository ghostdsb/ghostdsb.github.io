---
layout: post-euler
title:  "Project Euler Solution 017"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Number letter counts</h2>
<div><p>If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.</p><p>If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? </p><br/><p><b>NOTE:</b> Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.</p></div>

### Solution

{% highlight python %}
#pe17
def digits(num):
	n = num
	dig = 0
	while n > 0:
		n = n//10
		dig += 1
	return dig

def count_char(word):
	w = 'qwertyuioplkjhgfdsazxcvbnm'
	chars = 0
	for l in word:
		if l in w:
			chars += 1
	return chars

words = {0: '',
		 1: 'one',
		 2: 'two',
		 3: 'three',
		 4: 'four',
		 5: 'five',
		 6: 'six',
		 7: 'seven',
		 8: 'eight',
		 9: 'nine',
		 10: 'ten',
		 11: 'eleven',
		 12: 'twelve',
		 13: 'thirteen',
		 14: 'fourteen',
		 15: 'fifteen',
		 16: 'sixteen',
		 17: 'seventeen',
		 18: 'eighteen',
		 19: 'nineteen',
		 20: 'twenty',
		 30: 'thirty',
		 40: 'forty',
		 50: 'fifty',
		 60: 'sixty',
		 70: 'seventy',
		 80: 'eighty',
		 90: 'ninety',
		 100: 'hundred',
		 1000: 'thousand',
		 1000000: 'million',
		 1000000000: 'billion'}

		 
def two_digit(i):
	if i not in words:
		tens = i//10
		units = i%10
		ans = words[tens*10]+words[units]
	if i in words:
		ans = words[i]
	return ans

tot_chars = 0	

for i in range(1,1001):	
	if digits(i)==1:
		ans = words[i]
	elif digits(i)==2:
		ans = two_digit(i)
	elif digits(i)==3 and i not in words:
		t_digit = i%100
		hundreds = i//100
		if t_digit != 0:
			ans = words[hundreds]+words[100]+" and "+two_digit(t_digit)
		else:
			ans = words[hundreds]+words[100]
	elif digits(i)==3 and i in words:
		ans = 'one'+words[i]
	elif digits(i)==4:
		ans = 'one'+words[i]
	print(i,ans,count_char(ans))
	tot_chars += count_char(ans)
print(tot_chars)

#21124
{% endhighlight %}
