---
layout: post-euler
title:  "Project Euler Solution 019"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Counting Sundays</h2>
<div><p>You are given the following information, but you may prefer to do some research for yourself.</p><ul><li>1 Jan 1900 was a Monday.</li><li>Thirty days has September,<br/>
April, June and November.<br/>
All the rest have thirty-one,<br/>
Saving February alone,<br/>
Which has twenty-eight, rain or shine.<br/>
And on leap years, twenty-nine.</li><li>A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.</li></ul><p>How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?</p></div>

### Solution

{% highlight python %}
#pe019
import datetime

sundays = 0
for year in range(1901,2001):
	for month in range(1,13):
		if datetime.date(year,month,1).weekday()==6:
			sundays += 1
print(sundays)
{% endhighlight %}
