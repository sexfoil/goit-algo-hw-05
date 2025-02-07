import timeit

def boyer_moore(text: str, pattern: str):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    bad_char = {char: m for char in set(pattern)}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += bad_char.get(text[i + m - 1], m)
    return -1


def knuth_morris_pratt(text: str, pattern: str):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    lps = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def rabin_karp(text: str, pattern: str, prime: int = 101):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    
    base = 256
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    for i in range(m - 1):
        h = (h * base) % prime
    
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return -1

def read_text_from_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def measure_time(algorithm, text: str, pattern: str):
    return algorithm.__name__, timeit.timeit(lambda: algorithm(text, pattern), number=10)

def compare_algorithms(filename: str, pattern: str):
    text = read_text_from_file(filename)
    results = [
        measure_time(boyer_moore, text, pattern),
        measure_time(knuth_morris_pratt, text, pattern),
        measure_time(rabin_karp, text, pattern)
    ]
    
    for name, exec_time in results:
        print(f"{name}: {exec_time:.6f} seconds")

print("\nСтаття 1: пошук існуючого рядка")
compare_algorithms('text1.txt', 'стандартна бібліотека')
print("\nСтаття 2: пошук існуючого рядка")
compare_algorithms('text2.txt', 'непогані результати')

print("\nСтаття 1: пошук неіснуючого рядка")
compare_algorithms('text1.txt', 'немає такого рядку в тексті')
print("\nСтаття 2: пошук неіснуючого рядка")
compare_algorithms('text2.txt', 'немає такого рядку в тексті')
