class TreeNode(object):
    def __init__(self, val, idx_in_str):
        self.val = val
        self.idx_in_str = idx_in_str
        self.last_idx_in_str = len(val) + idx_in_str - 1

    def get_val(self):
        return self.val

    def get_idx(self):
        return self.idx_in_str

    def get_last_idx(self):
        return self.last_idx_in_str


def check_s_all_1s(s):
    return s == '1' * len(s)


def check_dict_has_key(k, d):
    return k in d.keys()


class Solution:
    '''
    substring to a tree(breadth first search)
    '''
    def numSub(self, s: str) -> int:
        result = 0
        my_queue = []  # for BFS
        my_map = {}  # records whether certain substring handled before

        for idx, val in enumerate(s):  # starts with only one char
            if val == '1':
                result += 1  # manually handle 1 char case to improve the performance
                if s[idx:idx + 2] == '11':
                    my_queue.append(TreeNode(s[idx: idx + 2], idx))  # enqueue
        while len(my_queue) > 0:
            first_ele = my_queue.pop(0)  # dequeue
            first_val = first_ele.get_val()
            first_idx = first_ele.get_idx()
            first_last_idx = first_ele.get_last_idx()

            map_key = first_val + ',' + str(first_idx)
            if not check_dict_has_key(map_key, my_map) and check_s_all_1s(first_val):
                result += 1
                my_map[map_key] = True
                if first_last_idx <= len(s) - 1:
                    my_queue.append(TreeNode(s[first_idx: first_last_idx + 2], first_idx))

        return result % (10**9 + 7)
