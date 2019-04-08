
fd="file.txt"
file=open(fd,'w')
file.write("mayank")
file.close()
file2=open(fd,'a')
file2.write("agrawal")
file2.close()
file3=open(fd,'r')
string=file3.read()
print(string)
