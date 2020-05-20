file = input('Enter the name of the file: ')
file2 = 'results.csv'

infile = open(file, 'r')
outfile = open(file2, 'w')

lines = infile.readlines()
print(lines[0], file = outfile)
lines = lines[1:]
counter = 0
k = 1

while k < len(lines):
    lines[k] = lines[k][:-1]
    components = lines[k].split(',')
    count1 = 0
    if components[-2] > components[-3]:
        components[-2] = 'black'
    else:
        components[-2] = 'white'

    integer = float(components[2])
    if integer <= 20000.0:
        components[2] = '0K-20K'
    elif integer > 20000 and integer <= 40000:
        components[2] = '20K-40K'
    elif integer > 40000 and integer <= 60000:
        components[2] = '40K-60K'
    elif integer > 60000 and integer <= 80000:
        components[2] = '60K-80K'
    else:
        components[2] = '>80K'

    integer1 = float(components[3])
    if integer1 <= 5000:
        components[3] = '0K-5K'
    elif integer1 > 5000 and integer1 <= 10000:
        components[3] = '5K-10K'
    elif integer1 > 10000 and integer1 <= 15000:
        components[3] = '10K-15K'
    elif integer1 > 15000 and integer1 <= 20000:
        components[3] = '15K-20K'
    else:
        components[3] = '>20K'

    integer2 = float(components[4])
    if integer2 <= 320:
        components[4] = '0-320'
    elif integer2 > 320 and integer2 <= 640:
        components[4] = '320-640'
    elif integer2 > 640 and integer2 <= 960:
        components[4] = '640-960'
    elif integer2 > 960 and integer2 <= 1280:
        components[4] = '960-1280'
    else:
        components[4] = '>1280'

    integer3 = float(components[-1])
    if integer3 <= 32000:
        components[-1] = '0-32K'
    elif integer3 > 32000 and integer3 <= 64000:
        components[-1] = '32K-64K'
    elif integer3 > 64000 and integer2 <= 96000:
        components[-1] = '64K-96K'
    elif integer3 > 96000 and integer3 <= 128000:
        components[-1] = '96K-128K'
    else:
        components[-1] = '>128K'

    for i in range(len(components)):
        if len(components[i]) == 0:
            count1 += 1
    if count1 == 0:
        counter += 1
        x = ','.join(components)
        print(x, file = outfile)
    k = k + 1

print('There are', counter, 'institutions with no missing values')

infile.close()
outfile.close()
