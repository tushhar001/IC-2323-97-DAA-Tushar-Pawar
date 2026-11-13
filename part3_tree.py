
# Part 3: Build a Small Tree

# Creating the tree using a dictionary
tree = {
    "Math": ["Algebra", "Geometry"],
    "Science": ["Physics", "Chemistry"]
}

print("Subject Tree:")

# Display parent and child subjects
for parent, children in tree.items():
    print(parent)

    for child in children:
        print("  ->", child)


# Level Order Traversal
print("\nLevel Order Traversal:")

queue = ["Math", "Science"]

while queue:
    current = queue.pop(0)

    print(current, end=" ")

    # Add children of the current subject
    if current in tree:
        for child in tree[current]:
            queue.append(child)

print()

