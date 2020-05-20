file = input('Enter the name of the file: ')
file2 = 'results_final.csv'

infile = open(file, 'r')
outfile = open(file2, 'w')

lines = infile.readlines()
lines = lines[1:]
k = 1
data_hh = [0,0,0,0]
mean_hh = [0,0,0,0]

data_afs = [0,0,0,0]
mean_afs = [0,0,0,0]

data_s = [0,0,0,0]
mean_s = [0,0,0,0]

while k < len(lines):
    lines[k] = lines[k][:-1]
    components = lines[k].split(',')
    if components[-2] > components[-3]:
        components[-2] = 'black'
    else:
        components[-2] = 'white'

    integer = float(components[2])
    if integer <= 40000.0 and components[-2] == 'black':
        data_hh[0] += 1
        mean_hh[0] = mean_hh[0] + float(components[-1])
    elif integer > 40000.0 and components[-2] == 'black':
        data_hh[1] += 1
        mean_hh[1] = mean_hh[1] + float(components[-1])
    elif integer <= 40000.0 and components[-2] == 'white':
        data_hh[2] += 1
        mean_hh[2] = mean_hh[2] + float(components[-1])
    elif integer > 40000.0 and components[-2] == 'white':
        data_hh[3] += 1
        mean_hh[3] = mean_hh[3] + float(components[-1])


    integer1 = float(components[3])
    if integer1 <= 7041.5 and components[-2] == 'black':
        data_afs[0] += 1
        mean_afs[0] = mean_afs[0] + float(components[-1])
    elif integer1 > 7041.5 and components[-2] == 'black':
        data_afs[1] += 1
        mean_afs[1] = mean_afs[1] + float(components[-1])
    elif integer1 <= 7041.5 and components[-2] == 'white':
        data_afs[2] += 1
        mean_afs[2] = mean_afs[2] + float(components[-1])
    elif integer1 > 7041.5 and components[-2] == 'white':
        data_afs[3] += 1
        mean_afs[3] = mean_afs[3] + float(components[-1])

    integer2 = float(components[4])
    if integer2 <= 800 and components[-2] == 'black':
        data_s[0] += 1
        mean_s[0] = mean_s[0] + float(components[-1])
    elif integer2 > 800 and components[-2] == 'black':
        data_s[1] += 1
        mean_s[1] = mean_s[1] + float(components[-1])
    elif integer2 <= 800 and components[-2] == 'white':
        data_s[2] += 1
        mean_s[2] = mean_s[2] + float(components[-1])
    elif integer2 > 800 and components[-2] == 'white':
        data_s[3] += 1
        mean_s[3] = mean_s[3] + float(components[-1])

    k = k + 1

for x in range(len(mean_hh)):
    if mean_hh[x]!= 0 and data_hh[x]!=0:
        mean_hh[x] = mean_hh[x] // data_hh[x]
    else:
        mean_hh[x] = mean_hh[x]

for y in range(len(mean_afs)):
    if mean_afs[y]!= 0 and data_afs[y]!=0:
        mean_afs[y] = mean_afs[y] // data_afs[y]
    else:
        mean_afs[y] = mean_afs[y]

for z in range(len(mean_s)):
    if mean_s[z]!= 0 and data_s[z]!=0:
        mean_s[z] = mean_s[z] // data_s[z]
    else:
        mean_s[z] = mean_s[z]

print('mean_hh = ', mean_hh)
print('mean_afs = ', mean_afs)
print('mean_ss = ', mean_s)

infile.close()
outfile.close()
