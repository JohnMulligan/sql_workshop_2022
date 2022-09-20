import re

d=open('codebook.txt','r')
t=d.read()
d.close()

tablename=''

lines=t.split('\n')

tables={}

linenumber=1

for line in lines:
	
	integrityfail=False
	#data type checking (very basic for now)
	try:
		tablename,colname,coldatatype,colsize,colallownull,coldescription=[i.strip() for i in line.split('\t')]
	except:
		integrityfail=True
	
	try:
		int(colsize)		
	except:
		integrityfail=True
	if colallownull not in ['','NO']:
		integrityfail=True
	if colname=='':
		integrityfail=True
	
	if integrityfail:
		print("data error in line %d" %linenumber)
		print(line)
		exit()
	
	linedata=[colname,coldatatype,colsize,colallownull,coldescription]
	if tablename not in tables:
		tables[tablename]=[]
	tables[tablename].append(linedata)
	
	linenumber+=1

for table in tables:
	formattedcols=[]
	for column in tables[table]:
		colname,coldatatype,colsize,colallownull,coldescription=column
		formattedcol="`%s` %s(%s)" %(colname,coldatatype,colsize)
		if colallownull=="NO":
			formattedcol += ' NOT NULL'
		if coldescription != '':
			cleancoldescription=re.sub("'","",coldescription)
			formattedcol += ' COMMENT \'%s\'' %cleancoldescription
		coldescription +=';'
		formattedcols.append(formattedcol)
	formattedcols_str=",\n".join(formattedcols)
	createtablestatement="CREATE TABLE %s (%s);" %(table,formattedcols_str)
	
	print('\n',createtablestatement,'\n')