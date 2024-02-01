---
layout: post-euler
title:  "Project Euler Solution 046"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Goldbach's other conjecture</h2>
<div><p>It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.</p><p>9 = 7 + 2×1<sup>2</sup><br/>
15 = 7 + 2×2<sup>2</sup><br/>
21 = 3 + 2×3<sup>2</sup><br/>
25 = 7 + 2×3<sup>2</sup><br/>
27 = 19 + 2×2<sup>2</sup><br/>
33 = 31 + 2×1<sup>2</sup></p><p>It turns out that the conjecture was false.</p><p>What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?</p></div>

### Solution

{% highlight python %}
#composite = prime + 2*square

import primecache
import math

def isSquare(num):
    return math.sqrt(num) == int(math.sqrt(num))

plist = primecache.primelist(10000)
clist = []
for p in range(2,10000):
    if p not in plist:
        clist.append(p)

print(plist)
print(clist)
passnum = []
for c in clist:
    check = 0
    found = False
    for p in plist:
        #check = 0
        if c>p and isSquare(int((c-p)/2)):
            check *= 0
            found = True
            break
        else:
            check += 1
    if found == True:
        passnum.append(c)
        print(c,p)
for c in clist:
    if c not in passnum:
        print(c)

{% endhighlight %}
