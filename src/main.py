from logic import base
from sys import argv
from config import get_random_sample, PATH_OUTPUT, PATH_BASE

"""
Author: Giovanni Colonni
Date: 2021-09-01

Description: This is the main file of the project.
To run a random sample just type

    > python3 main.py

To run a specific sample just type the name without extension for PNG
 files or with extension for other files

    > python3 main.py <sample_name> 

"""

if __name__ == "__main__":
    name = get_random_sample()
    ext = ""

    if(len(argv) > 1):
        if("." in argv[1]):
            name = argv[1]
            ext = name.split(".")[1]
        else:
            name = f"{argv[1]}.png"
    
    path_in = f"{PATH_BASE}/{name}"
    path_out = f"{PATH_OUTPUT}/{name}"
    
    if(ext != ""):
        path_out = f"{PATH_OUTPUT}/{name.split('.')[0]}.png"
    
    base(path_in,path_out)

    exit(0)