---
layout: post-euler
title:  "Project Euler Solution 048"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Self powers</h2>
<div><p>The series, 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> + ... + 10<sup>10</sup> = 10405071317.</p><p>Find the last ten digits of the series, 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> + ... + 1000<sup>1000</sup>.</p></div>

### Solution

{% highlight python %}
#pe048
ans = 0
for i in range(1,1001):
	ans += i**i
print(str(ans)[-10:])

{% endhighlight %}
