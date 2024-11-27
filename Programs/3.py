fobj=open('file1.txt','r')
c=0
for line in fobj:
    l=line.strip()
    c+=len(l)
print(c)
