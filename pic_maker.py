#! /usr/bin/python3

import math, random

with open('pic.ppm', 'w') as f:
    f.write('P3\n551 551\n255\n')
    r = g = b = 0
    i = 0
    while i < 250000:
        f.write('{} {} {} '.format(r,g,b))
        if i % 3 == 0:
            r+=math.sqrt(i) * i * random.randint(1,255)
            r%=255
        if i % 3 == 1:
            g+=math.sqrt(i) * i * random.randint(1,255)
            g%=255
        if i % 3 == 2:
            b +=math.sqrt(i) * i * random.randint(1,255)
            b%=255
        i+=1
