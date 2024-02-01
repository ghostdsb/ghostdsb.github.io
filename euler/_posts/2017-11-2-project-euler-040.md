---
layout: post-euler
title:  "Project Euler Solution 040"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Champernowne's constant</h2>
<div><p>An irrational decimal fraction is created by concatenating the positive integers:</p><p>0.12345678910<span>1</span>112131415161718192021...</p><p>It can be seen that the 12<sup>th</sup> digit of the fractional part is 1.</p><p>If <i>d</i><sub><i>n</i></sub> represents the <i>n</i><sup>th</sup> digit of the fractional part, find the value of the following expression.</p><p><i>d</i><sub>1</sub> × <i>d</i><sub>10</sub> × <i>d</i><sub>100</sub> × <i>d</i><sub>1000</sub> × <i>d</i><sub>10000</sub> × <i>d</i><sub>100000</sub> × <i>d</i><sub>1000000</sub></p></div>

### Solution

{% highlight python %}
#pe040
d = '.'+''.join(str(i) for i in range(1,1000000))
p = 1
for i in range(7):
	p *= int(d[10**i])
print(p)
{% endhighlight %}
