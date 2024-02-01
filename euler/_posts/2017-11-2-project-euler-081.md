---
layout: post-euler
title:  "Project Euler Solution 081"
date:   2017-11-2 15:23:25 +0530
category: Euler
---

<h2>Path sum: two ways</h2>
<div><p>In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by <b>only moving to the right and down</b>, is indicated in bold red and is equal to 2427.</p><div>
$$
\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & \color{red}{746} & \color{red}{422} & 111\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$
</div><p>Find the minimal path sum from the top left to the bottom right by only moving right and down in <a>matrix.txt</a> (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.</p></div>

### Solution

{% highlight python %}
matrix = []
with open('p081_matrix.txt')as m:
	mat = m.read().split("\n")

for i in mat:
	lst = i.split(",")
	matrix.append(lst)
matrix.pop()

summ = 0
size = 80
for i in range(78,-1,-1):
	matrix[79][i] = str(int(matrix[79][i]) + int(matrix[79][i+1]))
	matrix[i][79] = str(int(matrix[i][79]) + int(matrix[i+1][79]))

for i in range(78,-1,-1):
	for j in range(78,-1,-1):
		matrix[i][j] = str(int(matrix[i][j]) + min(int(matrix[i+1][j]),int(matrix[i][j+1])))
print(matrix[0][0])

{% endhighlight %}
