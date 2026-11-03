def remove_fourth_character(word: str) -> str:
    k=word[0:3]
    s=word[4:]
    d=k+s
    return d


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
