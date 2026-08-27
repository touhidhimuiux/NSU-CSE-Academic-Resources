# Touhid Ara Himu

import threading
import time
import random

# 3 forks represented as Lock objects.
# Fork index acts as its "ID" (0, 1, 2) for philosophers 0, 1, 2 respectively. we used resource ordering to prevent deadlock.
NUM_PHILOSOPHERS = 3
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]


# Deadlock prevention method used:
#   Option A – "Resource Ordering"
#   Each philosopher always picks up the lower numbered fork first.
#   This breaks the circular-wait condition that causes deadlock.
#
#   Without ordering, every philosopher might grab their left fork simultaneously and then wait forever for the right one -> deadlock.
#   With ordering, at least one philosopher always gets both forks.
def philosopher(philosopher_id, eat_times=3):
    left  = philosopher_id                            # e.g., Phil-0 -> fork 0
    right = (philosopher_id + 1) % NUM_PHILOSOPHERS   # e.g., Phil-0 -> fork 1

    # Determine the order of picking up forks based on their IDs to prevent deadlock.
    first_fork  = min(left, right)
    second_fork = max(left, right)

    for round_num in range(1, eat_times + 1):
        # Think
        think_time = random.uniform(0.5, 1.5)
        print(f"  Philosopher {philosopher_id} is thinking...")
        time.sleep(think_time)

        # Get hungry
        print(f"  Philosopher {philosopher_id} is hungry.")

        # Pick up forks (lower number first)
        with forks[first_fork]:
            print(f"  Philosopher {philosopher_id} picked up fork {first_fork}")

            with forks[second_fork]:
                print(f"  Philosopher {philosopher_id} picked up fork {second_fork}")

                # Eat
                eat_time = random.uniform(0.5, 1.0)
                print(f"  Philosopher {philosopher_id} is eating...")
                time.sleep(eat_time)

                print(f"  Philosopher {philosopher_id} finished eating, putting down forks.")
            # second_fork released here automatically

        # first_fork released here automatically

    print(f"  Philosopher {philosopher_id} is DONE for today.")


# Main entry point
if __name__ == "__main__":
    print("  Part 3 - Dining Philosophers")

    threads = [
        threading.Thread(target=philosopher, args=(i, 3), name=f"Phil-{i}")
        for i in range(NUM_PHILOSOPHERS)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("\nAll philosophers have finished dining. No deadlock occurred!")

    ================================ Question Answers ===========================


    # Explanation:
    # WHY RESOURCE ORDERING PREVENTS DEADLOCK:
    #   Deadlock requires 4 conditions to occur at the same time:
    #     1. Mutual Exclusion  – only one philosopher can hold a fork
    #     2. Hold and Wait     – holding one fork while waiting for another
    #     3. No Preemption     – forks cannot be forcibly taken away
    #     4. Circular Wait     – each philosopher waits on the next one
    #
    #   Resource ordering breaks the CIRCULAR WAIT condition.
    #   Without ordering, all 3 philosophers could grab their left fork
    #   simultaneously and wait forever for the right one → deadlock.
    #   With ordering, Philosopher 2 must grab fork 0 before fork 2.
    #   But Philosopher 0 also needs fork 0 first — so they compete.
    #   Whoever wins fork 0 can proceed and finish eating.
    #   The circular chain is broken → deadlock is impossible.