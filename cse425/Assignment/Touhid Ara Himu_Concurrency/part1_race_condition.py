# Touhid Ara Himu

import threading
import time


# Counter WITHOUT a lock (demonstrates race condition)
class UnsafeCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # Artificially slow down the read-modify-write steps
        # so the race condition is clearly visible here.
        temp = self.value
        time.sleep(0.00001)   # tiny delay exposes the race
        temp = temp + 1
        self.value = temp


# Counter WITH a lock (safe version)
class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            temp = self.value
            temp = temp + 1
            self.value = temp


# Worker function that increments the counter multiple times
def worker(counter, times=100):
    for _ in range(times):
        counter.increment()


# Helper to run threads and return the final counter value
def run_threads(counter, num_threads=3, increments_each=100):
    threads = [threading.Thread(target=worker, args=(counter, increments_each))
               for _ in range(num_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter.value


# Main entry point
if __name__ == "__main__":
    NUM_THREADS  = 3
    INCREMENTS   = 1000
    EXPECTED     = NUM_THREADS * INCREMENTS   # 3000

    # Run WITHOUT lock
    unsafe = UnsafeCounter()
    result_unsafe = run_threads(unsafe, NUM_THREADS, INCREMENTS)
    print(f"\nWITHOUT LOCK:")
    print(f"  Final counter value: {result_unsafe}  {'(WRONG!)' if result_unsafe != EXPECTED else '(got lucky, run again!)'}")

    # Run WITH lock
    safe = SafeCounter()
    result_safe = run_threads(safe, NUM_THREADS, INCREMENTS)
    print(f"\nWITH LOCK:")
    print(f"  Final counter value: {result_safe}  {'(CORRECT!)' if result_safe == EXPECTED else '(WRONG!)'}")

================================ Question Answers ===========================

# WHY the first version gives wrong results:
#     Because multiple threads read the same value before any of them writes back, so
         some increments get lost.

# HOW the lock fixes the problem:
#     The lock allows only one thread at a time to increment the counter, so 
       no updates are ever lost.
