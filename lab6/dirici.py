import os
path = "C:/Users/Professional/Documents/demo"
cfile = "C:/Users/Professional/Documents/demo/lab6/bobik/file.txt"
tfile = "C:/Users/Professional/Documents/demo/lab6/bobik/file.txt"
ld = ['bam', 'badum', 'purum']
def task1(path):
    print([name for name in os.listdir(path)])
    print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
    print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
task1(path)
def task2(path):
    if os.path.exists(path):
        result = 'Path is '

        result += 'readable, ' if os.access(path, os.R_OK) else 'not readable, '

        result += 'writable, ' if os.access(path, os.W_OK) else 'not writable, '

        result += 'executable' if os.access(path, os.X_OK)else 'not executable.'

        print(f'Path {path} exists\n{result}')

    else:
        print(f'Path {path} does not exists')
task2(path)
def task3(path):
    if os.path.exists(path):
        print(f'Path {path} exists')
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f'Path {path} does not exists')
task3(tfile)
def task4(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'Numbers of lines = {len(lines)}')
task4(tfile)
def task5(path, l):
    try:
        with open(path, 'w') as file:
            file.write(' '.join(l))
    except PermissionError:
        print(f"Error: No write permission for {path}")
task5(path, ld)        
def task6():
    from string import ascii_uppercase
    for letter in ascii_uppercase:
        with open(f'{letter}.txt', 'w'):
            pass
task6()
def task7(path1, path2):
    with open(path1, 'r') as file1, open(path2, 'a') as file2:
        file2.write(file1.read())
task7(tfile, cfile)
def task8(path):
    if os.access(path, os.F_OK):
        os.remove(path)
        print('File exists and has been removed')
    else:
        print(f"Error: File '{path}' does not exist.")
task8(cfile)