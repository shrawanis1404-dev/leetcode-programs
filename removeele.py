class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


obj = Solution()

nums = [3, 2, 2, 3]
val = 3

k = obj.removeElement(nums, val)

print("Number of elements:", k)
print("Updated array:", nums[:k])