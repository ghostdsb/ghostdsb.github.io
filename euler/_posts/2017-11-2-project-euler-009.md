---
layout: post-euler
title:  "Project Euler Solution 009"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Special Pythagorean triplet</h2>
<div><p>A Pythagorean triplet is a set of three natural numbers, <var>a</var> < <var>b</var> < <var>c</var>, for which,</p><div><var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> = <var>c</var><sup>2</sup></div><p>For example, 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>.</p><p>There exists exactly one Pythagorean triplet for which <var>a</var> + <var>b</var> + <var>c</var> = 1000.<br/>Find the product <var>abc</var>.</p></div>

### Solution

{% highlight python %}
#pe09

n = 1000
ans = 0
for a in range(n//3,0,-1):
	b = (2*n*a - n**2)//(2*(a-n))
	c = n-a-b
	if c**2 == a**2 + b**2  and c>a and c>b and b>a:
		ans = a*b*c
		print(a,b,c,ans)
print(ans)
{% endhighlight %}
