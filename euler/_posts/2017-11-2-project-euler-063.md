---
layout: post-euler
title:  "Project Euler Solution 063"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Powerful digit counts</h2>
<div><p>The 5-digit number, 16807=7<sup>5</sup>, is also a fifth power. Similarly, the 9-digit number, 134217728=8<sup>9</sup>, is a ninth power.</p><p>How many <i>n</i>-digit positive integers exist which are also an <i>n</i>th power?</p></div>

### Solution

{% highlight python %}
#pe063
counter = 0
for i in range(1,10):
	for j in range(23):
		if len(str(i**j)) == j:
			counter += 1
			print(i**j,j)
print(counter)

{% endhighlight %}
