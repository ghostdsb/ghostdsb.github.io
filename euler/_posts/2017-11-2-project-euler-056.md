---
layout: post-euler
title:  "Project Euler Solution 056"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Powerful digit sum</h2>
<div><p>A googol (10<sup>100</sup>) is a massive number: one followed by one-hundred zeros; 100<sup>100</sup> is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.</p><p>Considering natural numbers of the form, <i>a<sup>b</sup></i>, where <i>a, b</i> < 100, what is the maximum digital sum?</p></div>

### Solution

{% highlight python %}
#pe056
def digsum(num):
	sum = 0
	for d in str(num):
		sum += int(d)
	return sum

max = -1
for a in range(101):
	for b in range(101):
		num = a**b
		dsum = digsum(num)
		if dsum>max:
			max = dsum
print(max)

{% endhighlight %}
