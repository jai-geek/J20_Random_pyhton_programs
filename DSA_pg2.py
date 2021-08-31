"""# finding maximum number from the list of array
arr=[12,13,14,15,16]            #initialized the array
max=arr[0]                      #in max keyword initialize the 1st value that is of 0th index
for i in range(0,len(arr)):     #loop through the code from 0th index to the length of array inserted in arr
    if (arr[i] >max):           #compare if the value of i which is iterated from arr is greater than max 
        max=arr[i]              
print("largest element in the given array is:" + str(max))

# finding minimum number from the list of array

arr=[12,23,34,45,67]
min=arr[0]
for i in range(0,len(arr)):
    if (arr[i]< min):
        min = arr[i]
print("lowest value from the list is:" + str(min))"""

arr=[10000,2,3]
arr1=[]
for j,i in enumerate(arr):
    if(j< len(arr)):
      a=sum(arr)-arr[j+1]- i + i**3
      arr1=arr.append(a)
    else:
      a=sum(arr)-arr[j-1]-i + i**3
print(arr1)

    

        
