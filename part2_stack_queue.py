
# Part 2: Stack or Queue

tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

# Stack (LIFO)
stack = []

for task in tasks:
    stack.append(task)

print("Stack Completion Order:")

while stack:
    print(stack.pop())


# Queue (FIFO)
queue = []

for task in tasks:
    queue.append(task)

print("\nQueue Completion Order:")

while queue:
    print(queue.pop(0))


# Printer uses Queue
printer = []

for task in tasks:
    printer.append(task)

print("\nPrinter Printing Order:")

while printer:
    print(printer.pop(0))
