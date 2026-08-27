# Concurrency Assignment - [Touhid Ara Himu]
# ID: 2312187042
# Course: CSE425 | Summer 2026


## How to Run
Make sure you have **Python 3.8+** installed. No external libraries needed.
Make sure your codes folder directory is correct in the terminal. The program will not run if the directory is wrong.

For MACOS Run these commands on the Terminal. 
```bash
python3 part1_race_condition.py
python3 part2_producer_consumer.py
python3 part3_dining_philosophers.py
python3 part4_thread_pool.py
```

## Part 1: Race Condition

This program demonstrates how multiple threads accessing a shared variable
without protection leads to wrong results (race condition), and how adding
a `threading.Lock` fixes the problem by allowing only one thread to
increment the counter at a time.

I learned that even a simple `counter += 1` is not atomic at the CPU
level — it is actually three steps (read, add, write). Without a lock, two
threads can read the same stale value and one update gets silently lost.


## Part 2: Producer-Consumer

This program simulates a bakery where baker threads produce bread and
customer threads consume it using a thread-safe `queue.Queue` as the
shared basket.

I learned that `queue.Queue` handles all synchronization internally —
`put()` blocks automatically when the basket is full and `get()` blocks
when it is empty, eliminating the need for explicit locks.


## Part 3: Dining Philosophers

This program models 3 philosophers sharing 3 forks. Deadlock is prevented
using `resource ordering`: every philosopher always picks up the
lower-numbered fork first, which breaks the circular-wait condition.

I learned that deadlock requires four conditions to occur simultaneously
(mutual exclusion, hold-and-wait, no preemption, circular wait), and
breaking even one condition (here: circular wait) is enough to prevent it.


## Part 4: Thread Pool

This program runs 10 tasks first sequentially, then in parallel using
`concurrent.futures.ThreadPoolExecutor` with 4 workers, and compares the
execution times.

I learned that for I/O-bound tasks (tasks that spend time waiting),
parallel execution with a thread pool gives a significant speed-up because
threads wait simultaneously instead of one after another. The speed-up
factor roughly equals the number of worker threads used.


## General Observations

- Concurrency bugs (like race conditions) are non-deterministic and hard
  to reproduce — they may or may not appear on each run.
- Python's Global Interpreter Lock (GIL) limits true CPU parallelism for
  threads; `multiprocessing` would be better for pure computation.
- Good synchronization primitives (Lock, Queue, ThreadPool) make writing
  correct concurrent code much easier.
