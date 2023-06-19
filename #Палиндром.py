#Палиндром

def Palindrome(word):
    word = word.replace(' ','').lower()
    return True if word == word[::-1] else False

print(Palindrome(input()))