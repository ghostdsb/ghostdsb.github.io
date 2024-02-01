---
layout: post-euler
title:  "Project Euler Solution 076"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Counting summations</h2>
<div><p>It is possible to write five as a sum in exactly six different ways:</p><p>4 + 1<br/>
3 + 2<br/>
3 + 1 + 1<br/>
2 + 2 + 1<br/>
2 + 1 + 1 + 1<br/>
1 + 1 + 1 + 1 + 1</p><p>How many different ways can one hundred be written as a sum of at least two positive integers?</p></div>

### Solution

{% highlight python %}
target = 100
ways = [0]*(target+1)
ways[0] = 1
for i in range(1,100):
    for j in range(i,101):
        ways[j] += ways[j-i]
print(ways[-1])

{% endhighlight %}
