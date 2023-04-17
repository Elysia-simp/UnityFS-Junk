import os

directory = input("Enter the directory path: ").replace("\\", "/")

remove_offset = input("y/n automatically skip some data?: ").lower() == 'y'

if remove_offset:
    seek_start = int(input("input offset? (1, 10, 20, 30): "))

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r+b') as f:
            if remove_offset:
                f.seek(seek_start)
                data = f.read()
                f.seek(0)
                f.write(data)
                f.truncate(len(data))
            f.seek(0)
            try:
                start = f.read().index(bytes.fromhex('556e6974794653'))
                f.seek(start)
                data = f.read()
                f.seek(0)
                f.write(data)
                f.truncate(len(data))
            except ValueError:
                pass
