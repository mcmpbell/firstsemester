def insertionSort(Sort):
    
    for i in range(1, len(Sort)):

        cval = Sort[i]
        
        pos = i

        while pos > 0 and Sort[pos - 1] > cval:
            
            Sort[pos] = Sort[pos - 1]
            
            pos = pos - 1

        Sort[pos] = cval




