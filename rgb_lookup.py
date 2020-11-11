# RGB Lookup

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]

print(f'I have learned the RGB code for {len(colours)} colours so far.')

colour = input("Please enter a colour name: ")

# DO NOT CHANGE CODE ABOVE THIS LINE

# TODO:
# Given a colour name as input from the user print the RGB code for that colour.
red =colours[0][1].title()
print(red)
yellow =colours[1][1]
print(yellow)
green =colours[2][1]
print(green)
cyan =colours[3][1]
print(cyan)
blue =colours[4][1]
print(blue)
magenta =colours[5][1]
print(magenta)
# C=dict(colours)
# print(C)
# x=C.values()
# print(x)
# y=C.keys()
# print(y)


# The input case should be ignored, 'RED' and 'red' should both print the same code.
# The ouput should look something like this:
# >> The RGB code for 'red' is 'F00'.
#