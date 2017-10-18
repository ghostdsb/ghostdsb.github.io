import os,re

with open(r'F:\ghost_dsb\templates\eulertemplates\eulermain1.txt') as t:
	text1 = t.read()
with open(r'F:\ghost_dsb\templates\eulertemplates\eulermain2.txt') as t:
	text2 = t.read()

eulerFolder = r'F:\ghost_dsb\euler\Euler solutions'
blog = ''
for file in os.listdir(eulerFolder):
	seeFile = eulerFolder+'\\'+file
	
	num = re.compile(r'^pe(\d\d\d)')
	
	t = num.search(file).group(1)
	title = t + '.html'
	
	
	quesNumber = str(int(t))
	
	#print(file,seeFile,quesNumber,title)
	blog += '<a href="euler/'+ title+ '"><h3>Solution to Project Euler Problem ' + quesNumber + '</h3></a><hr>'
	print(blog)


blogLocation = r'F:\ghost_dsb\euler.html'
blog = text1 + blog + text2

writer = open(blogLocation,'w')
writer.write(blog)
writer.close()
	
	