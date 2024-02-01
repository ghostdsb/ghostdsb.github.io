---
layout: post-euler
title:  "Project Euler Solution 065"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Convergents of e</h2>
<div><p>The square root of 2 can be written as an infinite continued fraction.</p><p>$\sqrt{2} = 1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + ...}}}}$</p><p>The infinite continued fraction can be written, $\sqrt{2} = [1; (2)]$, $(2)$ indicates that 2 repeats <i>ad infinitum</i>. In a similar way, $\sqrt{23} = [4; (1, 3, 1, 8)]$.</p><p>It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for $\sqrt{2}$.</p><p>$
1 + \dfrac{1}{2} = \dfrac{3}{2}\\
1 + \dfrac{1}{2 + \dfrac{1}{2}} = \dfrac{7}{5}\\
1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2}}} = \dfrac{17}{12}\\
1 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2 + \dfrac{1}{2}}}} = \dfrac{41}{29}
$</p><p>Hence the sequence of the first ten convergents for $\sqrt{2}$ are:</p><p>$1, \dfrac{3}{2}, \dfrac{7}{5}, \dfrac{17}{12}, \dfrac{41}{29}, \dfrac{99}{70}, \dfrac{239}{169}, \dfrac{577}{408}, \dfrac{1393}{985}, \dfrac{3363}{2378}, ...$</p><p>What is most surprising is that the important mathematical constant,<br/>$e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...]$.</p><p>The first ten terms in the sequence of convergents for <i>e</i> are:</p><p>$2, 3, \dfrac{8}{3}, \dfrac{11}{4}, \dfrac{19}{7}, \dfrac{87}{32}, \dfrac{106}{39}, \dfrac{193}{71}, \dfrac{1264}{465}, \dfrac{1457}{536}, ...$</p><p>The sum of digits in the numerator of the 10<sup>th</sup> convergent is $1 + 4 + 5 + 7 = 17$.</p><p>Find the sum of digits in the numerator of the 100<sup>th</sup> convergent of the continued fraction for $e$.</p></div>

### Solution

{% highlight python %}
import math

def sumOfDigits(num):
	sum = 0
	for d in str(num):
		sum += int(d)
	return sum

interger = 2
convergent = []
convergent.append(1)
convergent.append(2)
i = 0
k = 1
while len(convergent) <= 100:
	i += 1
	if i%3 != 0:
		convergent.append(1)
	else:
		k += 1
		convergent.append(2*k)

n0 = 1
n1 = 2
for i in range(99):
	c = convergent[i]
	n = c*n1 + n0
	n0 = n1
	n1 = n
	
ans = sumOfDigits(n1)
print(ans)
		


		

{% endhighlight %}
