def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()
        unique_words = list(set(words))
        num_unique_words = len(unique_words)
        selected_word = unique_words[(index - 1) % num_unique_words]
        return (num_unique_words, selected_word)


choose_word(r"c:\words.txt", 3)