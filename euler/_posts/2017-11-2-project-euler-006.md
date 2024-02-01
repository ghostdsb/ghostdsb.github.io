---
layout: post-euler
title:  "Project Euler Solution 006"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Sum square difference</h2>
<div><p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p><p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p></div>

### Solution

{% highlight python %}
#pe006
n = 100
sum_of_square = n*(n+1)*(2*n+1)//6
square_of_sum = (n*(n+1)//2)**2
ans = abs(sum_of_square-square_of_sum)
print(ans)
{% endhighlight %}
