import threading
import time

counter = 0

def increment():
    global counter
    temp = counter
    time.sleep(0.1)  # simulate some delay
    counter = temp + 1

def run_threads():
    global counter
    counter = 0
    threads = [threading.Thread(target=increment) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter