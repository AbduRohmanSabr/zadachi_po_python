"""
Created on Thu Nov 11 18:38:33 2021

@author: Lenovo
"""
import time
stime = time.time()
for i in range(1,5000):
    print(i)
etime = time.time()
ttime = etime - stime
print("время",ttime)