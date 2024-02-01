---
layout: post-euler
title:  "Project Euler Solution 112"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Bouncy numbers</h2>
<div><p>Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.</p><p>Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.</p><p>We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.</p><p>Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.</p><p>Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.</p><p>Find the least number for which the proportion of bouncy numbers is exactly 99%.</p></div>

### Solution

{% highlight python %}
def checkBounce(num):
	bounce = {'UP':0,'DOWN':0}
	for i in range(len(str(num))-1):
		if int(str(num)[i])>int(str(num)[i+1]):
			bounce['DOWN']+=1
		elif int(str(num)[i])<int(str(num)[i+1]):
			bounce['UP'] +=1
	if bounce['UP'] != 0 and bounce['DOWN']!=0:
		return True
	else:
		return False
		
counter = 0
perc = 0
i = 100
limit = 99
while perc <= limit:
	if checkBounce(i):
		counter += 1
	perc = counter*100/(i)
	i += 1
	
print(i-2)

		
{% endhighlight %}
