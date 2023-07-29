from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x*(-1), stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return abs(stones[0]) if len(stones) else 0