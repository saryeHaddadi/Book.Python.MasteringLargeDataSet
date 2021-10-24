from time import process_time_ns, sleep
from multiprocessing import Pool


def times_two(x):
  return x*2+7


def lazy_map(xs):
  return list(map(times_two, xs))


def parallel_map(xs, chunck=8500):
  with Pool(2) as P:
    x =  P.map(times_two, xs, chunck)
  return x

if __name__ =='__main__':
  for i in range(0, 7):
    N = 10**i
    t1 = process_time_ns()
    lazy_map(range(N))
    lm_time = process_time_ns() - t1

    t1 = process_time_ns()
    parallel_map(range(N))
    par_time = process_time_ns() - t1
    print("""
  -- N = {} --
  Lazy map time:      {}
  Parallel map time:  {}
  """.format(N, lm_time, par_time))
