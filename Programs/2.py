fobj=open('file1.txt','r')
c=0
for var in fobj:
    c+=len(var.split())
print(c)
