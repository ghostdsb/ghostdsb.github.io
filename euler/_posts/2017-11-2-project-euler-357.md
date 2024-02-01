---
layout: post-euler
title:  "Project Euler Solution 357"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Prime generating integers</h2>
<div><p>
Consider the divisors of 30: 1,2,3,5,6,10,15,30.<br/>
It can be seen that for every divisor <var>d</var> of 30, <var>d</var>+30/<var>d</var> is prime.
</p><p>
Find the sum of all positive integers <var>n</var> not exceeding 100 000 000<br/>such that
for every divisor <var>d</var> of <var>n</var>, <var>d</var>+<var>n</var>/<var>d</var> is prime.
</p></div>

### Solution

{% highlight python %}
import math,primecache

def isSquare(num):
    return math.sqrt(num) == int(math.sqrt(num))

print(primecache.primelist(10**6))

{% endhighlight %}
