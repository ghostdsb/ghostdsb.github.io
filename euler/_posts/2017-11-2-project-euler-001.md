---
layout: post-euler
title:  "Project Euler Solution 001"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Multiples of 3 and 5</h2>
<div><p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p><p>Find the sum of all the multiples of 3 or 5 below 1000.</p></div>

### Solution

{% highlight python %}
#pe001
arr = [x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(arr))

{% endhighlight %}
