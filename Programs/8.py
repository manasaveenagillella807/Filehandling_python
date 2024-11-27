fobj=open('file1.txt','r')
c=0
for line in fobj:
    i=line.strip('\n')
    for ch in i:
        if not 'A'<=ch<='z':
            c+=1
print(c)
