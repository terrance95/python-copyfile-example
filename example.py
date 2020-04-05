import shutil, os
from pathlib import Path

currentDirectory = os.getcwd()
oldFolder = os.path.join(currentDirectory, "old")
fileList = os.listdir(oldFolder)

newFolder = os.path.join(currentDirectory + "/new")
shutil.copytree(oldFolder, newFolder)
