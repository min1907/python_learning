from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count for keeping track of elements other than val
        count = 0
        # loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        print(nums)
        return count


# Testing
tmp = Solution()
a = [3, 2, 2, 3]

print(tmp.removeElement(a, 2))
