n = int (input ("Enter the number of elements in the list: "))
bubbleList = []

print ("Provide the elements : ")
for x in range(0,n):
    bubbleList_element = input ()
    bubbleList.append(bubbleList_element)

print ("Before sort :")

print(bubbleList,end=" ")
print ()

print ("After sort :")
for i in range(0,n):
   for j in range(0,n-i-1):
       if(bubbleList[j]>bubbleList[j+1]):
           emp= bubbleList[j+1]
           bubbleList[j + 1]=bubbleList[j]
           bubbleList[j]=emp
print(bubbleList,end=" ")









