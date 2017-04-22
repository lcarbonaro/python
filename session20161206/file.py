import os

dirPath = "testFiles"

fileName = os.path.join(dirPath,'testfile.txt')

fileHandle = open(fileName, 'a')  #r(ead) or w(rite) or a(ppend)

fileHandle.write("hello world")

fileHandle.write("\n a new line here")

fileHandle.close()

fh = open(fileName, 'r')
#print(fh.read())

print(fh.readline())

fh.close()

# look up with open()