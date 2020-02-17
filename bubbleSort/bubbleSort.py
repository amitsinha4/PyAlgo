""" Bubble Sort Algorithm """


class BubbleSort(object):
    """ Bubble Sort """

    def __init__(self, arr):
        self._arr = arr

    def bubble_sort(self):
        """ Performing a bubble sort"""
        n = len(self._arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self._arr[j] > self._arr[j+1]:
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
        return self._arr


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bs = BubbleSort(arr)
    sorted_array = bs.bubble_sort()

    print(f'sorted array {sorted_array}')