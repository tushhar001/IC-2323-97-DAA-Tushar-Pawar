
# Lab Task 1

## Part 1. Trace It Yourself

### Input:
[8, 3, 15, 6, 2]

### Output:
Largest Number: 15
Sorted List: [2, 3, 6, 8, 15]

### Comparisons made:
4 comparisons.

### Dry Run:
Initial maximum = 8

i = 1, A[i] = 3, max = 8, comparisons = 1
i = 2, A[i] = 15, max = 15, comparisons = 2
i = 3, A[i] = 6, max = 15, comparisons = 3
i = 4, A[i] = 2, max = 15, comparisons = 4

### Sorting method used:
Bubble Sort.

### Sorting steps:
Pass 1: [3, 8, 6, 2, 15]
Pass 2: [3, 6, 2, 8, 15]
Pass 3: [3, 2, 6, 8, 15]
Pass 4: [2, 3, 6, 8, 15]
Pass 5: [2, 3, 6, 8, 15]

### Data Structure Used:
Python List (Array).

### Explanation:
The program checks every element to find the
largest number. It updates the maximum whenever
a larger element is found.

Bubble Sort compares adjacent elements and
swaps them when they are in the wrong order.

### Complexity:
Finding maximum: O(n) - Linear.
Bubble Sort: O(n²) - Quadratic.

If input size grows 100 times, finding the
maximum requires approximately 100 times
more comparisons.

Bubble Sort may require approximately
10,000 times more operations in the
worst case because its complexity is O(n²).



## Part 2. Stack or Queue

### Input:
Task1, Task2, Task3, Task4, Task5

### Stack order:
Task5, Task4, Task3, Task2, Task1

### Queue order:
Task1, Task2, Task3, Task4, Task5

### Printer should use:
Queue (FIFO).

### Reason:
A printer should print jobs in the order
they arrive. Queue follows First In,
First Out (FIFO), so the first submitted
job gets printed first.

### Dry Run:

Stack (LIFO):
Push Task1, Task2, Task3, Task4, Task5.
Pop in reverse order.

Queue (FIFO):
Enqueue Task1, Task2, Task3, Task4, Task5.
Dequeue in the same order.

### Data Structure Used:
Python List.

### Explanation:
Stack follows Last In, First Out, which
means the last inserted task is removed first.

Queue follows First In, First Out, which
means the first inserted task is removed first.
A printer uses a queue to maintain the
correct order of printing jobs.

### Complexity:
Stack insertion and removal: O(1) each.

Queue insertion: O(1) using list append.
Queue removal using pop(0): O(n).

If input grows 100 times, stack operations
remain constant per task, while list-based
queue removal becomes more expensive.
A deque can provide O(1) queue operations.


## Part 3. Build a Small Tree

### Input:
Subjects:
Math, Science, Physics, Chemistry,
Algebra, Geometry.

### Tree Structure:

Level 0: Math, Science

Level 1 under Math:
Algebra, Geometry

Level 1 under Science:
Physics, Chemistry

### Level Order Traversal:
Math, Science, Algebra, Geometry,
Physics, Chemistry.

### Dry Run:
Start Queue: Math, Science

1. Visit Math.
   Add Algebra, Geometry.

2. Visit Science.
   Add Physics, Chemistry.

3. Visit Algebra.
4. Visit Geometry.
5. Visit Physics.
6. Visit Chemistry.

Final Queue: Empty.

### Data Structure Used:
Tree (represented using Dictionary)
and Queue (for traversal).

### Explanation:
A tree is a non-linear data structure
that represents hierarchical relationships.

Level order traversal visits nodes level
by level, from left to right. It uses a
queue to process nodes in FIFO order.

### Complexity:
Time Complexity: O(n)
Space Complexity: O(n)

If the number of nodes grows 100 times,
the traversal effort also grows approximately
100 times when an efficient queue is used.

# IC-2323-54-DAA-lalit-solanki
