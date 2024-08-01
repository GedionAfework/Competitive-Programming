class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            a = str(x)
        if x == int(a[::-1]):
            return True