# Prime Sieve (C)

## Aim
To find and print all prime numbers up to a given number N in C. The program should use an efficient method, the Sieve of Eratosthenes.

## Prerequisites
- GCC (or any C compiler) installed
- Arrays and pointers
- Dynamic memory (`calloc`, `free`)
- Nested loops
- Command-line arguments (`argc`, `argv`)

## Procedure
An array marks every number as prime at first. For each unmarked `i` up to √N, its multiples starting from `i*i` are marked as composite, and the unmarked numbers are printed.

## Build & run
```bash
gcc -Wall -O2 -o sieve sieve.c
./sieve         # primes up to 100
./sieve 500     # primes up to 500
```
On Windows (MinGW): `gcc -o sieve.exe sieve.c` then `sieve.exe 500`.

## Conclusion
The sieve finds primes much faster than checking each number one by one. It shows how a simple array and nested loops can solve a mathematical problem efficiently. Proper memory handling (`free`) keeps the program clean and safe.
