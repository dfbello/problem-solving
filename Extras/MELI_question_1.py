### Codigo para la entrevista de MELI, problema:
### 	Minimizar el numero de bit-flips para hacer segura una password binaria.
### 	Una password segura se divide en substrings de igual tamaño donde cada subcadena esta conformada por ceros o unos, pero no ambos.

### 110011
import math

#Devuelve la secuencia mas larga de un caracter
def sec_count(s, char):
    max_count = 0
    current_count = 0

    for c in s:
        if c == char:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count


#Divide la palabra binaria en substrings de tamaño k
def divide(s, k):
    if len(s) % k != 0:
        return -1

    return [s[i:i+k] for i in range(0, len(s), k)]



# recibe la password s from STDIN
s = input()


uno, cero = sec_count(s, "1"), sec_count(s, "0")
max_sec = max(uno, cero)


substrings = divide(s, math.gcd(len(s),max_sec))




flips = 0 #	Number of bits flipped

for s in substrings:
    ones = s.count("1")
    zeroes = s.count("0")

    if ones > zeroes:
        flips += zeroes
    else:
        flips += ones

print(flips)

