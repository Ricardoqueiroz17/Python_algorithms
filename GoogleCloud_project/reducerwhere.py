#!/usr/bin/python3
from operator import itemgetter
import sys

list_log=[]
for line in sys.stdin:
    line = line.strip()
    list_log.append(line)

dict_ip_count = {}
   
for line in list_log:
    issue_date, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[issue_date] = dict_ip_count.get(issue_date, 0) + num
    except ValueError:
        pass
    else:
        next

print ('Rank of the 20 streets where tickets are most issued')
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1),reverse=True)
dict_items = list(sorted_dict_ip_count[0:20])
for ip, count in dict_items:
    print ('%s\t%s' % (ip, count))
