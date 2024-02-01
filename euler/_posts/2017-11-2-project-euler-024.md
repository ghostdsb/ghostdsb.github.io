---
layout: post-euler
title:  "Project Euler Solution 024"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Lexicographic permutations</h2>
<div><p>A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:</p><p>012   021   102   120   201   210</p><p>What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?</p></div>

### Solution

{% highlight python %}
#pe024
import itertools

permute = itertools.permutations('0123456789',10)
perm = []
for i in permute:
	perm.append(i)
ans = ''
for value in perm[999999]:
	ans += value
print(ans)

{% endhighlight %}
