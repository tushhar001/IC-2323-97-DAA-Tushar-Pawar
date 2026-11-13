
# Part 1: Trace It Yourself

numbers = [8, 3, 15, 6, 2]

# Find the largest number
maximum = numbers[0]
comparisons = 0

for i in range(1, len(numbers)):
    comparisons += 1

    if numbers[i] > maximum:
        maximum = numbers[i]

print("Original List:", numbers)
print("Largest Number:", maximum)
print("Comparisons Made:", comparisons)


# Sorting using Bubble Sort
arr = numbers.copy()

print("\nSorting Steps:")

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Pass", i + 1, ":", arr)

print("\nSorted List:", arr)
