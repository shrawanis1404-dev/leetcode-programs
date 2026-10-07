def isSorted(nums):
    if len(nums) <= 1:
        return True

    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            return False

    return True