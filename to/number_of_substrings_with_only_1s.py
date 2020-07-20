def get_num_of_substrings_of_n_1s(n):
    return int((1 + n) * n / 2)


def check_is_last_idx_of_s(s, idx):
    return len(s) - 1 == idx


class Solution:
    '''
    The key point is to find the segment only containing 1s
    then use formula to calc it
    001000110 => 1 \ 11
    0111101101 => 1111 \ 11 \1
    '''
    def numSub(self, s: str) -> int:
        result = 0
        one_range_start = None
        for i in range(len(s)):
            # mark the start of segment
            if one_range_start is None and s[i] == '1':
                one_range_start = i
                # if the char is the last one, just add 1 to result
                if check_is_last_idx_of_s(s, i):
                    result += 1
            # it's the end of one segment
            elif one_range_start is not None and s[i] == '0':
                # len of segment: (i - 1) - one_range_start + 1
                result += get_num_of_substrings_of_n_1s(i - one_range_start)
                one_range_start = None
            # continuous 1s string and reach the end of the string
            elif one_range_start is not None and check_is_last_idx_of_s(s, i) and s[i] == '1':
                result += get_num_of_substrings_of_n_1s(i - one_range_start + 1)
                one_range_start = None

        # https://leetcode.com/problems/number-of-substrings-with-only-1s/
        # Since the answer may be too large, return it modulo 10^9 + 7.
        return result % (10**9 + 7)
