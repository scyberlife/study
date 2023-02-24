data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations, codes = [], []
num = {'0700','0500','0999','0555','0222','0777'}
o=0
for i in data:
    codes.append(i) if i.isnumeric() else designations.append(i)
operators = {}
i,k = 0,0
while i < len(designations):
    operators[designations[i]] = set(codes[i:i+1])
    i +=1
for k in operators.keys():
    num1=list(num)
    operators[k] = operators[k] | set(num1[o:o+2])
    o += 2
del operators['Katel']
del operators['Fonex']
for i, k in operators.items():
     print(f'{i} - {k}')