import random
import os
import pathlib

nmus = []

for k in range(50):
    nmus.append((random.randint(1,20), random.randint(1,2000), random.randint(1,2000)))

for k in range(50):
    nmus.append((random.randint(20,40), random.randint(2000,4000), random.randint(2000,4000)))

for k in range(50):
    nmus.append((random.randint(40,60), random.randint(4000,6000), random.randint(4000,6000)))

for k in range(50):
    nmus.append((random.randint(60,80), random.randint(6000,8000), random.randint(6000,8000)))

for k in range(50):
    nmus.append((random.randint(80,100), random.randint(8000,10000), random.randint(8000,10000)))

with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "input_params.txt"), "w") as f:
    for i in nmus:
        f.write(f"{i[0]} {i[1]} {i[2]}\n")
