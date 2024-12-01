# Load the data from the uploaded file
file_path = '../data/01.txt'

# Read the data from the file
with open(file_path, 'r') as file:
    data = file.readlines()

# Parse the data into two separate lists
left_list = []
right_list = []

for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()

# Calculate the total distance
total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
print(total_distance)

# Part 2.
from collections import Counter

# Count occurrences of each number in the right list
right_counts = Counter(right_list)

# Calculate the similarity score
similarity_score = sum(num * right_counts[num] for num in left_list)
print(similarity_score)
