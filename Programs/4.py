fobj=open('file1.txt','r')
c=0
for line in fobj:
    l=line.strip('\n')
    for ch in l:
        if l in '0123456789':
            c+=1
print(c)
