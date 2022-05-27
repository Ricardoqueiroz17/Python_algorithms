#!/usr/bin/python3
# --*-- coding:utf-8 --*--
import re
import sys
import json
import datetime

#---------------------------------------------------------------------------------------------------------------
#Since the color names of the dataset are in different formats, we have to adjust them to one single form for each color

#Defining a list of colors with the wrong and right names. 
true_colors_list = [('BLK', 'BLACK'),
 ('WHITE', 'WHITE'),
 ('BLUE', 'BLUE'),
 ('WH', 'WHITE'),
 ('GY', 'GRAY'),
 ('GRY', 'GRAY'),
 ('RED', 'RED'),
 ('GRAY', 'GRAY'),
 ('WHT', 'WHITE'),
 ('BLACK', 'BLACK'),
 ('BK', 'BLACK'),
 ('SILVE', 'SILVER'),
 ('GREY', 'GRAY'),
 ('BLU', 'BLUE'),
 ('BL', 'BLUE'),
 ('GREEN', 'GREEN'),
 ('WT', 'WHITE'),
 ('RD', 'RED'),
 ('TAN', 'TAN'),
 ('BROWN', 'BROWN'),
 ('SIL', 'SILVER'),
 ('SL', 'SILVER'),                  
 ('W', 'WHITE'),
 ('SILV', 'SILVER'),
 ('GRN', 'GREEN'),
 ('GR', 'GREEN'),
 ('WHI', 'WHITE'),
 ('YL', 'YELLOW'),
 ('GOLD', 'GOLD'),
 ('YELLO', 'YELLOW'),
 ('BRN', 'BROWN'),
 ('GLD', 'GOLD'),
 ('B', 'B'),
 ('BRW', 'BROWN'),
 ('BLA', 'BLACK'),
 ('GN', 'GREEN'),
 ('SLVR', 'SILVER'),
 ('ONG', 'ORANGE'),
 ('TN', 'TAN'),
 ('BW', 'BROWN'),
 ('BR', 'BROWN'),
 ('G', 'G'),
 ('PURP', 'PURPLE'),
 ('BEIGE', 'BEIGE'),
 ('ORANG', 'ORANGE'),
 ('PINK', 'PINK'),
 ('BRG', 'BRG'),
 ('YEL', 'YELLOW'),
 ('BLAC', 'BLACK'),
 ('MAROO', 'MAROON'),
 ('BRO', 'BROWN'),
 ('OTH', 'OTHER'),
 ('YW', 'YELLOW'),
 ('OR', 'ORANGE'),
 ('BLCK', 'BLACK'),
 ('SLV', 'SILVER'),
 ('PURPL', 'PURPLE'),
 ('BRWN', 'BROWN'),
 ('GL', 'GOLD'),
 ('GRE', 'GREEN'),
 ('GD', 'GOLD'),
 ('SLI', 'SILVER'),
 ('SIV', 'SILVER'),
 ('ORA', 'ORANGE'),
 ('BN', 'BROWN'),
 ('BIEGE', 'BEIGE'),
 ('WHTE', 'WHITE'),
 ('WHTIE', 'WHITE'),
 ('SILVR', 'SILVER'),
 ('WTH', 'WHITE'),                 
 ('ORG', 'ORANGE'),
 ('SLVER', 'SILVER'),
 ('ORAN', 'ORANGE'),
 ('PUR', 'PURPLE'),
 ('B L', 'BLACK'),
 ('YN', 'YELLOW'),
 ('GREE', 'GREEN'),
 ('BLACL', 'BLACK'),
 ('GRA', 'GRAY'),
 ('SIVER', 'SILVER'),
 ('YLW', 'YELLOW'),
 ('BRWB', 'BROWN'),
 ('BRWB', 'BROWN'),
 ('BROW', 'BROWN'),
 ('BKJ', 'BLACK'),         
 ('YELL', 'YELLOW')]

#----------------------------------------------------------------------------------------------------
#Function that converts a wrong color_name to the real one
def find_color(c):
    for i in true_colors_list:
        if c in i:
            return i[1]
            break
        
    return c
#----------------------------------------------------------------------------------------------------------------
for line in sys.stdin:
    try:
        #FIND THE LOCATION
        color = re.findall(r"vehicle_color': '(.+?['])", str(line)) #street_issued is a LIST OBJECT TYPE
        new_color = [c[:-1] for c in color] #Excluding the last character of each list[0], which is a ' (quotation mark)
        new_color = find_color(new_color[0]) #Function that unify the names of a same color (i.e. BLK, BK and BLCK are always BLACK)
        print('%s\t%s' % (new_color, 1)) #since new_x is a LIST, new_x[0] is the first element of that, which is the car type
            
    except:
        continue
