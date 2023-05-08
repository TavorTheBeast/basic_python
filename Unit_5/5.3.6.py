def fix_age(age):
    if age in range(13, 15) or age in range(17, 20):
        return 0
    else:
        return age

def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    print(a + b + c)



filter_teens()

filter_teens(1, 2, 3)

filter_teens(2, 13, 1)

filter_teens(2, 1, 15)