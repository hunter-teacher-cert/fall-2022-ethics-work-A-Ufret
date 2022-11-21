# binsearch.py
# Ashley Ufret
# CSCI 77800 Fall 2022
# collaborators:
# consulted:  Kiana Herr, Usman Ahmed (part of my group for BinSearch.java)

# binSearch(List, n) -- searches a list for target value = n
# precondition: input list is all of same type and is sorted in ascending order
# postcondition: returns index of target, or returns "Found at -1" if target not found in the list

pos = -1

def binsearch(list, n):
    NOT_FOUND = -1
    lower = 0
    upper = len(list)-1
    
    while lower <= upper:
        middle = (lower + upper) // 2
             
        if list[middle] == n: #if the target value is found at the middle index = true
            globals()['pos'] = middle
            return True
        else: # if the target value is not found at the middle index will continue binary search (searching lower half or upper half depending on value at middle index) continuing to split in half until the index is found or search is complete
            if list[middle] < n:
                lower = middle        
            else:
                upper = middle
           
          
list = [2,8,17,26,32,46,55,68,99]
n = 26 #target_value 

if binsearch(list, n):
    print("found at ", pos)
else:
    return NOT_FOUND
#this is not working properly for n not found will continue to debug
#I tried adding return statement after the else on line 27 but then it would interrupt the loop of checking for index after not finding target in the middle
