import os

path = "C:/ProgramData/chocolatey/lib"
dirs = os.listdir(path)
ignoreFileList = ['chocolatey', 'chocolatey-core.extension', 'git', 'git.install']

for item in ignoreFileList:
    dirs.remove(item)
    
print(dirs)