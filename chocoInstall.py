import os
import requests as req
import shutil
import pathlib

path = "C:/ProgramData/chocolatey/lib"

def list_dir():
    dirs = os.listdir(path)
    ignoreFileList = ['chocolatey', 'chocolatey-core.extension', 'git', 'git.install']

    for item in ignoreFileList:
        dirs.remove(item)
    
    return dirs

def download_dir_file(dir):
    f = open(path + "/" + dir +"/tools/chocolateyinstall.ps1", "r")
    lines = f.readlines()
    
    for line in lines:
        URL = ''
        if 'http' in line:
            fileName = line[line.rfind('/')+1:line.rfind('\'')]
      
            URL = line[line.find('\'')+1:line.rfind('\'')]
            file = req.get(URL,  allow_redirects=True)

            #replace %20 to _
            fileName = fileName.replace('%20', '_')
            open(copylibDir + "/" + dir + "/tools/" + fileName, 'wb'). write(file.content)
            
    f.close

def copyDir():
    global copylibDir
    currentDir = str(pathlib.Path().resolve())
    copylibDir = currentDir + "_copylib"

    shutil.copytree(path, copylibDir)

copyDir()

dirs = list_dir()

for dir in dirs:
    download_dir_file(dir)

download_dir_file('lens')