def inverse_dict(my_dict):
    inv_dict = {}
    for key, value in my_dict.items():
        if value not in inv_dict:
            inv_dict[value] = [key]
        else:
            inv_dict[value].append(key)
            inv_dict[value].sort()
    print(inv_dict)

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
inverse_dict(course_dict)
