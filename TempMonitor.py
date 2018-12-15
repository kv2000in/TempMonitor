#Copyright kv2000in@gmail.com
#ipwebcam sensor data to CSV file
import re
#mystring = '{"ambient_temp":{"unit":"℃","data":[[1544568579352,[24.980392]],[1544568580314,[24.980392]],[1544568581275,[24.980392]],[1544568582236,[24.980392]],[1544568583194,[24.980392]],[1544568584154,[24.980392]]]}}' # each line
import time
import urllib2
#contents = urllib2.urlopen("http://192.168.1.126:8080/sensors.json?sense=ambient_temp").read()
myurl="http://192.168.1.126:8080/"
mysensor="ambient_temp"
while 1:
	myfile = open('tempdata.csv','a')
	#mystring = urllib2.urlopen("http://192.168.1.126:8080/sensors.json?sense=ambient_temp").read()
	mystring = urllib2.urlopen(myurl+"sensors.json?sense="+mysensor).read()
	myregex  = r'\S*:\S*:\S*:(\S*)]}}'
	mytxt = re.search(myregex,mystring)
	myregex1 = r'.{1,2}(\d*),\[(\d*\.\d*)\]\]'
	mytxt1=re.findall(myregex1,mytxt.group(1))
	#mytxt1[0][0] is the epoch timestamp in miliseconds of the 1st matched -returned as a tuple
	#mytxt1[0][1] is temp in deg C as float
	i = 0
	while i <len(mytxt1): 
		myfile.write(mytxt1[i][0]+","+mytxt1[i][1])
		i +=1
		myfile.write('\n')
	myfile.close()
	time.sleep(5)

