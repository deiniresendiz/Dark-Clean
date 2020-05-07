import os
from methods import *

user = os.getlogin()
hiberFile = r'C:\hiberfil.sys'
tempDirectory = r'C:\Users\{}\AppData\Local\Temp'.format(user)


t = get_sizeFolder(tempDirectory)
h = get_sizeFile(hiberFile)

print(t)
print(convert_size(t))

print(h)
print(convert_size(h))