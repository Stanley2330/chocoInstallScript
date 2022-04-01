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

def update_dir_file(dir, oldStr, newStr):
    fileData = ""

    file = copylibDir + "/" + dir +"/tools/chocolateyinstall.ps1"
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if oldStr in line:
                line = line.replace(oldStr, newStr)
            fileData += line
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(fileData)

def update_url_to_filePath(dir):
    fileData = ""

    file = copylibDir + "/" + dir +"/tools/chocolateyinstall.ps1"
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if 'http' in line:
                URL = line[line.find('\''):line.rfind('\'')+1]
                fileName = line[line.rfind('/')+1:line.rfind('\'')]
                fileName = fileName.replace('%20', '_')
                line = line.replace(URL, "\""+copylibDir + "/" + dir + "/tools/" + fileName+"\"")           
            fileData += line
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(fileData)
    
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

def copy_dir():
    global copylibDir
    currentDir = str(pathlib.Path().resolve())
    copylibDir = currentDir + "_copylib"
    
    try:
        if os.path.isdir(copylibDir):
            shutil.rmtree(copylibDir)
        shutil.copytree(path, copylibDir)
    except OSError as e:
        print(e)

# # 複製 programData 到 當前目錄
copy_dir()

# 列出下載的全部資料夾
dirs = list_dir()

#下載資料夾內ps1的url
for dir in dirs:
    try:
        print(dir + " exec start")
        download_dir_file(dir)
    
        update_dir_file(dir, "url", "file")
        update_url_to_filePath(dir)
        print(dir + " exec end")
    except:
        print("###" + dir + " exec fail###")

    print("=========")

