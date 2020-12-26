---
layout: post-euler
title:  "Project Euler Solution 034"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Digit factorials</h2>
<div><p>145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.</p><p>Find the sum of all numbers which are equal to the sum of the factorial of their digits.</p><p>Note: As 1! = 1 and 2! = 2 are not sums they are not included.</p></div>

### Solution

{% highlight python %}
#pe034
import math
ans = 0
for i in range(3,99999):
	sum = 0
	for j in str(i):
		sum += math.factorial(int(j))
	if sum == i:
		ans += i
print(ans)
{% endhighlight %}
