from config import NAMES
from random import randint

def get_random_path():
    return f"./examples/base/{NAMES[randint(0,len(NAMES)-1)]}"

