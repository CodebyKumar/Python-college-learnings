from pathlib import Path
helloFile=open('C:\\Users\\Admin\\Desktop\\1SI23CI019\\KLab6\\hello.txt')
#Reading file
hellocontent=helloFile.read()
print(hellocontent)
#Writing file
baconFile=open('bacon.txt','w')
print(baconFile.write('Hello, World!\n'))
baconFile.close()
baconFile=open('bacon.txt','a')
print(baconFile.write('Bacon is not a vegetable.\n'))
baconFile.close()
baconFile=open('bacon.txt')
content=baconFile.read()
baconFile.close()
print(content)
