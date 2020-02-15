""" Binary Search """

class BinarySearch(object):
    """docstring for BinarySearch"""
    def __init__(self, arr):
        self._arr = arr

    def binarySearch(self, left, right, search_item):
        """ Binary Search """
        # Checking the base case
        if right >= left:
            mid = left + (right -1) // 2

            if self._arr[mid] == search_item:
                return mid
            elif self._arr[mid] > search_item:
                return self.binarySearch(left, mid-1, search_item)
            elif self._arr[mid] < search_item:
                return self.binarySearch(mid+1, right, search_item)
        else:
            return -1


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    search_item = int(input())
    bs = BinarySearch(arr)
    result = bs.binarySearch(0, len(arr)-1, search_item)
    if result != '-1':
        print(f"Item found at position {result}")
    else:
        print("Item not found")
