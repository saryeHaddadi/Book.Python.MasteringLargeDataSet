from functools import reduce

values = ["these", "are", "some", "words", "for", "grouping"]

def len_and_add(acc, nxt):
    size = len(nxt)
    acc[size] = acc.get(size, []) + [nxt]
    return acc


def group_by_len(values):
    return reduce(len_and_add, values, dict())

print(group_by_len(values))


