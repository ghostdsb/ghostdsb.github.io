---
layout: post-euler
title:  "Project Euler Solution 007"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>10001st prime</h2>
<div><p>By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.</p><p>What is the 10 001st prime number?</p></div>

### Solution

{% highlight python %}
#pe007
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
		if len(prime)==10001:
			break
			
	#print(prime)
	return prime[-1]
	
ans = prime_num(999999)
print(ans)

	
	
{% endhighlight %}
