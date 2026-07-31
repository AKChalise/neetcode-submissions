from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char_count={}
    for key in word:
        if key in char_count:
            char_count[key] +=1
        else:
            char_count[key]=1
    return char_count
    
    
   





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
