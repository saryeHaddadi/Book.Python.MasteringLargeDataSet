#from pathos.multiprocessing import ProcessPool
from multiprocessing import Pool, current_process

def print_and_return(x):
    print(x); return x

def start_process():
    print("Starting: ", current_process().name)

if __name__ == '__main__': 
    with Pool(processes=2,
            initializer=start_process) as P:
        P.map(print_and_return, range(20))