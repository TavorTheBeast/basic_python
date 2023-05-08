def who_is_missing(file_name):
    with open(file_name) as f:
        numbers = f.read().split(',')
        numbers = [int(n) for n in numbers]
        sorted_numbers = sorted(numbers)
        missing_number = None
        for i in range(len(sorted_numbers)):
            if sorted_numbers[i] != i + 1:
                missing_number = i + 1
                break
        if missing_number:
            with open('found.txt', 'w') as f:
                f.write(str(missing_number))
        return missing_number
