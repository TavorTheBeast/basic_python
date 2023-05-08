def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    if len(lines) < 3:
        lines += ['\n'] * (3 - len(lines))

    old_song = lines[2].split(';')[0]
    lines[2] = f'{new_song};{lines[2].split(";")[1]}'

    with open(file_path, 'w') as f:
        f.writelines(lines)

    with open(file_path, 'r') as f:
        updated_lines = f.readlines()
        print(''.join(updated_lines))

    return old_song


my_mp4_playlist(r"c:\my_files\songs.txt", "Python Love Story")
