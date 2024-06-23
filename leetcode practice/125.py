class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter=''.join([char for char in s.lower() if char.isalnum()])
        return filter==filter[::-1]
        