
#math library

#include <math.h>
#---------------------
import math

dir(math)

help(math.sqrt)

x = input("Enter the number: ")


x = int(x)

print (math.sqrt(x))


#version 01
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..leaving app')
        break #terminates the loop
    
    x = int(x)
    
    print (math.sqrt(x))   
    
#version 02

while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):

        x = int(x)
        
        print ("the square root is", math.sqrt(x)) 
    else:
        print ("the length is", len(x))


#version 03

datastore = []
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        break
    
    
    if( x.isdigit()):
        x = int(x)
        
        datastore.append(math.sqrt(x))
    else:
        datastore.append(len(x))
        help(str.append)

print (datastore)


#version 04 

datastore = {}
import math
while (True):
    x = input("Enter the number: ")
    
    #check if x is blank
    
    if (not x):
        print ('Invalid input..try next')
        continue
    
    
    if( x.isdigit()):
        
        x = int(x)
        
        datastore[x] = math.sqrt(x)
    else:
        datastore[x] = (len(x))



print(datastore)
