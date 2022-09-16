#include <iostream>
using namespace std;

int binarySearch(int arr[], int N, int item)
{
	int low = 0, high = N - 1;
	while (low <= high)
	{
		int mid = (high + low) / 2;	//access the middle item
		if (arr[mid] == item)
		{
			return mid;
		}
		else if (arr[mid] > item)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return -1;
}

int main()
{
	//Remember: the array must be sorted
	int myArray[10] = { 1,2,3,4,5,6,7,8,9,10 };
	
	cout << binarySearch(myArray, 10,5) << endl;	//prints: 4
	cout << binarySearch(myArray, 10, 89) << endl;	//prints: -1

	return 0;
}