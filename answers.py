# 1. Create an empty list called my_list
my_list = []  # Creates an empty list

# 2. Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)  # Adds 10 to the list
my_list.append(20)  # Adds 20 to the list
my_list.append(30)  # Adds 30 to the list
my_list.append(40)  # Adds 40 to the list

# 3. Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Inserts 15 at index 1 (second position)

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])  # Adds multiple elements at the end of the list

# 5. Remove the last element from my_list
my_list.pop()  # Removes the last element (70)

# 6. Sort my_list in ascending order
my_list.sort()  # Sorts the list in increasing order

# 7. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)  # Finds the index of the first occurrence of 30
print(index_of_30)  # Prints the index
