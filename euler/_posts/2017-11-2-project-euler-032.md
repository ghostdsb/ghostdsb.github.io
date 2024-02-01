---
layout: post-euler
title:  "Project Euler Solution 032"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Pandigital products</h2>
<div><p>We shall say that an <var>n</var>-digit number is pandigital if it makes use of all the digits 1 to <var>n</var> exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.</p><p>The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.</p><p>Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.</p><div>HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div></div>

### Solution

{% highlight python %}
def checkPan(a,b,m):
    digs = []
    count = 0
    for i in str(a):
        digs.append(int(i))
    for i in str(b):
        digs.append(int(i))
    for i in str(m):
        digs.append(int(i))
    pandig = [1,2,3,4,5,6,7,8,9]
    for i in pandig:
        if i in digs:
            count += 1
    if count == 9:
        print(a,b,m,digs)
        return True
    else:
        return False

sum = 0
count = 0
prods = []
for i in range(1,10):
    for j in range(1000,10000):
        if len(str(i*j))+len(str(i))+len(str(j))==9 and (i*j) not in prods:
            if checkPan(i,j,i*j):
                sum += i*j
                count +=1
                prods.append(i*j)
for i in range(10,100):
    for j in range(100,1000):
        if len(str(i*j))+len(str(i))+len(str(j))==9 and (i*j) not in prods:
            if checkPan(i,j,i*j):
                sum += i*j
                count +=1
                prods.append(i*j)
print(sum,count)
print(prods)

{% endhighlight %}
