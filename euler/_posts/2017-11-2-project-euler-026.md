---
layout: post-euler
title:  "Project Euler Solution 026"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Reciprocal cycles</h2>
<div><p>A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:</p><blockquote><table><tr><td><sup>1</sup>/<sub>2</sub></td><td>= </td><td>0.5</td></tr><tr><td><sup>1</sup>/<sub>3</sub></td><td>= </td><td>0.(3)</td></tr><tr><td><sup>1</sup>/<sub>4</sub></td><td>= </td><td>0.25</td></tr><tr><td><sup>1</sup>/<sub>5</sub></td><td>= </td><td>0.2</td></tr><tr><td><sup>1</sup>/<sub>6</sub></td><td>= </td><td>0.1(6)</td></tr><tr><td><sup>1</sup>/<sub>7</sub></td><td>= </td><td>0.(142857)</td></tr><tr><td><sup>1</sup>/<sub>8</sub></td><td>= </td><td>0.125</td></tr><tr><td><sup>1</sup>/<sub>9</sub></td><td>= </td><td>0.(1)</td></tr><tr><td><sup>1</sup>/<sub>10</sub></td><td>= </td><td>0.1</td></tr></table></blockquote><p>Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that <sup>1</sup>/<sub>7</sub> has a 6-digit recurring cycle.</p><p>Find the value of <i>d</i> < 1000 for which <sup>1</sup>/<sub><i>d</i></sub> contains the longest recurring cycle in its decimal fraction part.</p></div>

### Solution

{% highlight python %}
#pe026
max = 0 
for i in range(2,1001):
	decimal = []
	remainder = []
	number = 10**(len(str(i)))
	for j in range(len(str(number))-2):
		decimal.append(0)
	r = -1
	while r not in remainder[:-1] :
		d = number//i
		r = number%i
		decimal.append(d)
		remainder.append(r)
		number = r*10
	idx = remainder.index(r)
	#print(i,end = " 0.")
	#print(*decimal)
	if len(decimal)>max:
		max = i
print(max)
	
		
	

{% endhighlight %}
