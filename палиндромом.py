def polidrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(polidrome('сос'))
