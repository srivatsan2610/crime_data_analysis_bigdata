#!/usr/bin/python
import sys
import fileinput


heading_index=[] #to store the required heading index
#print '%s\t%s' % (word, 1)
required_row = []

# 5 - area name; 10 - age ; 11 - gender ; 12- victim origin

for line in fileinput.input():
    every_row= []
    if fileinput.isfirstline():
        continue
    else:
        line = line.strip()
        every_row = line.split(",")
        if every_row[11] == "F" and every_row[12] == "W": #if the victim is female and from asian
            print '%s\t%s' % (every_row[5],1)
            #print(every_row[5] , 1,sep = "\t") #print the area name
            
            
            
            
        
        
    
        
    
    
