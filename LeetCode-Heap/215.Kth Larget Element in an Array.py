import heapq

def findKth(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
    print(heap)
    for _ in range(1, k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


result = findKth([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
print(result)
