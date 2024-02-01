---
layout: post-euler
title:  "Project Euler Solution 493"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Under The Rainbow</h2>
<div><p>70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.</p><p>What is the expected number of distinct colours in 20 randomly picked balls?</p><p>Give your answer with nine digits after the decimal point (a.bcdefghij).</p></div>

### Solution

{% highlight python %}
import math

def combination(a,b):
	return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
	

ans = combination(60,20)/combination(70,20)

print(7*(1-ans))
{% endhighlight %}
