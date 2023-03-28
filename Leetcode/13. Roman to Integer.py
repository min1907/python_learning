class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary of Roman numerals
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # Length of given string
        n = len(s)
        # variable to store the result
        num = roman_map[s[n - 1]]

        # Loop for each character from right to left
        for i in range(n - 2, -1, -1):
            # check if the character at right of current character is bigger of smaller
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                number += roman_map[s[i]]
            else:
                number -= roman_map[s[i]]

        return number


tmp = Solution()
print(tmp.romanToInt("MCMXCIV"))
