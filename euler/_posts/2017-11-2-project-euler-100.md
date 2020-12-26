---
layout: post-euler
title:  "Project Euler Solution 100"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Arranged probability</h2>
<div><p>If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.</p><p>The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.</p><p>By finding the first arrangement to contain over 10<sup>12</sup> = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.</p></div>

### Solution

{% highlight python %}
b0 = 15
n0 = 21

limit = 10**12

while True:
	b = 3*b0 + 2*n0 - 2
	n = 4*b0 + 3*n0 - 3
	b0 = b
	n0 = n
	if n > limit:
		break
print(b)
{% endhighlight %}
