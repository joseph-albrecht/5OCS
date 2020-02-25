from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pytz
import re

def isItFive(requests):
    now = datetime.datetime.now()
    hour = int(now.hour)


    #get UTC offset for current time
    tz_string = datetime.datetime.now(datetime.timezone.utc).astimezone().strftime('%z')#.tzname()
    
    
    #convert offset to format we need
    if re.match("[+|-][0][0-9][0][0]$", tz_string):
    	utc_num = tz_string[0:3:2]
    	num = int(utc_num)
    	difference = 17 - hour
    	offset = num + difference

    	if offset == -12:
    		place = "Baker Islands"
    	elif offset == -11:
    		place = "Niue, New Zealand"
    	elif offset == -10:
    		place = "Honolulu"
    	elif offset == -9:
    		place = "Anchorage"
    	elif offset == -8:
    		place = "Vancouver"
    	elif offset == -7:
    		 place = "Phoenix"
    	elif offset == -6:
    		place = "Mexico City"
    	elif offset == -5:
    		place = "Havana"
    	elif offset == -4:
    		place = "La Paz"
    	else: 
    		place = 'not added yet...'

    	# typee2 = utc_num + 1
    	return  HttpResponse("It is 5oclock in  " + place)
    else:
    	utc_num = tz_string[0:3]
    	# return HttpResponse(utc_num) 
	

