class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x = abs(x)
        else:
            negative = False
        string = str(x)
        reverse = string[::-1]
        if negative:
            return -int(reverse)
        else:
            return int(reverse)
