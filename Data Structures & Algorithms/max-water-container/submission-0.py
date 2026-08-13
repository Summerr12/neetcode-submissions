class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # if there is only 2 lens, then return the smallest val
        if len(heights) == 2:
            return min(heights[0], heights[1])

        #sorted width is a list of pairs that shows its position and height
        # sorted_width = list(enumerate(heights))
        # sorted_width.sort(key = lambda x: x[1])
        # for i,x in sorted_width:
        #     print(i,x)

        j=0
        k=len(heights)-1
        best_area = 0

        while j<k:# closing in on dist till it overlaps
            min_h = min(heights[j],heights[k])
            dist = k-j
            area = dist * min_h
            best_area = max(best_area,area)
            if(heights[j] < heights[k]):
                j+=1
            else:
                k-=1
        return best_area


        """
        we need to find the largest area in terms of height and width
        height is the min value of 2 indexes
        width is the difference of 2 indexes
        
        start from beginning and end for largest width
        then increment by 1 on either side and keep the max area
        [1,7,2,5,4,7,3,6]
        [0,1,2,3,4,5.6.7]
        so
        [1,6] = indexes(7-0) * min(1,6) = 7

        there has to be a check to ignore some pairs

        if unsorted, the width can be found easy
            mult the min height with dist
            closing in from left and right
        
        dont sort because finding index is harder than value of index

        finding maxes, the max width is the len(x)-1
                       the max height is the second highest height

        so we can do
        1,,,,6 = 1*(index 7-1) = 6


        we can move from the greatest width and greatest heights
        [1,7,2,5,4,7,3,6]
        sort the heights(values) and make a list of indexes to match

        [1,2,3,4,5,6,7,7]  
        [0,2,6]
        if we go to

        1 and 6 [heights], 7-0 [dist] = 7, we see 1* 7 = 7
        if anything is greater than 7 increase height min

        IF we found the max dist, find the next best area with the next best max dist
        depending on if left is smaller than right, increment closer
        so 1 increments to 7
        7 and 6 , 7-1 = 6 , 6*6 = 36
        since right is smaller height, move right closer
        7 and 3, 6-1 = 5, 5*3 = 15
        """