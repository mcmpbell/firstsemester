def merge_sort(arr):
    if len(arr) > 1:
        a = b = c = 0
        split = len(arr) // 2
        left = arr[:split]                     
        right = arr[split:]                    
        merge_sort(left)                            
        merge_sort(right)                           
        while a < len(left) and b < len(right):             
            if left[a] < right[b]:                      
                arr[c] = left[a]                        
                a += 1
            else:
                arr[c] = right[b]                       
                b += 1
            c += 1
        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1



    

