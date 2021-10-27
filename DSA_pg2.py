"""# finding maximum number from the list of array using function
def max_number(arr):           
    max=arr[0]                      
    for i in range(0,len(arr)):    
        if (arr[i] >max):           
            max=arr[i]
    return max
    
arr=[10,32,14,24,54]
result= max_number(arr)
print ("Largest number in given array is:",result)





# finding minimum number from the list of array without using function

arr=[12,23,34,45,67]
min=arr[0]
for i in range(0,len(arr)):
    if (arr[i]< min):
        min = arr[i]
print("lowest value from the list is:" + str(min))"""






"""special puzzle code"""
arr=[10000,2,3]
arr1=[]
for j,i in enumerate(arr):
    if(j< len(arr)):
      a=sum(arr)-arr[j+1]- i + i**3
      arr1=arr.append(a)
    else:
      a=sum(arr)-arr[j-1]-i + i**3
print(arr1)

    

        
