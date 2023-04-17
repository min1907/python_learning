"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def searchInsert(
    nums: List[int], target: int
) -> int:  # Accept by Leetcode but very low rating
    idmin = 0
    idmax = len(nums)
    idmid = (idmin + idmax) // 2

    if target in nums:
        while idmid < idmax:
            if target < nums[idmid]:
                print("a")
                idmax = idmid
                idmid = (idmin + idmax) // 2
            elif target > nums[idmid]:
                print("b")
                idmin = idmid
                idmid = (idmin + idmax) // 2
            else:  # target = nums[mid]
                print("c")
                return idmid
    else:  # not target in nums
        if target > max(nums):
            return len(nums)
        if target < min(nums):
            return 0

        while idmid < idmax:
            while target < nums[idmid]:
                print("d")
                idmax = idmid
                idmid = (idmin + idmax) // 2
                if idmid == idmin:
                    return idmid + 1

            while target > nums[idmid]:
                print("e")
                idmin = idmid
                idmid = (idmin + idmax) // 2
                if idmid == idmin:
                    return idmid + 1


nums = [1, 2, 4, 6, 7]
target = 3
print(searchInsert(nums, target))


# Or consider using bisect python (import bisect)
# ref: https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# The purpose of Bisect algorithm is to find a position in list where an element needs to be inserted to keep the list sorted.
"""
1. bisect(list, num, beg, end) :- This function returns the position in the sorted list,
where the number passed in argument can be placed so as to maintain the resultant list in sorted order.
If the element is already present in the list, the rightmost position where element has to be inserted is returned.
"""
