def binarySearch(array, key, start, end):    
    
    if end is None:
        
        end = len(array) - 1              

    middle = (start + end) // 2           
    
    if key == array[middle]:             
        
        return middle
    
    if key < array[middle]:              
        
        return (binarySearch(array, key, start, middle - 1))
    
    return (binarySearch(array, key, middle + 1, end)) 

