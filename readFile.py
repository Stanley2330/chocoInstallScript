import urllib
import requests as req

f = open("C:\\ProgramData\\chocolatey\\lib\lens\\tools\\chocolateyinstall.ps1", "r")
lines = f.readlines()

for line in lines:
    URL = ''
    if 'http' in line:
        URL = line[line.find('\'')+1:line.rfind('\'')]
        file = req.get(URL,  allow_redirects=True)

        open('xxx.exe', 'wb'). write(file.content)

f.close
