# Stwórz funkcję, która przyjmuje listę dużych plików tekstowych, a następnie korzystając z
# `multiprocessing`, równolegle analizuje każdy plik, oblicza liczbę słów i zwraca sumę słów ze
# wszystkich plików.

import multiprocessing as mp
from multiprocessing.synchronize import Lock
import os
import time

lock: Lock = mp.Lock()

def analyze_text(file_path: str) -> int:
    time.sleep(0.5)
    with lock:
        print(file_path, str(os.getpid()))
    with open(file_path, 'r') as file:
        text: str = file.read()
        total_words: int = len(text.split())
    return total_words

if __name__ == '__main__':
    
    with mp.Pool() as pool:
        results: list[int] = pool.map(analyze_text, ['text_1.txt', 'text_2.txt', 'text_3.txt', 'text_4.txt'])
        # the with block would eventually call pool.terminate() if any exception occurs, but since we want to be sure our workers complete tasks we explicitly call close() and join()
        pool.close()
        pool.join()

    print(results)
    print('Sum of words: ', sum(results))