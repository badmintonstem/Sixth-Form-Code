#OCR A Level Computer Science
#Unit 7 Data Structures Topic 3 Lists and linked lists

#program MergeLists.py
#merges two sorted lists into one sorted list

#Author: PG Online team
#Date: 15/04/2016

list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergeList = []
i = 0
j = 0
#k = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        mergeList.append(list1[i])
        i += 1
    else:
        mergeList.append(list2[j])
        j += 1
    #endif   
#    k += 1
   
#endwhile
#now put any remaining items from the longer list into mergeList
while i < len(list1):
    mergeList.append(list1[i])
    i += 1
#endwhile
while j < len(list2):
    mergeList.append(list2[j])
    j += 1
#endwhile

print("list1",list1)
print("list2",list2)
print("mergeList",mergeList)
