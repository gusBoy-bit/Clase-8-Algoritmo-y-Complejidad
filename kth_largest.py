import heapq

class Solution:
    def findKthLargest(self, nums, k):
        cola = []

        for numero in nums:
            heapq.heappush(cola, numero)

            if len(cola) > k:
                heapq.heappop(cola)

        return cola[0]