#!/usr/bin/python
#Copyright kv2000in@gmail.com
#Generates HTML and JS file with arrays needed to plot the sensor data
#Will run the script at 23:59 - use same days CSV file 
import datetime
import sys
#pass name of the sensor as argument to the script
#Available sensors (Depends on what has been enabled in the ipwebcam app 
#battery_level,humidity,ambient_temp,battery_temp,light,battery_voltage 
mysensor=sys.argv[1]
#open yesterday's temperature data csv file
#myfile = open((datetime.datetime.today()-datetime.timedelta(1)).strftime('%m-%d-%Y')+'ambient_temp.csv','r')
#open today's csv file - running at 23:59 everyday
myfile = open(datetime.datetime.today().strftime('%m-%d-%Y')+mysensor+'.csv','r')
myX=[]
myY=[]
myJSfilename="./html/scripts/"+datetime.datetime.today().strftime('%m-%d-%Y')+mysensor+".js"
myHTMLfilename="./html/"+datetime.datetime.today().strftime('%m-%d-%Y')+"-"+mysensor+"Plot.html"
myJSfilenameForHTML = datetime.datetime.today().strftime('%m-%d-%Y')+mysensor+".js"
for myline in myfile:
	myNewLine = myline.rstrip() #remove the trailing whitespaces
	#myXelement=datetime.datetime.fromtimestamp(float(myNewLine.split(',')[0])/1000).strftime('%Y-%m-%d %H:%M:%S')#convert timestamp from milliseconds to seconds, format it so that plotly plots correctly
	myXelement=datetime.datetime.fromtimestamp(float(myNewLine.split(',')[0])).strftime('%Y-%m-%d %H:%M:%S') #Already saving in seconds instead of millis in csv files
	myYelement = myNewLine.split(',')[1]
	myX.append(myXelement)
	myY.append(myYelement)
myfile.close()
#Create the JS file with two arrays which will be used by plotly
myfile = open(myJSfilename,'w')
myfile.write('traceX=')
myfile.write(str(myX))
myfile.write(';')
myfile.write('traceY=')
myfile.write(str(myY))
myfile.write(';')
myfile.close()
#create the HTML file
myHTML = """ <!DOCTYPE html>
	<html>
	<!-- 	 
	-->
	<head>
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
	<meta http-equiv="Content-Language" content="hi" />
	<title>Temp Graph</title>
	<style>
	* {
	box-sizing: border-box;
	}
	
	html {
	font-family: "Lucida Sans", sans-serif;
	font-size: 100%;
	}
	
	[class*="col-"] {
	float: left;
	padding-left: 15px;
	padding-right: 15px;
	}
	
	/* For mobile phones: */
	[class*="col-"] {
	width: 100%;
	}
	.topright{
	height:160px;
	}
	
	@media only screen and (min-width: 768px) {
	/* For desktop: */ .col-1 {
	width: 8.33%;
	}
	
	.col-2 {
	width: 16.66%;
	}
	
	.col-3 {
	width: 25%;
	}
	
	.col-4 {
	width: 33.33%;
	}
	
	.col-5 {
	width: 41.66%;
	}
	
	.col-6 {
	width: 50%;
	}
	
	.col-7 {
	width: 58.33%;
	}
	
	.col-8 {
	width: 66.66%;
	}
	
	.col-9 {
	width: 75%;
	}
	
	.col-10 {
	width: 83.33%;
	}
	
	.col-11 {
	width: 91.66%;
	}
	
	.col-12 {
	width: 100%;
	}
	
	.topright{
	
	margin-top:160px;
	height:290px;
	}
	}
	
	
	/* For mobile*/
	
	ul {
	list-style-type: none;
	margin: 0;
	padding: 0;
	}
	
	.digitaldisplay {
	color: #2509e8;
	text-align: center;
	width: 40px;
	float: left;
	font-weight: bold;
	padding-top: 5px;
	padding-bottom: 5px;
	font-size: x-large;
	position: absolute;
	z-index: -1;
	margin-left: 15px;
	}
	
	.Psensordisplay{
	color:blue;
	}
	.Tsensordisplay{
	color:blue;
	}
	.topleft{
	
	margin-top:160px;
	}
	
	
	
	</style>
	<script src="./scripts/plotly.js" type="text/javascript" charset="utf-8"></script>
	<script src="./scripts/
	"""
myHTML+=myJSfilenameForHTML
myHTML+="""
	" type="text/javascript" charset="utf-8"></script>
	
	</head>
	<!--<body onload="queryServer3()"> -->
	<body style="margin:0;" onload = 'drawplot();'>
	<!-- supported tags for onload event <body>, <frame>, <iframe>, <img>, <input type="image">, <link>, <script>, <style> -->
	<div style="width:100%;"> 
	
	
	<div id="9ab6bde0-5a69-4f53-a80c-d2e19447d850" class="plotly-graph-div"></div>
	</div>
	
	
	
	
	
	
	
	
	
	<script type="text/javascript">
	function drawplot(){ 
	/* to do - if data lengths are not equal - graphs not plotted -option 1 : send equal length data from the server , option 2: chop the data to equal length, non-empty arrays on the client side
	*** problem is on the client side - JS stopping execution midway
	*/
	
	window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("9ab6bde0-5a69-4f53-a80c-d2e19447d850", [{"y": traceY, "x": traceX, "type": "scatter", "name": "Tank 1","mode":"markers"}], {"xaxis": {"ticks": "outside", "tickwidth": 4, "tick0": 0, "ticklen": 8, "dtick": 0.25, "tickcolor": "#000", "autotick": true}, "yaxis": {"ticks": "outside", "tickwidth": 4, "tick0": 0, "ticklen": 8, "dtick": 0.25, "tickcolor": "#000", "autotick": true}}, {"linkText": "Export to plot.ly", "showLink": false})
	};
	/*window.removeEventListener("resize");*/
	window.addEventListener("resize", function(){Plotly.Plots.resize(document.getElementById("9ab6bde0-5a69-4f53-a80c-d2e19447d850"));});
	window.removeEventListener("resize", function(){Plotly.Plots.resize(document.getElementById("9ab6bde0-5a69-4f53-a80c-d2e19447d850"));});
	
	
	
	</script>
	
	</body>
	</html>
	
"""
myfile = open(myHTMLfilename,'w')
myfile.write(myHTML)
myfile.close()

