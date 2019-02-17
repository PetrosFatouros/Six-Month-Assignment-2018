#ASKHSH 3

f=open("source.py","r")
content=f.readlines()
f.close()
f=open('source.py','w').close()
f=open('source.py','a')
for line in content:
	if "#" in line:
		grammh=line.strip()
		if grammh[0]!="#":
			tmp=line.split("#")
			mona=tmp[0].count("'")
			dipla=tmp[0].count('"')
			if mona%2==1 or dipla%2==1:
				f.write(line)
			else:
				f.write(line.split("#")[0])
	else:
		f.write(line)
f.close()
