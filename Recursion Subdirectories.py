import os, shutil
from configobj import ConfigObj
'''Using recursion to iterate through all subdirectories and transfer it to the main directory.'''
config=ConfigObj('config.ini')
srcpath = config["srcpath"]
types_of_files = config["types_of_files"]

#ensure that the srcpath always stays constant, so its passed on to the next function varibales
def transfer(srcpath, cwd):
    file_dir = os.listdir(cwd)
    for fileName in file_dir:
        if os.path.isdir(os.path.join(cwd,fileName)):
            transfer(srcpath, os.path.join(cwd,fileName))
        else:
            for mytype in types_of_files:
                if fileName.endswith(mytype)and cwd != srcpath:
                    print ("Moving "+ fileName)
                    shutil.move(os.path.join(cwd,fileName), srcpath)
            

transfer(srcpath, srcpath)
