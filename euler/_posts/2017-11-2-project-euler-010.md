---
layout: post-euler
title:  "Project Euler Solution 010"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Summation of primes</h2>
<div><p>The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.</p><p>Find the sum of all the primes below two million.</p></div>

### Solution

{% highlight python %}
#pe010
def prime_num(number):
	p = [True]*(number+1)
	p[0] = False
	p[1] = False
	
	for i in range(2, len(p)):
		for j in range(i*i, len(p), i):
			if p[j]:
				p[j] = False
				
	prime = []
	for i in range(len(p)):
		if p[i]:
			prime.append(i)
	
	return sum(prime)
	
ans = prime_num(2000001)
print(ans)

{% endhighlight %}
