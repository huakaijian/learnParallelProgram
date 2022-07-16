import multiprocessing


def foo(i):
    print(f'call function in process {i}')
    return


if __name__ == '__main__':
    process_job = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        process_job.append(p)
        p.start()
        p.join()

""":returns
call function in process 0
call function in process 1
call function in process 2
call function in process 3
call function in process 4
"""
