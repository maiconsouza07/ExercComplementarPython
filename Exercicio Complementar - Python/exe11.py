# Verificar se uma string é palíndrome:

def eh_palindrome(s):
    return s == s[::-1]
print(eh_palindrome("radar"))
