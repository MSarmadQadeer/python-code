import time
import sys


def slow(some_string):
    for letter in some_string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


print('\n')
slow("WELCOME to OPEN SOURCE World!")
print('\n')
