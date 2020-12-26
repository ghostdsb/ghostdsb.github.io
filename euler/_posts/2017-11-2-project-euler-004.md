---
layout: post-euler
title:  "Project Euler Solution 004"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Largest palindrome product</h2>
<div><p>A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.</p><p>Find the largest palindrome made from the product of two 3-digit numbers.</p></div>

### Solution

{% highlight python %}
#pe004
def palindrome(check):
	sc = str(check)
	tr = ""
	for i in sc[::-1]:
		tr += i
	if(sc==tr):
		return True
	else:
		return False
		
ans = 0		
for i in range(999,100,-1):
	for j in range(999,100,-1):
		ans_p = i*j
		if palindrome(ans_p) and ans_p >= ans:
			ans = ans_p
			print(ans)

			
{% endhighlight %}
