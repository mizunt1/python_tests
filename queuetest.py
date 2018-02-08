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
        data_received.append(a)
        print(data_received)

        
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

