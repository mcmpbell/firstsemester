import timeit

with open("input_100.txt", "r") as ri:
    
        temp = ri.readline()

        forSort = list(map(int, temp.split()))

        start = timeit.default_timer()

def merge_sort(arr):
    
    if len(arr) > 1:

        a = b = c = 0
        
        split = (len(arr) // 2)
        
        right = arr[:split]
        
        left = arr[split:]

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
            
def insertion_sort(arr):
        
    for i in range(0, len(arr)):

        cval = arr[i]
        
        pos = i

        while pos > 0 and arr[pos - 1] > cval:
            
            arr[pos] = arr[pos - 1]
            
            pos = pos - 1

        arr[pos] = cval
    
arr = forSort
if len(arr) >= 1000:
    merge_sort(arr)
    stop = timeit.default_timer()
    print(arr)
    print("Merge sort. Elapsed time: ", stop - start)

else:
    if len(arr) <= 100:
        insertion_sort(arr)
        stop = timeit.default_timer()
        print(arr)
        print("Insertion sort. Elapsed time: ", stop - start)

