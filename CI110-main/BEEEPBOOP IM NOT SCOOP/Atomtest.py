import time
import random

s = time.time()
for i in range(5):
    time.sleep(1)
    print(i)
a = time.time()
b = a - s
print(b)