import os
from random import randint

TARGET_SIZE = (512,512)
QUALITY = 95

NAMES = [sample for sample in os.listdir("./examples/base") if sample.endswith(".png")] 

PATH_BASE = "./examples/base"
PATH_INVALID = "./examples/invalid"
PATH_OUTPUT = "./examples/output"

def get_random_sample():
    return NAMES[randint(0,len(NAMES)-1)]