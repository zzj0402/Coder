class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        reverse = string[::-1]
        return int(reverse)
