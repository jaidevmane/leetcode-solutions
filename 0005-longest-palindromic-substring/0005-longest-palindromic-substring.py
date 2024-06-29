class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        res = ""
        for i in range(len(s)):
            # odd case
            odd_palindrome = expand(i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome
            # even case
            even_palindrome = expand(i, i +1)
            if len(even_palindrome) > len(res):
                res = even_palindrome
        return res

        