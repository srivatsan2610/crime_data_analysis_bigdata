#!/usr/bin/python
import sys

current_area = None
current_count = 0
area = None

for line in sys.stdin:
    line = line.strip()

    area,count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue



    if current_area== area:
        current_count += count

    else:
        if current_area:
            print '%s\t%d' %(current_area, current_count)
           # print(current_area,current_count,sep='\t')
            

        current_count = count
        current_area= area


if current_area == area:
    print '%s\t%d' %(current_area, current_count)
