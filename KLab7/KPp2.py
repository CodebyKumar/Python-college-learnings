#extracting from zipfile
import os
from zipfile import ZipFile
f=ZipFile('spam.zip','r')
f.extractall()
f.close()
print('Done')
