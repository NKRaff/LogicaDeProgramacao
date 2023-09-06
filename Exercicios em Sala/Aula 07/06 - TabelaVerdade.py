import os
os.system('cls')

p = True; q = True
print(f"P = {p},  Q = {q}  = {(p and q) and not (p or q)} | {not(p and not q) or q}")
p = True; q = False
print(f"P = {p},  Q = {q} = {(p and q) and not (p or q)} | {not(p and not q) or q}")
p = False; q = True
print(f"P = {p}, Q = {q}  = {(p and q) and not (p or q)} | {not(p and not q) or q}")
p = False; q = False
print(f"P = {p}, Q = {q} = {(p and q) and not (p or q)} | {not(p and not q) or q}")
