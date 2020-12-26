---
layout: post-euler
title:  "Project Euler Solution 041"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Pandigital prime</h2>
<div><p>We shall say that an <i>n</i>-digit number is pandigital if it makes use of all the digits 1 to <i>n</i> exactly once. For example, 2143 is a 4-digit pandigital and is also prime.</p><p>What is the largest <i>n</i>-digit pandigital prime that exists?</p></div>

### Solution

{% highlight python %}
#p041
import primecache


def isPan(a):
    pan = []
    for i in range(len(str(a))):
        pan.append(i+1)
    count = 0
    for digs in pan:
        if str(digs) in str(a):
            count += 1
    return count==len(str(a))

primes = primecache.primelist(10**7)
for i in primes[::-1]:
    if isPan(i):
        print(i)
        break

{% endhighlight %}
