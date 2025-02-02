#creating zipfile
from zipfile import ZipFile
file='spam.txt'
f=ZipFile('spam.zip','w')
f.write(file)
f.close()
