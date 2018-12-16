#!/usr/bin/python
#Copyright kv2000in@gmail.com
#ipwebcam sensor data to CSV file
#Usage : python TempMonitor.py http://192.168.1.126:8080/ ambient_temp
# Will save ambient_temp data in dateambient_temp.csv file
#Will run the script at reboot - file name for CSV will change with the change in date
#Available sensors (Depends on what has been enabled in the ipwebcam app 
#battery_level,humidity,ambient_temp,battery_temp,light,battery_voltage 
import sys
import re
import time
import urllib2
import datetime
myurl = sys.argv[1] # url passed as arg
mysensor = sys.argv[2] # one sensor at a time - passed as an arg f
timeTosleep = 5 # ipwebcam has setting - how long to keep the sensor data for (in seconds). Set at 5 seconds in ipwebcam
while 1:
	#Open .csv file
	myfile = open(datetime.datetime.today().strftime('%m-%d-%Y')+mysensor+'.csv','a')
	try:
		#read json file
		mystring = urllib2.urlopen(myurl+"sensors.json?sense="+mysensor).read()
		myregex  = r'\S*:\S*:\S*:(\S*)]}}'#\S any non whitespace, * any number of non whitespaces, 
		mytxt = re.search(myregex,mystring) #this regex will just capture the data from json
		myregex1 = r'.{1,2}(\d*),\[(\d*\.\d*)\]\]' 
		mytxt1=re.findall(myregex1,mytxt.group(1)) #This regex will capture ALL the matches with [0] being timestamp and [1] being value
		i = 0
		while i <len(mytxt1): 
			myfile.write(mytxt1[i][0]+","+mytxt1[i][1])#write this as a CSV format
			i +=1
			myfile.write('\n')
	except URLError:
		print "URLError"
	myfile.close()
	time.sleep(timeTosleep)
