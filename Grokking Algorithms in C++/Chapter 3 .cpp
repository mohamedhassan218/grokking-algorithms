#include <iostream>
using namespace std;

//function count down from N to 1 using recursion
void countDown(int N)
{
	if (N <= 0)
		return;
	else
	{
		cout << N << " ";
		countDown(N - 1);
	}
}

int factorial(int N)
{
	if (N == 0 || N == 1)
		return 1;
	else
	{
		return N * factorial(N - 1);
	}
}

//binary search using recursion:
int binarySearch(int arr[], int N, int item, int l, int r)
{
	//int low = l, high = r;
	if (r >= l)
	{
		int mid = (l + r) / 2;

		if (arr[mid] == item)
			return mid;
		else if (arr[mid] > item)
			return binarySearch(arr, N, item, l, mid - 1);
		else
			return binarySearch(arr, N, item, mid + 1, r);

	}
	return -1;
}

int main()
{
	countDown(5);
	cout << factorial(5) << endl;
	int myArray[4] = { 1,2,3,4 };
	cout << binarySearch(myArray, 4, 4, 0, 3) << endl;//prints: 3
	cout << binarySearch(myArray, 4, 9, 0, 3) << endl;//prints: -1
	return 0;
}