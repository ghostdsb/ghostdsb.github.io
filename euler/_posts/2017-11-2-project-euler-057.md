---
layout: post-euler
title:  "Project Euler Solution 057"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Square root convergents</h2>
<div><p>It is possible to show that the square root of two can be expressed as an infinite continued fraction.</p><p>$\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$</p><p>By expanding this for the first four iterations, we get:</p><p>$1 + \frac 1 2 = \frac  32 = 1.5$<br/>
$1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$<br/>
$1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$<br/>
$1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$<br/></p><p>The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.</p><p>In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?</p></div>

### Solution

{% highlight python %}
n = []
d = []
n.append(3)
d.append(2)
count = 0
for i in range(1000):
    d.append(n[-1]+d[-1])
    n.append(n[-1]+2*d[-2])
    if len(str(n[-1])) > len(str(d[-1])):
        count+=1
print(count)

{% endhighlight %}
