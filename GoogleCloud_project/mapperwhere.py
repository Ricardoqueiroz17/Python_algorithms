#!/usr/bin/python3
# --*-- coding:utf-8 --*--
import re
import sys
import json
import datetime

pat = re.compile('(?P<issue_date>\d+[-/]\d+[-/]\d+)')
#pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    try:
        #FIND THE LOCATION
        street_issued = re.findall(r"street_name': '(.+?['])", str(line)) #street_issued is a LIST OBJECT TYPE
        new_street_issued = [c[:-1] for c in street_issued] #Excluding the last character of each list[0], which is a ' (quotation mark)
        
        #.REPLACE TERMS: Since there are names with ST and without ST, but are the same street, and other terms, we run this .replace methods below
        x = new_street_issued[0]
        x= x.replace(' ST', '') 
        x= x.replace(' STREET', '')
        x= x.replace('REET', '')
        x= x.replace(' PL', 'PLACE')
        x= x.replace(' PK', 'PARK')
        x= x.replace(' ROAD', 'RD')
        
        print('%s\t%s' % (x, 1)) #since new_x is a LIST, new_x[0] is the first element of that, which is the car type
            
    except:
        continue
