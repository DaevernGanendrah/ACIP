import threading
import time

def worker():
    """thread worker function"""
    for i in range(1000):
        print(i,end='\t')
        if ((i%10)==0):
            print()
    print("Worker ended....")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
print("Main ended....")