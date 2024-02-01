---
layout: post-euler
title:  "Project Euler Solution 003"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Largest prime factor</h2>
<div><p>The prime factors of 13195 are 5, 7, 13 and 29.</p><p>What is the largest prime factor of the number 600851475143 ?</p></div>

### Solution

{% highlight python %}
#pe003
num = 600851475143
r = 2
lim = num
while num>1 and num<=lim: 
	if num%r == 0:
		num = num / r
	else:	
		r += 1
print(r)
{% endhighlight %}
