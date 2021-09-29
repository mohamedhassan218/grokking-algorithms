def binarysearch_iteration(arr,item):
    low =0
    high =len(arr)-1
    mid =0
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == item:
            return item
        elif arr[mid] > item:
            high = mid-1
        elif arr[mid] < item:
            low = mid+1
    return None
array1 = [2,5,6,8,9,6,5,2,1,8,7,45,45,45,87,78,96,5]
print (binarysearch_iteration(array1,45))
#Binary search Chapter1 test from gomaa sdf sdf sd fsd f sdf sdf sdf sdf
# my test from froking repo
#change from mohassans laptoptest3
#***********************************************************************************************************

def findsmallest(arr):
    smallest = arr[0]
    smallest_index =0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selection_sort(arr):
    new_array =[]
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array
array2 = [12,13,56,4,65,8,9,1,65,89,3]
print (selection_sort(array2))
#Selection sort chapter2
#***********************************************************************************************************

def count_down(item):
    print (item)
    if item<=0:             #base case
        return 0
    else:
        count_down(item-1)   #recursive case
count_down(5)


def fact(item):
    if item ==1:
        return 1
    else:
        return item*fact(item-1)
print (fact(5))
#Recursion chapter3
# test here creat login
#***********************************************************************************************************

def sum(List):
    if List == []:                    #base case
        return 0
    else :
        return List[0] + sum(List[1:])   #recursive case
my_array = [2,3,5,6,4]
print (sum(my_array))


def count (arr):
    if arr ==[]:                    #base case
        return 0
    else:
        return 1 + count(arr[1:])   #recursive case
my_array2 = [2,3,5,6,4]
print (count(my_array2))


def max(lis):
    if len(lis) == 2:                             #base case
        return lis[0] if lis[0]>lis[1] else lis[1]
    sub_max = max(lis[1:])                    #recursive case
    return lis[0] if lis[0] > sub_max else sub_max
array3 = [1,2,3,9,45,888]
print (max(array3))


def binarysearch_recursion(array,element,start,end):
    if start > end :
        return -1
    mid = (start + end)//2
    if element == array[mid]:
        return mid
    elif element > array[mid]:
        return binarysearch_recursion(array,element,mid+1,end)
    else :
        return binarysearch_recursion(array,element,start,mid-1)
array4 = [2,3,6,5,69,8,9,88]
print (binarysearch_recursion(array4,5,0,7))


def quicksort(array):
    if len(array) <2:                  #base case
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  #recursive case
        greater = [ m for m in array[1:] if m > pivot]
        return quicksort(less) + pivot + quicksort(greater)
array5 = [2,8,20,6,103,4,900]
print (quicksort(array5))

#devide & concer and quicksort chapter4
#******************************************************************************************************


voted ={}
def check_voter(name):
    if voted.get(name):
        print ("Kick him out !")                #Using hashtables to prevent duplicate entires
    else :
        voted[name] = True
        print ("Let him vote!")

check_voter("mohamed")
print ("****************************************")
check_voter("mohamed")


#Hash tables chapter 5 
#****************************************************************************************************************


graph = {}
graph['you'] = ['Bob', 'Clarie','Alice']
graph ['Clarie'] = ['Tom','gony']
graph['Tom'] =[]
graph['Gony'] = []
graph['Bob']= []
graph['Alice'] =[]
from collections import deque 
def person_is_seller(name):
    return name[-1] == 'm'
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched :
            if person_is_seller(person):
                print (person + " is a mango seller ")
                return True 
            else :
                search_queue += graph[person]
                searched.append(person)
    return False
search('you')

#breadth first search chapter 6
#**************************************************************************************************

graph2 = {}
graph2['start'] = {}
graph2['start']['a'] = 6
graph2['start']['b'] = 2
graph2['a'] = {}
graph2['a']['finish'] = 1
graph2['b'] = {}
graph2['b']['a'] = 3
graph2['b']['finish'] = 5
graph2['finish'] = {}                              #hash table to the graph

infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['finish'] = infinity                          #hash table to the costs

perants = {}
perants['a'] = 'start'
perants['b'] = 'start'
perants['finish'] = None                            #hash table for perants

processed =[]

def find_lowest_cost_node(Costs):
    lowest_cost = float("inf")
    lowest_cost_node = None 
    for node in Costs :
        cost = Costs[node]
        if cost < lowest_cost and node not in processed :
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node                          #function to find the nearest node

node = find_lowest_cost_node(costs)
while node is not None :
    cost = costs[node]
    neighbors = graph2[node]
    for n in neighbors.key():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost :
            costs[n] = new_cost
            perants[n] = node 
    processed.append(node)
    node = find_lowest_cost_node(costs)

#Dijkstra's algorithm chapter 7
#**************************************************************************************************************

states_needed = set([“mt”, “wa”, “or”, “id”, “nv”, “ut”, “ca”, “az”])
stations = {}
stations[“kone”] = set([“id”, “nv”, “ut”])
stations[“ktwo”] = set([“wa”, “id”, “mt”])
stations[“kthree”] = set([“or”, “nv”, “ca”])
stations[“kfour”] = set([“nv”, “ut”])
stations[“kfive”] = set([“ca”, “az”])
while states_needed :
    best_station = None
    states_covered = set()
    for station , states in stations.item():
        covered = states_needed & states 
        if len(covered) > len(states_covered) :
            best_station = station 
            states_covered = covered
    states_needed -= states_covered
    final_station.add(best_station)
print (final_station)




