#!/usr/bin/python3
# --*-- coding:utf-8 --*--
import re
import sys
import json
import datetime

pat = re.compile('(?P<issue_date>\d+[-/]\d+[-/]\d+)')
#pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(str(line))
    if match:
        x = match.group('issue_date')
        year, month, day = (int(y) for y in x.split('-'))
        ans = datetime.date(year, month, day)
        week_day = ans.strftime("%A")
        print ('%s\t%s' % (week_day, 1))
