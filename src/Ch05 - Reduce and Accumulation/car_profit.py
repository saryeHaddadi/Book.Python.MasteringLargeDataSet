from functools import reduce

MPG = 'mpg'
ODO = 'odo'
PROFIT = 'profit'
TOTAL = 'total'
COUNT = 'count'
AVG = 'avg'

def low_med_hi(d, k, breaks):
    if float(d[k]) < breaks[0]:
        return "low"
    elif float(d[k]) < breaks[1]:
        return "med"
    else:
        return "high"


def clean_entry(d):
    r = {'profit':None, 'mpg':None, 'odo':None}
    r['profit'] = float(d.get("price-sell", 0)) - float(d.get("price-buy", 0))
    r['mpg'] = low_med_hi(d, 'mpg', (18, 35))
    r['odo'] = low_med_hi(d, 'odo', (60000, 105000))
    return r

def acc_avg(acc: dict, profit):
    acc[TOTAL] += profit
    acc[COUNT] += 1
    acc[AVG] = acc[TOTAL] / acc[COUNT]
    return acc

def acc(acc: dict, nxt):
    profit = nxt[PROFIT]
    acc[MPG][nxt[MPG]] = acc_avg(acc[MPG][nxt[MPG]], profit)
    acc[ODO][nxt[ODO]] = acc_avg(acc[ODO][nxt[ODO]], profit)
    return acc


def get_agg_dict():
    return {'total': 0, 'count': 0, 'avg': None}

def get_category_dict():
    return {'low': get_agg_dict(), 'med': get_agg_dict(), 'high': get_agg_dict()}

def get_initializer():
    return {'mpg' : get_category_dict(), 'odo': get_category_dict()}

if __name__ == "__main__":
    import json
    with open("cars.json") as f:
        data = json.load(f)
    result = reduce(acc, map(clean_entry, data), get_initializer())
    print(json.dumps(result, indent=4))


# # Lambda exercice
# def my_addition(a, b):
#     return a+b

# my_addition = lambda a, b: a+b

# def is_odd(a):
#      return a % 2 == 1

# is_odd = lambda a: (a % 2 == 1)

# def contains(a, b):
#     return b in a

# contains = lambda a, b: (b in a)

# def reverse(s):
#      return s[::-1]

# reverse = lambda s : s[::-1] 
