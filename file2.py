user=input('write something')
fd='file1.txt'
file=open(fd,'w')
file.write(user)
file.close()
file=open(fd,'r')
text=file.read()
file.close()
fd1='file2.txt'
file=open(fd,'w')
file.write(user)
file.close()
file=open(fd,'r')
text1=file.read()
file.close()
print(text1)

