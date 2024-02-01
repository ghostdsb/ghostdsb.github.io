---
layout: post-euler
title:  "Project Euler Solution 060"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Prime pair sets</h2>
<div><p>The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.</p><p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p></div>

### Solution

{% highlight python %}
import mathtools
primes = mathtools.primelist(20000)
print(primes)
{% endhighlight %}
