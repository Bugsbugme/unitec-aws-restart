# Sets
# my_list = [1, 5, 8, 1, 9, 2, 5]
# my_set = set(my_list)
# my_unique_list = list(my_set)

# Intersections
your_colours = {"Red", "Green", "Blue", "Purple"}
my_colours = {"Red", "Orange", "Purple"}
their_colours = {"Yellow", "Purple", "Pink"}
our_colours = your_colours.intersection(my_colours.intersection(their_colours))
our_colours2 = your_colours & my_colours & their_colours
