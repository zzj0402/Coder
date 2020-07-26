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
            int_reverse = int(reverse)
            if int_reverse >= 2147483648:
                return 0
            else:
                return int_reverse
