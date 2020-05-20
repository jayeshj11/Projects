import random

file = input('Enter the name of the file: ')
file2 = 'results.csv'

infile = open(file, 'r')
outfile = open(file2, 'w')

lines = infile.readlines()
print(lines[0], file = outfile)
lines = lines[1:]
counter = 0

while counter <= 75:
    index = random.choice(range(len(lines)))
    components = lines[index].split(',')
    count1 = 0
    for i in range(len(components)):
        if len(components[i]) == 0:
            count1 += 1
    if count1 > 0:
        counter += 0
    else:
        counter += 1
        x = lines[index]
        print(x, file = outfile)

infile.close()
outfile.close()
