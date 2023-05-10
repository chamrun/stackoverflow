from multiprocessing import Pool
def f(x):
    print(x)
    out= x*x
    return out

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))