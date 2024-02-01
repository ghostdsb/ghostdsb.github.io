---
layout: post-euler
title:  "Project Euler Solution 085"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Counting rectangles</h2>
<div><p>By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:</p><div><img/></div><p>Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.</p></div>

### Solution

{% highlight python %}
import mathtools,math

limit = 2*10**6
min = 10**10
m,n = 0,0
for i in range(100):
	for j in range(100):
		ans = i*(i+1)*j*(j+1)/4
		d = abs(ans-limit)
		if d < min:
			min = d
			m,n = i,j
print(m,n,m*n)
			


{% endhighlight %}
