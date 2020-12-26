---
layout: post-euler
title:  "Project Euler Solution 028"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Number spiral diagonals</h2>
<div><p>Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:</p><p><span><b>21</b></span> 22 23 24 <span><b>25</b></span><br/>
20  <span><b>7</b></span>  8  <span><b>9</b></span> 10<br/>
19  6  <span><b>1</b></span>  2 11<br/>
18  <span><b>5</b></span>  4  <span><b>3</b></span> 12<br/><span><b>17</b></span> 16 15 14 <span><b>13</b></span></p><p>It can be verified that the sum of the numbers on the diagonals is 101.</p><p>What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?</p></div>

### Solution

{% highlight python %}
#pe028
NE = []
SW = []
NW_SE = []
n = 1001
for i in range(1,n+1,2):
	NE.append(i**2)
for i in range(2,n,2):
	SW.append(i**2+1)
val = 1
for i in range(1,n):
	NW_SE.append(val+2*i)
	val = val+2*i
sum = sum(NE)+sum(SW)+sum(NW_SE)
#print(NE)
#print(SW)
#print(NW_SE)
print(sum)
{% endhighlight %}
