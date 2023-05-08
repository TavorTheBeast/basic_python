def are_lists_equal(list1, list2):
    # check if the two lists have the same length
    if len(list1) != len(list2):
        print(False)

    # sort the lists and compare them
    print(sorted(list1) == sorted(list2))

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

are_lists_equal(list1, list3)
are_lists_equal(list1, list2)