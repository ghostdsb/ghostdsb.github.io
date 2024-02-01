---
layout: post-euler
title:  "Project Euler Solution 023"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Non-abundant sums</h2>
<div><p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.</p><p>A number <var>n</var> is called deficient if the sum of its proper divisors is less than <var>n</var> and it is called abundant if this sum exceeds <var>n</var>.</p><p>As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p><p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p></div>

### Solution

{% highlight python %}
#pe023
import math

def divsum(n):
	divs = []
	divs.append(1)
	for i in range(2,int(round(math.sqrt(n),0))+1):
		if n%i == 0:
			divs.append(i)
			if n//i not in divs:
				divs.append(n//i)
	return sum(divs)

end = 28123
abundant = []
for i in range(1,end+1):
	if divsum(i)>i:
		abundant.append(i)		


not_sum = [False]*(end+1)
for x in abundant:
	for y in abundant:
		if x+y<(end+1):
			not_sum[x+y] = True

sum = 0
for i,b in enumerate(not_sum):
	if not b:
		sum += i
print(sum)
{% endhighlight %}
