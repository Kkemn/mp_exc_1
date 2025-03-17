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
    
    # czy to potrzebne? Chyba pool automatycznie użyje tylu rdzeni ilu się da
    # processes is the number of worker processes to use. If processes is None then the number returned by os.process_cpu_count() is used.
    # Enter a number of text files to read
    # files_num: int = 4

    # Check cores available
    cores: int = mp.cpu_count()
    print('Cores: ', cores)

    # Set number of cores to be used
    # cor_num: int = files_num if cores > files_num else cores


    with mp.Pool() as pool:
        results: list[int] = pool.map(analyze_text, ['text_1.txt', 'text_2.txt', 'text_3.txt', 'text_4.txt'])

    print(results)
    print('Sum of words: ', sum(results))