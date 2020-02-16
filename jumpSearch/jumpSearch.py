import math

class JumpSearch(object):
    """docstring for JumpSearch"""
    def __init__(self, arr):
        self._arr = arr

    def jump_search(self, search_item):
        """ Jump Search """
        n = len(self._arr)
        step = math.sqrt(n)

        while self._arr[int(min(step, n)-1)] < search_item:
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return -1

        while arr[int(prev)] < search_item:
            prev += 1

            if prev == min(step, n):
                return -1

        if arr[int(prev)] == search_item:
            return prev


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    search_item = int(input())

    js = JumpSearch(arr)
    index = js.jump_search(search_item)

    print("Number" , search_item, "is at index" ,"%.0f"%index)
