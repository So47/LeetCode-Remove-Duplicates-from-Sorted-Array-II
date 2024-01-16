class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        next_unique_num = 2  # Start from the third element

        for i in range(2, len(nums)):
            if nums[i] != nums[next_unique_num - 2]:
                nums[next_unique_num] = nums[i]
                next_unique_num += 1

        return next_unique_num   


        
