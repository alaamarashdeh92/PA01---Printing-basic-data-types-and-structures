
# Symmetric Difference

odd_list = [1, 3, 5, 7, 9]
natural_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# DO NOT CHANGE CODE ABOVE THIS LINE

# TODO:
# Print a list of the difference between the two lists.
set_difference=set(natural_list)-set(odd_list)
list_difference=list(set_difference)
list_difference.sort()
print(list_difference)
# You cannot use the symmetric_difference() method for sets to solve this problem.
#
# For the input above, the printed list looks like this:
# >> [2, 4, 6, 8]