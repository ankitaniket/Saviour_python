arr = [];   
n=int(input("Enter the size of the list: "))  

for i in range(0,n):
    key=int(input())
    arr.append(key)
     
print("Duplicate elements in given array: ");    
  
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j],end=" ");    