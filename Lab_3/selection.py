def selectionSort(A):
    for i in range(len(A)):  
        
        # Find the minimum element in remaining  
        # unsorted array  
        min_idx = i  
        for j in range(i+1, len(A)):  

            if A[min_idx] > A[j]:  

                min_idx = j
        # Swap the found minimum element with  

        # the first element   
        A[i], A[min_idx] = A[min_idx], A[i]  

    
def printList(arr): 
    for i in range(len(arr)): 
        print(arr[i], end=" ")
    print() 

# Driver Code 

if __name__ == '__main__': 
    A = [64, 25, 12, 22, 11, 8, 55, 34]  
    print("Given unsorted Array") 
    printList(A) 
    selectionSort(A) 
    print("\nSorted array is ") 
    printList(A) 
    
    
