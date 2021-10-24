from functools import reduce
import bisect

values = [10,7,3,1,9,8,11,21,15,72]

def sort_and_keep_v1(acc, nxt, n):
    bisect.insort_left(acc, nxt)
    return acc[n:]

def sort_and_keep_n(n):
    def sort_and_keep(acc, nxt):
        bisect.insort_left(acc, nxt)
        return acc[-n:]
    return sort_and_keep

def largest(n, val):
    return reduce(sort_and_keep_n(n), val, [])

print(largest(3, [10,7,3,1,9,8,11,21,15,72]))



