class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #looks like sliding window and a for loop
        #choosing the heaviest 2 rocks
        '''
        [9, 4, 3, 2, 2]
        [3,2,2, 5]
        [2, 2, 2, 1]
        '''
        stones.sort(reverse = True)
        print(stones)
        while len(stones) > 1:
            xy = abs(stones[0] - stones[1])
            stones.append(xy)
            stones = stones[2:]
            stones.sort(reverse = True)

        return stones[0]