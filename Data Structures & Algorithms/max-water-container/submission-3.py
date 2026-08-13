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


        