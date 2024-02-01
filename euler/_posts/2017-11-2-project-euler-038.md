---
layout: post-euler
title:  "Project Euler Solution 038"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Pandigital multiples</h2>
<div><p>Take the number 192 and multiply it by each of 1, 2, and 3:</p><blockquote>192 × 1 = 192<br/>
192 × 2 = 384<br/>
192 × 3 = 576</blockquote><p>By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)</p><p>The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).</p><p>What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , <var>n</var>) where <var>n</var> > 1?</p></div>

### Solution

{% highlight python %}
# 9234 9487

def isPan(a,b):
    pan = [1,2,3,4,5,6,7,8,9]
    count = 0
    if len(str(a)) + len(str(b)) == 9:
        for digs in pan:
            if str(digs) in str(a) or str(digs) in str(b):
                count += 1
    return count==9

for i in range(9487,9233,-1):
    if isPan(i,2*i):
        print(str(i)+str(2*i))
        break

{% endhighlight %}
