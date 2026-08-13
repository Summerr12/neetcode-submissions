class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_map = {}
        for i,n in enumerate(strs):
            # print(i, ''.join(sorted(n)))
            temp = ''.join(sorted(n))
            if temp not in list_map:
                list_map[temp] = [n]
            else:
                list_map[temp].append(n)
        # for i in list_map:
        #     print(i)
        return list(list_map.values())