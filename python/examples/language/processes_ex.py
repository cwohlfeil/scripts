# Queues transport messages, which can be any kind of information.
# In this case, we’re interested in queues for distributed task management,
# also known as work queues, job queues, or task queues.
# Use processes, networking, or events (discussed in the next section) for CPUbound problems
# Use threads for I/O bound problems

import multiprocessing as mp


def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()
    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()

