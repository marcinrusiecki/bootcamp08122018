import time
def czas_wykonania(dekorowana_funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        dekorowana_funkcja(*args, **kwargs)
        stop = time.time()
        print(f'Czas wykonania {dekorowana_funkcja__name__} wynosi {stop-start}')
     return wrapper

