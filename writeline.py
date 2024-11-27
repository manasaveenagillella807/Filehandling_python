f=open('file2.txt','w')
d="this is the content of pythonfile 2 \n his is the content"
print(f.writelines(d))
f.close()
