# Places

# Think of at least five places in the world you’d like to visit.

# TODO: Store the locations in the list locations.
locations = ['Turkey', 'Dubai', 'Germany', 'Malaysia', 'China']

# TODO: Print your list in its original order.
print (locations)
# TODO:
# Sort and print your list in alphabetical order wihout modifying the actual list. Read about the sorted() function.
set1 = set (locations)
set1.copy()
x= list(set1)
x.sort()
print(x)
# Show that your list is still in its original order by printing it.
print(locations)
# TODO:
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
x.reverse()
print(x)
# Show that your list is still in its original order by printing it again.
print(locations)
# TODO: Use reverse() to change the order of your list. Print the list to show that its order has changed.
set2 = set (locations)
set2.copy()
y=list(set2)
y.reverse()
print(y)
# TODO: Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
y.reverse()
print(y)
print(locations)
# TODO: Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
set1 = set (locations)
set1.copy()
x= list(set1)
x.sort()
print(x)
# TODO: Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
x.reverse()
print(x)