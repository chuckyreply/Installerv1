import os
import sys
import time
import termcolor 
from termcolor import colored
print(colored("Sedang Menginstall Bahan","white",attrs=["bold"]))
time.sleep(2)
os.system("pkg update && pkg upgrade")
os.system("pkg install python")
os.system("pkg install python2")
os.system("pkg install curl")
os.system("pkg install php")
os.system("pkg install bash")
os.system("pkg install sh")
os.system("pkg install git")
os.system("clear")
print (colored("menginstall bahan selesai","white",attrs=["bold"]))
time.sleep(2)
os.system("python installer.py")
