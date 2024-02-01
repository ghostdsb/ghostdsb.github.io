---
layout: post-euler
title:  "Project Euler Solution 031"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Coin sums</h2>
<div><p>In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:</p><blockquote>1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).</blockquote><p>It is possible to make £2 in the following way:</p><blockquote>1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p</blockquote><p>How many different ways can £2 be made using any number of coins?</p></div>

### Solution

{% highlight python %}
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print(ways[target])

{% endhighlight %}
