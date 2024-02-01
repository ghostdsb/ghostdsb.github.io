---
layout: post-euler
title:  "Project Euler Solution 033"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Digit cancelling fractions</h2>
<div><p>The fraction <sup>49</sup>/<sub>98</sub> is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that <sup>49</sup>/<sub>98</sub> = <sup>4</sup>/<sub>8</sub>, which is correct, is obtained by cancelling the 9s.</p><p>We shall consider fractions like, <sup>30</sup>/<sub>50</sub> = <sup>3</sup>/<sub>5</sub>, to be trivial examples.</p><p>There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.</p><p>If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</p></div>

### Solution

{% highlight python %}
#(10*n+i)/(10*i+d) = n/d
#d(10*n + i) = n(10*i + d)
#n<d<i

prod_ntor = 1;
prod_dtor = 1;

for i in range(1,10):
    for d in range(1,i):
        for n in range(1,d):
            if d*(10*n + i) == n*(10*i + d):
                prod_ntor *= n;
                prod_dtor *= d;
print(prod_ntor/prod_dtor)

{% endhighlight %}
