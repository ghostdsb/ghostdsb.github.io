---
layout: post-euler
title:  "Project Euler Solution 062"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Cubic permutations</h2>
<div><p>The cube, 41063625 (345<sup>3</sup>), can be permuted to produce two other cubes: 56623104 (384<sup>3</sup>) and 66430125 (405<sup>3</sup>). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.</p><p>Find the smallest cube for which exactly five permutations of its digits are cube.</p></div>

### Solution

{% highlight python %}
def digitList(num):
    dl = []
    for i in str(num):
        dl.append(int(i));
    dl.sort()
    return dl

limit = 10000
ans = 0
for i in range(5000,limit):
    count = 0
    j = i+1

    while len(digitList(i**3)) == len(digitList(j**3)):
        if digitList(i**3) == digitList(j**3):
            count += 1
        j += 1
    if count == 4:
        ans = i
        break
    print(i,count)

print(ans,ans**3)



{% endhighlight %}
