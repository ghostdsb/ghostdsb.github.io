---
layout: post-euler
title:  "Project Euler Solution 053"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Combinatoric selections</h2>
<div><p>There are exactly ten ways of selecting three from five, 12345:</p><p>123, 124, 125, 134, 135, 145, 234, 235, 245, and 345</p><p>In combinatorics, we use the notation, $\displaystyle \binom 5 3 = 10$.</p><p>In general, $\displaystyle \binom n r = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times ... \times 3 \times 2 \times 1$, and $0! = 1$.
</p><p>It is not until $n = 23$, that a value exceeds one-million: $\displaystyle \binom {23} {10} = 1144066$.</p><p>How many, not necessarily distinct, values of $\displaystyle \binom n r$ for $1 \le n \le 100$, are greater than one-million?</p></div>

### Solution

{% highlight python %}
#pe053
import math

counter = 0

for i in range(101):
	for j in range(i+1):
		c = math.factorial(i)//(math.factorial(j)*math.factorial(i-j))
		if c>1000000:
			counter += 1
print(counter)

{% endhighlight %}
