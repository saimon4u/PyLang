import os
import sys


currentDirectory = os.getcwd()
filename = currentDirectory + '/' + sys.argv[1]

projectDirectory = "/home/saimon/PycharmProjects/PyLang/Main"

os.chdir(projectDirectory)
os.system("python3  main.py " + filename)