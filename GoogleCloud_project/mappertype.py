#!/usr/bin/python3
# --*-- coding:utf-8 --*--
import re
import sys
import json
import datetime

pat = re.compile('(?P<issue_date>\d+[-/]\d+[-/]\d+)')



for line in sys.stdin:
    try:
        #FIND THE ELEMENT YEAR, AND THEN THE ELEMENT TYPE
        #YEAR
        car_year = re.findall(r"vehicle_year': '(.+?['])", str(line)) #x is a LIST OBJECT TYPE
        new_car_year = [c[:-1] for c in car_year] #Excluding the last character of each new_car_year, which is a ' (quotation mark)
        if int(new_car_year[0]) > 999: #error handler in case that year is missing
        
            #TYPE
            car_type = re.findall(r"vehicle_body_type': '(.+?['])", str(line)) #car_type is a LIST OBJECT TYPE
            new_car_type = [c[:-1] for c in car_type] #Excluding the last character of each new_car_type, which is a ' (quotation mark)

            info_concat = f'{new_car_type[0]} - {new_car_year[0]}'

            print('%s\t%s' % (info_concat, 1)) #since new_x is a LIST, new_x[0] is the first element of that, which is the car type
        
        else:
            continue
            
    except:
        continue
