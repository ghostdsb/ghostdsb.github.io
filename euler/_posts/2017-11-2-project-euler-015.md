---
layout: post-euler
title:  "Project Euler Solution 015"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Lattice paths</h2>
<div><p>Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.</p><div><img/></div><p>How many such routes are there through a 20×20 grid?</p></div>

### Solution

{% highlight python %}
#pe015
import math
print(math.factorial(40)//(math.factorial(20))**2)
{% endhighlight %}
