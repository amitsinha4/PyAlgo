class LinearSearch(object):
    """
    Linear search of an supplied array
    params:
        Expect an array while creating an object of this class

    Linear has time complexity of O(n)
    """
    
    def __init__(self, arr):
        """ Constructor """
        self._arr = arr
        
    def search(self, x):
        """ Perform linear Search on supplied array """
        n = len(self._arr)
        for i in range(0, n):
            if self._arr[i] == x:
                return i
        return -1


# Driver Code
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    search_item = int(input())
    ls = LinearSearch(arr)
    result = ls.search(search_item)
    if result == "-1":
        print(f"Item not found")
    else:
        print(f"Item found at position {result}")