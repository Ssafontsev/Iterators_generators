import hashlib

def myGenerator(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for i in myGenerator('test.txt'):
    print(i)