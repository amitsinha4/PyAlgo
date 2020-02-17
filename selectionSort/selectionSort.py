# Import statement
import sys


class SelectionSort(object):
    """ Selection Sort """
    def __init__(self, arr):
        """ Constructor to initialize the array """
        self._arr = arr

    def selection_sort(self):
        """ Performing the selection sort """
        len_of_array = len(self._arr)
        for i in range(len_of_array):
            min_idx = i
            for j in range(i+1, len_of_array):
                if self._arr[min_idx] > A[j]:
                    min_idx = j
            A[min_idx], A[i] = A[i], A[min_idx]
        return self._arr


if __name__ == '__main__':
    A = [64, 25, 12, 22, 11]
    ss = SelectionSort(A)
    sorted_arr = ss.selection_sort()
    print(f"Sorted array {sorted_arr}")