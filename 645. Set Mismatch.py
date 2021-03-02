class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        seen = set()
        for i in nums:
            if i in seen:
                result.append(i)
                break
            else:
                seen.add(i)
        
        for i in range(1,len(nums) +1):
            if i not in nums:
                result.append(i)
        return result
