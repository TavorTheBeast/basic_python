def my_mp3_playlist(file_path):
    with open(file_path, 'r') as f:
        songs = f.readlines()

    song_lengths = {}
    song_performers = {}
    song_count = len(songs)
    max_length = 0
    max_length_song = ''
    max_operation_count = 0
    max_operation = ''

    for song in songs:
        song_parts = song.strip().split(';')
        song_name = song_parts[0]
        song_performer = song_parts[1]
        song_length = song_parts[2]

        # Calculate length of song in seconds
        minutes, seconds = map(int, song_length.split(':'))
        length_in_seconds = minutes * 60 + seconds

        # Update dictionary for song lengths
        song_lengths[song_name] = length_in_seconds

        # Update dictionary for song performers
        if song_performer not in song_performers:
            song_performers[song_performer] = 0
        song_performers[song_performer] += 1

        # Update variables for longest song
        if length_in_seconds > max_length:
            max_length = length_in_seconds
            max_length_song = song_name

    # Find most frequent operation
    operations = {}
    for song in songs:
        operation = song.strip().split(';')[1]
        if operation not in operations:
            operations[operation] = 0
        operations[operation] += 1

        if operations[operation] > max_operation_count:
            max_operation_count = operations[operation]
            max_operation = operation

    with open('found.txt', 'w') as f:
        for song_name, length in song_lengths.items():
            if length == -1:
                f.write(f'Missing song: {song_name}\n')

    return (max_length_song, song_count, max_operation)


result = my_mp3_playlist('songs.txt')
print(result) 
