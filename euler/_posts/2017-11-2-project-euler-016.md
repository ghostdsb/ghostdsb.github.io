---
layout: post-euler
title:  "Project Euler Solution 016"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Power digit sum</h2>
<div><p>2<sup>15</sup> = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.</p><p>What is the sum of the digits of the number 2<sup>1000</sup>?</p></div>

### Solution

{% highlight python %}
#pe016
num = 2**1000
sum = 0
for i in str(num):
	sum += int(i)
print(sum)
{% endhighlight %}
