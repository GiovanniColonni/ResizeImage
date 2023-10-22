import time
import logging  

logging.basicConfig()
logging.root.setLevel(logging.INFO)


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"{func.__name__} took {execution_time:.2f} seconds to execute.")
        return result
    return wrapper