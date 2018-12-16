#Copyright kv2000in@gmail.com
myfile = open('ambient_temp.csv','r')
myX=[]
myY=[]
for myline in myfile:
	myNewLine = myline.rstrip()
	myXelement = myNewLine.split(',')[0]
	myYelement = myNewLine.split(',')[1]
	myX.append(myXelement)
	myY.append(myYelement)
myfile.close()
myfile.open('ambient_temp.js','a')
myfile.write('traceX=')
myfile.write(str(myX))
myfile.write(';')
myfile.write('traceY=')
myfile.write(str(myY))
myfile.write(';')
myfile.close()	
