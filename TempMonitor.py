#Copyright kv2000in@gmail.com
#ipwebcam sensor data to CSV file
#Usage : python TempMonitor.py http://192.168.1.126:8080/ ambient_temp
# Will save ambient_temp data in ambient_temp.csv file
import sys
import re
import time
import urllib2
myurl = sys.argv[1]
mysensor = sys.argv[2]
while 1:
	myfile = open(datetime.datetime.today().strftime('%m-%d-%Y')+mysensor+'.csv','a')
	mystring = urllib2.urlopen(myurl+"sensors.json?sense="+mysensor).read()
	myregex  = r'\S*:\S*:\S*:(\S*)]}}'#\S any non whitespace
	mytxt = re.search(myregex,mystring)
	myregex1 = r'.{1,2}(\d*),\[(\d*\.\d*)\]\]'
	mytxt1=re.findall(myregex1,mytxt.group(1))
	i = 0
	while i <len(mytxt1): 
		myfile.write(mytxt1[i][0]+","+mytxt1[i][1])
		i +=1
		myfile.write('\n')
	myfile.close()
	time.sleep(5)
