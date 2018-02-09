"""
first use of queue
explains some concepts about deamon
set deamon = False if you want to keep the thread running after the main thread has ended.
i.e. you want the job to complete regardless of how long it takes after the program has
finished executing
A queue stores multiple pieces of info. But only the oldest piece of info can be obtained from
the list. This is done by queue.get()
"""


from queue import Queue
import time
import threading
queue = Queue(maxsize=100)


def data_puller_worker():
    for i in range(20):
        print("putting on list")
        pull_data = [i+1, i+2, i+3, i+4]
        queue.put(pull_data)
        time.sleep(1)


def data_plotter():
    data_received = []
    while True:
        
        a = queue.get()
        # queue.get retrieves the most recent item in the queue
        # "remove and return an item from the queue"
        print("queue size")
        print(queue.qsize())
        # one item is added to queue, and get() is performed immediately, so qsize is always zero.
        # if a sleep statement is put in, which is greater than sleep in the data_puller_worker
        # sleep, then the qsize will increase
        time.sleep(2)
        data_received.append(a)
        print(a)

        
def main():
    t = threading.Thread(target=data_puller_worker)
    g = threading.Thread(target=data_plotter)
    t.daemon = True
    # daemon boolean must be specified before the thread is started
    # the python program will close when all daemon=False are gone
    # main thread is not a deamon thread (daemon = False)
    
    g.daemon = True
    t.start()
    g.start()
    time.sleep(5)
    # if g.deamon = True, we need to put in this time.sleep(5) statement to keep the main() thread
    # running while the g and t threads run.
    # without the sleep, the threads dont have time to run before the main thread stops

main()

