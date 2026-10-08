class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #looks like sliding window 
        #choosing the heaviest 2 rocks

        stones.sort(reverse = True)
        while len(stones) > 1:
            xy = abs(stones[0] - stones[1])
            stones.append(xy)
            stones = stones[2:]
            stones.sort(reverse = True)

        return stones[0]