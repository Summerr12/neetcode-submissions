class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use a map
        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i,0) + 1
        # map checker
        # for i,n in enumerate(count_dict):
        #     print(n, count_dict[n])
        sorted_dict = list(count_dict.keys())
        sorted_dict.sort(key=count_dict.get, reverse=True)
        return sorted_dict[:k]

    # fill map with values
    # [8,8,8,9,9,6,6,6,6]
    # {
    #     [8,3]
    #     [9,2]
    #     [6,4]
    # }
    # after filling this

    # place all vectors {count, val}
    # {3,1}
    # {2,2}
    # {4,3}
    # sort this
    # {2,2}
    # {3,1}
    # {4,3}

    # iterate k=2
    # look end of vector, grab the value and push it to the vector<int>
    # find the 
        