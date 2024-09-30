# Arrays

from array import *

# creation
#comment for git
#-------------

arr1=array('i',[1,2,3,4,4])

#print the enire arraystructre with a singlle satement
print("Arr1: ",arr1)

#loop through the entire array printing one elemn at a time(traversing)
print("contents of array arr1: ")
for item in arr1:
    print(item)
#traversing using len() and range()
for i in range(len(arr1)):
    print(arr1[i])
'''
##finding the length of an array
print("no.of eleements in arr1: ",len(arr1))

#accessing an item at an index
print(arr1[3])

##searching for an item through an array..
print(arr1.index(4))

# assigning value to a positon in the array..
arr1[4]=5
print(arr1)
'''
'''
#append an item to the end of an array
arr1.append(60)
print(arr1)

#to isert an item at a specifi position(INDEX)
arr1.insert(1,10)
print(arr1)

#to add an entire array at the end of anoher array
arr1.extend([7,8,9])
print(arr1)

#to remove an item from the array
arr1.remove(10)
print(arr1)

#to remove an item at an index
arr1.pop(3)
print(arr1)

# count the number of occurances of an element
print(arr1.count(4))

#reverse an array
arr1.reverse()
print(arr1)

string1="Hello World"
print(string1.split(" "))
'''






