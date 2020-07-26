class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x = abs(x)
        else:
            negative = False
        string = str(x)
        reverse = string[::-1]
        int_reverse = int(reverse)
        if negative:
            int_reverse = -int_reverse
            if int_reverse <= -2147483648:
                return 0
            else:
                return int_reverse
        else:
            if int_reverse >= 2147483647:
                return 0
            else:
                return int_reverse
