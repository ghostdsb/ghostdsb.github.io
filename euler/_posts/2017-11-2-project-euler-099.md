---
layout: post-euler
title:  "Project Euler Solution 099"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Largest exponential</h2>
<div><p>Comparing two numbers written in index form like 2<sup>11</sup> and 3<sup>7</sup> is not difficult, as any calculator would confirm that 2<sup>11</sup> = 2048 < 3<sup>7</sup> = 2187.</p><p>However, confirming that 632382<sup>518061</sup> > 519432<sup>525806</sup> would be much more difficult, as both numbers contain over three million digits.</p><p>Using <a>base_exp.txt</a> (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.</p><p>NOTE: The first two lines in the file represent the numbers in the example given above.</p></div>

### Solution

{% highlight python %}
import math

with open("p099_base_exp.txt") as b:
    be = b.read().split("\n")

max_num = -1
ind = 0
found = -1
nums = []
for i in be:
    nums.append(i.split(","))



for i in range(len(nums)):
    ind += 1
    val = math.log(int(nums[i][0]),10)*int(nums[i][1])
    if val > max_num:
        max_num = val
        found = ind
print(max_num,found)

{% endhighlight %}
