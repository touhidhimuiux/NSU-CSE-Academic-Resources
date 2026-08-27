# Touhid Ara Himu

import threading
import time
import queue

# Shared resource: the basket where bread is placed by bakers and taken by customers.
# maxsize=5 means bakers must wait when the basket is full.
basket = queue.Queue(maxsize=5)

TOTAL_BREAD = 10        # total bread to be produced and consumed (2 bakers × 5 each = 10)
STOP_SIGNAL = "STOP"    # special value to signal customers to stop when all bread is consumed


# Baker (Producer) – makes bread and puts it in the basket
def baker(name, num_items):
    for i in range(num_items):
        bread = f"Bread-{i}"
        basket.put(bread)                   # blocks automatically if basket is full
        print(f"{name} made {bread}")
        time.sleep(0.3)                     # bakers produce faster than customers eat

    print(f"  [Baker]    {name} finished baking.")


# Customer (Consumer) – takes bread from the basket and eats it
def customer(name, num_items):
    eaten = 0
    while eaten < num_items:
        bread = basket.get()                # blocks automatically if basket is empty
        if bread == STOP_SIGNAL:            # check if stop signal received
            basket.put(STOP_SIGNAL)         # pass signal along for other customers
            break
        print(f"{name} ate {bread}")
        basket.task_done()
        eaten += 1
        time.sleep(0.6)                     # customers eat slower than bakers produce

    print(f"  [Customer] {name} is full.")


# Main function to set up and run the producer-consumer simulation
if __name__ == "__main__":
    print("  Part 2 – Producer-Consumer (Bakery Simulation)")

    # 2 bakers × 5 bread each = 10 total items
    # 2 customers × 5 bread each = 10 total consumed
    baker_threads = [
        threading.Thread(target=baker, args=("Baker-1", 5), daemon=True),
        threading.Thread(target=baker, args=("Baker-2", 5), daemon=True),
    ]
    customer_threads = [
        threading.Thread(target=customer, args=("Customer-1", 5), daemon=True),
        threading.Thread(target=customer, args=("Customer-2", 5), daemon=True),
    ]

    # Start all threads
    for t in baker_threads + customer_threads:
        t.start()

    # Wait for all bakers to finish producing
    for t in baker_threads:
        t.join()

    # Wait for all bread in the queue to be consumed
    basket.join()

    # Send stop signal so customer threads exit cleanly
    basket.put(STOP_SIGNAL)

    # Wait for all customers to finish
    for t in customer_threads:
        t.join()

    print("\nAll bread has been baked and eaten!")

    ================================ Question Answers ===========================
    
    # HOW the queue prevents overflow:
    #   queue.Queue(maxsize=5) makes basket.put() block when 5 items are already inside,
    #   no extra bread can be added until a customer takes one out,
    #   ensuring the basket never exceeds its capacity.
    #
    # HOW the queue prevents underflow:
    #   basket.get() blocks when the basket is empty,
    #   customers simply wait instead of crashing on an empty list,
    #   ensuring they only consume what is available.
    #
    # RESULT: no explicit locks needed;
    #         Queue handles all synchronization internally,
    #         making the producer-consumer problem straightforward to implement.

    # What happens if the basket is full:
    #   The baker thread is blocked at basket.put() and cannot add more bread.
    #   It simply waits until a customer takes something.
    #   No crash, no data loss — just automatic waiting.

    # What happens if the basket is empty:
    #   The customer thread is blocked at basket.get() and cannot take anything.
    #   It waits until a baker adds new bread.
    #   Again no crash — the thread just pauses automatically.