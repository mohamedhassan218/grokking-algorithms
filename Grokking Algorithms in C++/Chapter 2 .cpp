#include <iostream>
using namespace std;

//function to swap the elements:
void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

void selectionSort(int arr[], int N)
{
	int i, j, minIndx;
	for (i = 0; i < N - 1; i++)
	{
		
		for (j = i + 1; j < N; j++)
		{
			minIndx = i;
			if (arr[j] < arr[minIndx])
				minIndx = j;

			if (minIndx != i)
				swap(&arr[minIndx], &arr[i]);
		}
	}
}

int main()
{
	int arr[10] = { 10,5,6,-6,6565,552,120,1,2,0 };
	selectionSort(arr, 10);
	for (int i = 0; i < 10; i++)
		cout << arr[i] << " ";
	//prints: -6 0 1 2 5 6 10 120 552 6565

	return 0;
}