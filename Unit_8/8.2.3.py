def mult_tuple(tuple1, tuple2):
    print([(a, b) for a in tuple1 for b in tuple2])


first_tuple = (1, 2)
second_tuple = (4, 5)
mult_tuple(first_tuple, second_tuple)