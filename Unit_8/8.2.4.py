def sort_anagrams(list_of_strings):
    sorted_strings = sorted(list_of_strings)
    anagram_groups = []
    for string in sorted_strings:
        found_group = False
        for group in anagram_groups:
            if sorted(group[0]) == sorted(string):
                group.append(string)
                found_group = True
                break
        if not found_group:
            anagram_groups.append([string])
    print(anagram_groups)


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
sort_anagrams(list_of_words)