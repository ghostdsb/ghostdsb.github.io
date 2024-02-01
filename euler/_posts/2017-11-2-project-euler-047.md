---
layout: post-euler
title:  "Project Euler Solution 047"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Distinct primes factors</h2>
<div><p>The first two consecutive numbers to have two distinct prime factors are:</p><p>14 = 2 × 7<br/>15 = 3 × 5</p><p>The first three consecutive numbers to have three distinct prime factors are:</p><p>644 = 2² × 7 × 23<br/>645 = 3 × 5 × 43<br/>646 = 2 × 17 × 19.</p><p>Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?</p></div>

### Solution

{% highlight python %}
import primecache

prime_list = primecache.primelist(150000)

def primefactors(num):
    pf = []
    i = 0
    while num>1:
        if num%prime_list[i]==0:
            while num%prime_list[i]==0:
                num/=prime_list[i]
                if prime_list[i] in pf or len(pf)>0 and pf[len(pf)-1]%prime_list[i]==0:
                    pf[len(pf)-1] *= prime_list[i]
                else:
                    pf.append(prime_list[i])
            i += 1
        else:
            i += 1
    return pf


notfound = True
start = 10
lim = 4
while notfound:
    chain = 0
    cons_prime = []
    cons_prime_len = []
    for i in range(start,start+lim):
        pfactors = primefactors(i)
        cons_prime_len.append(len(pfactors))
        for j in pfactors:
            cons_prime.append(j)
    #print(cons_prime,cons_prime_len)
    allval = 1
    for i in cons_prime_len:
        if i == lim:
            allval *= 1
        else:
            allval *= 0
    if allval == 1 and len(cons_prime) == len(set(cons_prime)):
        print(start)
        notfound = False
    else:
        start += 1

{% endhighlight %}
