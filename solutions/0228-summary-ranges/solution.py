class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i +=1

            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans
    
# T: O(n)   nonostante ci sia un while dentro un altro while. Il contatore i va sempre avanti, non è la tipica situazione con 2 contatori i e j in cui i scorre e j si fa tutto l' array da i  a n-1 ogni volta
# S: O(n)    per via della lista ans
