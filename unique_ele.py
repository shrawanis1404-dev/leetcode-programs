class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


obj = Solution()

nums = [1, 1, 2, 2, 3, 4, 4, 5]

k = obj.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Updated array:", nums[:k])

