# Faça uma função recursiva chamada ispalindrome() que retorne verdadeiro caso uma string seja palíndrome, ou falso caso contrário.

def isPalindrome(str)->bool:
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return isPalindrome(str[1:-1])

'''
str              return
'reviver'        isPalindrome('reviver'[1:-1])
'evive'          isPalindrome('evive'[1:-1])
'viv'            isPalindrome('viv'[1:-1])
'i'              True
'''

print(isPalindrome('reviver'))