def reverse_file_contents(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()

    return contents[::-1]
def reverse_files(file1, file2):
    reversed_contents = reverse_file_contents(file1)

with open(file2, 'w') as f:
    f.write(reversed_contents)
    reverse_files('file1.txt', 'file2.txt')
with open('file2.txt', 'r') as f:
    contents = f.read()
    print(contents)
