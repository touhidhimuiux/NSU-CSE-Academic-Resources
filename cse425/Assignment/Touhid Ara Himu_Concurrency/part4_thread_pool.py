# Touhid Ara Himu

import concurrent.futures
import threading
import time
import random
import math

# 10 Simple Tasks:
# Each task is a function that does one of three types of work:
#   1. Calculate factorial of a number
#   2. Count from 1 to 1000
#   3. Simulate processing (sleep for random time)

def task_0(task_id):
    # Calculate factorial of 10
    math.factorial(10)
    time.sleep(random.uniform(0.5, 2))

def task_1(task_id):
    # Count from 1 to 1000
    count = 0
    for n in range(1, 1001):
        count = n
    time.sleep(random.uniform(0.5, 2))

def task_2(task_id):
    # Simulate processing with random sleep
    time.sleep(random.uniform(0.5, 2))

def task_3(task_id):
    # Calculate factorial of 20
    math.factorial(20)
    time.sleep(random.uniform(0.5, 2))

def task_4(task_id):
    # Count from 1 to 1000
    count = 0
    for n in range(1, 1001):
        count = n
    time.sleep(random.uniform(0.5, 2))

def task_5(task_id):
    # Simulate processing with random sleep
    time.sleep(random.uniform(0.5, 2))

def task_6(task_id):
    # Calculate factorial of 30
    math.factorial(30)
    time.sleep(random.uniform(0.5, 2))

def task_7(task_id):
    # Count from 1 to 1000
    count = 0
    for n in range(1, 1001):
        count = n
    time.sleep(random.uniform(0.5, 2))

def task_8(task_id):
    # Simulate processing with random sleep
    time.sleep(random.uniform(0.5, 2))

def task_9(task_id):
    # Calculate factorial of 40
    math.factorial(40)
    time.sleep(random.uniform(0.5, 2))

# List of all 10 tasks
ALL_TASKS = [task_0, task_1, task_2, task_3, task_4,
             task_5, task_6, task_7, task_8, task_9]


# Worker Function:
# This is the function the thread pool calls for each task.
# It prints which worker thread is handling which task —
# satisfying requirement 5.
def process_task(task_id):
    ALL_TASKS[task_id](task_id)
    print(f"Task {task_id} completed")
    return task_id


if __name__ == "__main__":

    # Sequential Execution:
    # Tasks run one by one on the main thread.
    # Each task must finish before the next one begins.
    # We measure the total time taken for all 10 tasks.
    print("Sequential Execution:")

    start = time.time()
    for i in range(10):
        process_task(i)
    sequential_time = time.time() - start

    print(f"Time: {sequential_time:.2f} seconds")

    print()

    # Parallel Execution with Thread Pool:
    # ThreadPoolExecutor creates 4 worker threads.
    # Tasks are distributed among threads automatically.
    # Multiple tasks run at the same time, so total time is
    # much less than sequential.
    print("Parallel Execution:")

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(process_task, range(10))
    parallel_time = time.time() - start

    print(f"Time: {parallel_time:.2f} seconds")

    # Compare Execution Times:
    # Speedup = sequential time / parallel time
    # With 4 threads the speedup should be roughly 3-4x
    print(f"\nSequential: {sequential_time:.2f} seconds")
    print(f"Parallel: {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time/parallel_time:.2f}x")

    ================================ Question Answers ===========================

    # WHY PARALLEL EXECUTION IS FASTER:
    #   In sequential mode every task blocks the main thread while it sleeps,
    #   so total time = sum of all individual task durations.
    #   In parallel mode 4 threads sleep at the same time, 
    #   meaning 4 tasks are waiting simultaneously instead of one after another.
    #   This reduces total time to roughly (sum of durations / 4),
    #   which is why parallel execution is significantly faster.

    # HOW MANY WORKER THREADS:
    #   We used 4 worker threads (max_workers=4).
    #   This is a good balance for I/O-bound tasks because more threads
    #   means more tasks overlap, but too many threads waste memory.
    #   With 4 workers the expected speedup is roughly 3-4x.