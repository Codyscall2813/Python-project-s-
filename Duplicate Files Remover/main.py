import hashlib
import os

def calculate_file_hash(filename):
    BLOCK_SIZE = 65536
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCK_SIZE)
        while buffer:
            hasher.update(buffer)
            buffer = file.read(BLOCK_SIZE)
    return hasher.hexdigest()

if __name__ == "__main__":
    # Specify the directory to check
    directory_path = 'path/to/your/directory'

    # Dictionary to store file hashes
    hash_map = {}
    deleted_files = []

    # List of files in the specified directory
    files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for file in files:
        file_hash = calculate_file_hash(file)
        if file_hash in hash_map:
            deleted_files.append(file)
            os.remove(file)
        else:
            hash_map[file_hash] = file

    if deleted_files:
        print('Deleted Files:')
        for file in deleted_files:
            print(file)
    else:
        print('No duplicate files found')
