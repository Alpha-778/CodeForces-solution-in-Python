def fix_caps(word):
    if len(word)==1:
        if word==word.lower():
            return word.upper()
        else:
            return word.lower()
    if word.isupper() or (word[1:].isupper() and word[0].islower()):
        return word.swapcase()
    return word
print(fix_caps(input().strip()))