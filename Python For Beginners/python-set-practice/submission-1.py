from typing import List

def contains_duplicate(words: List[str]) -> bool:
    k=len(words) # list
    s=set(words)
    d=len(s) #set
    if k>d:
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
