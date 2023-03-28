class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Base condition
        if x < 0:
            return False
        # Store number in variable
        number = x
        # Store a reverse of a number
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse


tmp = Solution()

print(tmp.isPalindrome(121))

# Explanation: https://redquark.org/leetcode/0009-palindrome-number/
