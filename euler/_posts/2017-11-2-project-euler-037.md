---
layout: post-euler
title:  "Project Euler Solution 037"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Truncatable primes</h2>
<div><p>The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.</p><p>Find the sum of the only eleven primes that are both truncatable from left to right and right to left.</p><p>NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.</p></div>

### Solution

{% highlight python %}
#pe037
import primecache

def truncate_number(num):
	ret = []
	for i in range(len(str(num))):
		ret.append(int(str(num)[i:]))
		#ret.append(int(str(num)[:(-1*(i+1))]))
	return ret

def truncate_number_r(num):
	ret = []
	for i in range(len(str(num))):
		ret.append(int(str(num)[:len(str(num))-i]))
		#ret.append(int(str(num)[:(-1*(i+1))]))
	return ret

sum = 0
primes = primecache.primelist(800000)
for i in primes[4:]:
	l = truncate_number(i)
	r = truncate_number_r(i)
	there_l = 1
	for nums in l:
		if nums in primes:
			there_l *= 1
		else:
			there_l *= 0

	there_r = 1
	for nums in r:
		if nums in primes:
			there_r *= 1
		else:
			there_r *= 0
	if there_r==1 and there_l==1:
		sum += i

	if(there_l==there_r and there_l == 1):
		print(l,r,there_l,there_r)
print(sum)

# num = 1234
# ret = []
# for i in range(len(str(num))):
# 	ret.append(int(str(num)[:len(str(num))-i]))
# print(ret)

{% endhighlight %}
