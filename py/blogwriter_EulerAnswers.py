import os,re

with open(r'F:\ghost_dsb\templates\eulertemplates\1.txt') as t:
	text1 = t.read()
with open(r'F:\ghost_dsb\templates\eulertemplates\2.txt') as t:
	text2 = t.read()
with open(r'F:\ghost_dsb\templates\eulertemplates\3.txt') as t:
	text3 = t.read()
with open(r'F:\ghost_dsb\templates\eulertemplates\4.txt') as t:
	text4 = t.read()
with open(r'F:\ghost_dsb\templates\eulertemplates\5.txt') as t:
	text5 = t.read()

eulerFolder = r'F:\ghost_dsb\euler\Euler solutions'

for file in os.listdir(eulerFolder):
	seeFile = eulerFolder+'\\'+file
	with open(seeFile) as t:
		code = t.read()
	
	num = re.compile(r'^pe(\d\d\d)')
	title = num.search(file).group(1)
	
	pelink = str(int(title))
	
	blog = text1 + pelink + text2 + pelink + text3 + pelink + text4 + code + text5
	
	blogFileName = title + '.html' 
	blogFileFolder = r'F:\ghost_dsb\euler'
	blogLocation = blogFileFolder + '\\' + blogFileName
	
	writer = open(blogLocation,'w')
	writer.write(blog)
	writer.close()
	
	