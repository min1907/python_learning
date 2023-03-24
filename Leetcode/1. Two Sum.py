from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # List to store results
        result = []

        # Dictionary to store the difference and its index
        index_map = {}

        # Loop for each element
        for i, n in enumerate(nums):
            # Different which needs to be checked
            different = target - n
            if different in index_map:
                result.append(i)
                result.append(index_map[different])
                break
            else:
                index_map[n] = i

        return result


tmp = Solution()
a = [3, 2, 4]

print(tmp.twoSum(a, 6))

# Explanation:
# https://redquark.org/leetcode/0001-two-sum/
