---
layout: post-euler
title:  "Project Euler Solution 005"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Smallest multiple</h2>
<div><p>2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.</p><p>What is the smallest positive number that is <dfn>evenly divisible</dfn> by all of the numbers from 1 to 20?</p></div>

### Solution

{% highlight python %}
#pe05
def lcm(a1,b1):
	a = max(a1,b1)
	b = min(a1,b1)
	(m,n) = (a,b)
	while b != 0:
		(a,b) = (b,a%b)
	return m*n//a

ans = 1
for i in range(2,21):
	ans = lcm(i,ans)
print(ans) 

{% endhighlight %}
