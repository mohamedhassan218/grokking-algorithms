#RECURSION
#function to print numbers from N to 1 using recursion
def countDown(n):
    if(n <= 0):             #base case:
        return
    else:
        print(n)
        countDown(n-1)      #recursive case:

#function to find the factorial of the number using recursion
def factorial(n):
    if(n == 1 or n == 0):
        return 1            #base case (the point which the program will stop when it meets it)
    else:
        return n*factorial(n-1) #recursive case

#binary search using recursion:
def binarySearch(arr, low, high, x):
    if high >= low :
        mid = (low + high) // 2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x :
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1


#test the functions:
countDown(4)
print(factorial(5))
arr = [1,2,5,8,10,11,12]
print(binarySearch(arr, 0, 6, 10))   #prints: 4
print(binarySearch(arr, 0, 6, 100))  #prints: -1