from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # 2 pointers method
    i, j = 0, 1
    while i <= j and j < len(nums):
        print(f"i = {i}, j = {j}, nums = {nums}")
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1
    # print(f"i = {i}, j = {j}, nums = {nums}")
    return i + 1


num1s = [1, 1, 2]
num2s = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(
    removeDuplicates(num2s)
)  # i = 4, j = 10, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] - return 5
"""
i = 0, j = 1, nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
i = 0, j = 2, nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
i = 1, j = 2, nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
i = 1, j = 3, nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
i = 1, j = 4, nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
i = 1, j = 5, nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
i = 2, j = 5, nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
i = 2, j = 6, nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
i = 2, j = 7, nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
i = 3, j = 7, nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
i = 3, j = 8, nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
i = 3, j = 9, nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
i = 4, j = 9, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
"""
