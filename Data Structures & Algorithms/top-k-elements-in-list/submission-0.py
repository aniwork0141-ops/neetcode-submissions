class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        lst = []
        hashmap = Counter(nums)
        srtd = dict(sorted(hashmap.items(),key=lambda x:x[1])) #sorted by value
        for key,value in srtd.items():
            lst.append(key)
        return lst[-k:]