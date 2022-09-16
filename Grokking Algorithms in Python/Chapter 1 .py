#BINARY SEARCH

#define a function to find the item using the binary search technique
def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2    #go to the item in the half            # // ===> means floor division
        guess = list[mid]          #guess is the found number
        if guess == item:
            return mid
        elif guess > item:         #if guess bigger than item, search in the left side
            high = mid - 1
        else:
            low = mid + 1          #if guess smaller then item, search in the right side
    return None


#test the function
#Note: the list must be sorted
myList = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(myList, 9))              #prints: 8
print(binarySearch(myList, 15))             #prints: None
