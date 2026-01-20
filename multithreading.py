import threading
import time

# Task 1: Print numbers from 1 to 5
def task1():
    for i in range(1, 6):
        print(f"Task 1: {i}")
        time.sleep(1)  # Simulate work

# Task 2: Print letters from A to E
def task2():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Task 2: {letter}")
        time.sleep(1)  # Simulate work

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both tasks completed!")
