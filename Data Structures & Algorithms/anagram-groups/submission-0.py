class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        for item in strs:
            key = ''.join(sorted(item))
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(item)
        return list(hmap.values())
        