#SELECTION SORT

#function to find the smallest item 
def findSmallest(arr):
    smallest = arr[0]
    smallestIndx = 0
    for i in range(1, len(arr)):            #remember, range(l, r) ===> loops from l to r - 1 not including r.
        if(arr[i] < smallest):
            smallest = arr[i]
            smallestIndx = i
    return smallestIndx

#selection sort function:
def selectionSort(arr):
    sortedArray = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedArray.append(arr.pop(smallest))
    return sortedArray


#test the function:
myArray = [10,2,6,8,21,2200,-45,22225,0,12]
myArray = selectionSort(myArray)
print(myArray)          #prints: [-45, 0, 2, 6, 8, 10, 12, 21, 2200, 22225]