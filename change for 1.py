# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:25:44 2022

@author: tonyl
"""

counter = 0 
for h in range(0,3):
    for q in range(0,5):
        for d in range(0,11):
            for n in range(0,21):
                for p in range(0,101):
                    if 50*h + 25*q + 10*d + 5*n + p == 100:
                        print(f"{h}, {q}, {d}, {n}, {p}")
                        counter +=1 
    
print(f"number of ways is {counter}")

