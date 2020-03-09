from django.shortcuts import render
from django.http import HttpResponse
import datetime

def utcOffsetWhereTheHourIs(target_hour):
    """Return the UTC offset where the hour is currently the target_hour."""
    
    utc_hour   = datetime.datetime.now(datetime.timezone.utc).hour
    utc_offset = target_hour - utc_hour

    if abs(utc_offset) > 12:
        utc_offset = goAroundTheWorldTheOtherWay(utc_offset)

    return utc_offset

def goAroundTheWorldTheOtherWay(offset):
    """Because the earth is a globe, a particular timezone can be reached going
       eastward or westward. This function returns a new utc offset going the
       other cardinal direction.
       Examples:
       -14 ->  10
        14 -> -10"""

    new_magnitude = 24 - abs(offset)
    old_direction = (offset // abs(offset))
    new_direction = old_direction * -1

    return new_magnitude * new_direction
    
def isItFive(requests):
    utc_offset = utcOffsetWhereTheHourIs(17)

    place = {-12: "Baker Islands",
             -11: "Niue, New Zealand",
             -10: "Honolulu",
              -9: "Anchorage",
              -8: "Vancouver",
              -7: "Phoenix",
              -6: "Mexico City",
              -5: "Havana",
              -4: "La Paz",
              -3: "Sao Paulo",
              -2: "South Georgia",
              -1: "Cape Verde",
               0: "Reykjavic",
               1: "Brazzaville",
               2: "Cairo",
               3: "Mecca",
               4: "Yerevan",
               5: "Maldives",
               6: "Dhaka, Bangladesh",
               7: "Bangkok",
               8: "Taipei",
               9: "Seoul",
              10: "Guam",
              11: "Solomon Islands",
              12: "Baker Islands"}[utc_offset]

    return  HttpResponse("It is 5oclock in  " + place)
