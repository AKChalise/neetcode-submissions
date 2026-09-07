from typing import List

def read_integers() -> List[int]:
    s=(input())
    d=s.split(",")
    k=[]
    for i in d:
        k.append(int(i))
    return k

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
