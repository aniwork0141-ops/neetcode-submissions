class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k and k>i:
                target = -nums[i]
                if (nums[j] + nums[k] == target) and ([nums[i],nums[j],nums[k]] not in out):
                    out.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    k-=1
        return out