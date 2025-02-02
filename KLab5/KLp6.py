bands=[]
filename='bands.txt'
with open(filename) as fin:
    for line in fin:
        bands.append(line.strip())
bands.sort()
print(bands)

filename='bands_sorted.txt'
with open(filename,'w') as fout:
    fout.write(' '.join(bands))
