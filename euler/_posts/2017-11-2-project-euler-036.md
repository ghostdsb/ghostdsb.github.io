---
layout: post-euler
title:  "Project Euler Solution 036"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Double-base palindromes</h2>
<div><p>The decimal number, 585 = 1001001001<sub>2</sub> (binary), is palindromic in both bases.</p><p>Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.</p><p>(Please note that the palindromic number, in either base, may not include leading zeros.)</p></div>

### Solution

{% highlight python %}
#pe036
def dtob(num):
	dec = []
	d = num
	'''
	while d!=0:
		r = d%2
		d //=2
		dec.append(r)
	for i in dec[::-1]:
		ans+=str(i)
	return int(ans)
	'''
	return bin(d)[2:]
	
sum = 0
for i in range(1,1000000):
	bin_ = dtob(i)
	if str(i)==str(i)[::-1] and str(bin_)==str(bin_)[::-1]:
		sum+=i
print(sum)
{% endhighlight %}
