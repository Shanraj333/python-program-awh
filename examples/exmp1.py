def count_fruit_occurrences(fruit_string):
    # Split the string into a list of fruit names
    fruit_list = fruit_string.split()

    # Create an empty dictionary to store counts
    fruit_count = {}

    # Iterate over each fruit in the list
    for fruit in fruit_list:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1

    return fruit_count


# Example input
fruits = "orange apple grapes pineapple apple"

# Get the fruit count dictionary
result = count_fruit_occurrences(fruits)

# Print the result
print(result)
