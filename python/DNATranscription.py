dna = input()
valid = 'GCTA'
c = {"G": "C", "C": "G", "T": "A", "A": "U"}
rna = []
for i in dna:
    if i.upper() in valid:
        rna.append(c[i.upper()])
if len(rna) == len(dna):
    print(*rna, sep="")
else:
    print("Invalid Input")