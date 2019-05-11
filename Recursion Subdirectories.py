import os, shutil
'''Using recursion to iterate through all subdirectories and transfer it to the main directory.'''

srcpath = r"D:\Anime\speed power test"

#ensure that the srcpath always stays constant, so its passed on to the next function varibales
def transfer(srcpath, cwd):
    file_dir = os.listdir(cwd)
    for fileName in file_dir:
        if os.path.isdir(os.path.join(cwd,fileName)):
            transfer(srcpath, os.path.join(cwd,fileName))
        elif (fileName.endswith('.mkv') or fileName.endswith('.mp4')) and cwd != srcpath:
            print ("Moving "+ fileName)
            shutil.move(os.path.join(cwd,fileName), srcpath)

transfer(srcpath, srcpath)