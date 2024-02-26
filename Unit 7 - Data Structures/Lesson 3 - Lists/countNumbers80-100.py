#OCR A Level Computer Science
#Unit 7 Data Structures Topic 3 Lists and linked lists
#countNumbers 80-100 removes all numbers between 80-100 from a list

#Author: PG Online team
#Date: 14/04/2016

list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
count = 0
for index in range(len(list1)):
    if (list1[index] >=80) and (list1[index] <=100):
        print("list1[index]",list1[index])
        count+=1
print("Number of integers in range 80-100", count)

#remove these items from the list
list2 = []

for index in range(len(list1)):
    if (list1[index] <80) or (list1[index] >100) :
        print("list1[index]",list1[index])
        list2.append(list1[index])      
list1 = list2        
print(list2)