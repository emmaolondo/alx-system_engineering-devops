#include "search_algos.h"

/**
 * binary_search - implement the binary search algorithm
 * @array: a pointer to the first element of the array to search in
 * @size: the number of elements in array
 * @value: the value to search for
 * Return: the index where the value is located or -1
 */
int binary_search(int *array, size_t size, int value)
{
	size_t i, low, high, mid;

	if (!array)
		return (-1);

	low = 0;
	high = size -1;

	while (low <= high)
	{
		printf("Searching in array: ");
		for (i = low; i <= high; i++)
		{
			if (i < high)
				printf(", ");
		}
		printf("\n");

		mid = low + (high - low) / 2;

		if (array[mid] == value)
			return (m);
		else if (array[mid] < value)
			low = mid + 1;
		else
			high = mid -1;
	}
	return (-1);
}
