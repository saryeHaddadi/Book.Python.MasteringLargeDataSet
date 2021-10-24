from functools import reduce

xs = ["A", "B", "C", "A", "A", "C", "A"]
ys = [1, 3, 6, 1, 2, 9, 3, 12]


def make_count(acc: dict, next):
    acc[next] = acc.get(next, 0) + 1
    return acc

def my_frequencies(bow):
    return reduce(make_count, bow, dict())

print(my_frequencies(xs))
print(my_frequencies(ys))
print(my_frequencies("mississippi"))



