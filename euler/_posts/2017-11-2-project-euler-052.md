---
layout: post-euler
title:  "Project Euler Solution 052"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Permuted multiples</h2>
<div><p>It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.</p><p>Find the smallest positive integer, <i>x</i>, such that 2<i>x</i>, 3<i>x</i>, 4<i>x</i>, 5<i>x</i>, and 6<i>x</i>, contain the same digits.</p></div>

### Solution

{% highlight python %}
for i in range(99999,9999999):
    oneX = [int(d) for d in str(i)]
    oneX = set(oneX)

    twoX = [int(d) for d in str(2*i)]
    twoX = set(twoX)

    threeX = [int(d) for d in str(3*i)]
    threeX = set(threeX)

    fourX = [int(d) for d in str(4*i)]
    fourX = set(fourX)

    fiveX = [int(d) for d in str(5*i)]
    fiveX = set(fiveX)

    sixX = [int(d) for d in str(6*i)]
    sixX = set(sixX)

    if oneX==twoX and twoX==threeX and threeX==fourX and fourX==fiveX and sixX==fiveX:
        print(i)
        break

{% endhighlight %}
