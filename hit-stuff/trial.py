from collections import Counter
from math import pow

lst = [1, 2, 3, 4, 1, 2, 3, 4, 1]

def return_count(lst, key):
    cnt = Counter(lst)
    # at this point {1 : 2, 2 : 2, 3 : 3} and so on
    cnt = dict(cnt)
    if key in cnt:
        print(cnt[key])
        return cnt[key]
    return "Not There!"

def index_non_rc(s):
    # s = leetcode
    cnt = Counter(s)

    for i, ch in enumerate(s):
        if cnt[ch] == 1:
            return i 
    return -1

def return_powerd(lst, n):
    '''Return all the numbers in lst powerd n'''
    ret_lst = [pow(i, n) for i in lst]
    return ret_lst 

def prefix_sum(lst):
    # lst = 4 5 9 3
    prefix = [0, 4, 9, 18, 21]
    for i in lst:
        prefix.append(prefix[-1] + i)