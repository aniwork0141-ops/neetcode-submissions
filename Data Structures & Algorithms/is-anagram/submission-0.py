class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        hmap1 = dict(Counter(s))
        hmap2 = dict(Counter(t))

        return hmap1==hmap2

        