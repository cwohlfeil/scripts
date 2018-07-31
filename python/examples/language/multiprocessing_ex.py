from multiprocessing import Pool


def spawn():
    print('Spawned')


def job(num):
    return num * 2

if __name__ == '__main__':
    for i in range(5):
        p = Pool(processes=20)
        data = p.map(job, range(20))
        p.close()
        print(data)
