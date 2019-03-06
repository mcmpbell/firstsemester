import timeit

with open("input_100.txt", "r") as ri:
    
        temp = ri.readline()

        arr = list(map(int, temp.split()))

        start = timeit.default_timer()

def insertionSort(Sort):
        
    for i in range(0, len(Sort)):

        cval = Sort[i]
        
        pos = i

        while pos > 0 and Sort[pos - 1] > cval:
            
            Sort[pos] = Sort[pos - 1]
            
            pos = pos - 1

        Sort[pos] = cval
        
Sort = arr
insertionSort(Sort)
stop = timeit.default_timer()
print(Sort)
print("Time: ", (stop - start))










    
