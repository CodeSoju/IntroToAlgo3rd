def insertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while  i > -1 and arr[i] > key: 
            arr[i + 1] = arr[i]
            i = i -1
        arr[i + 1] = key
    return arr

testArr = [6, 3, 5, 7, 2, 4]

print("Original list:", testArr) 
print("\nSorted List: " , insertionSort(testArr))

