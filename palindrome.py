
def palindrome():
    word = input()
    if word == word[::-1]:
        print('True')
        return True
    else:
        print('False')
        return False
