''' Faça uma função recursiva chamada compareStr(char *str1, char *str2) que retorne:
0: str1 é igual a str2;
1: str1 é maior que str2;
-1: str1 é menor que str2; '''

def compareStr(str1, str2):
  if str1 == '' and str2 == '':
    return 0
  elif str1[0] == str2[0]:
    return compareStr(str1[1:], str2[1:])
  elif ( str1[0] > str2[0] ):
    return 1
  else:
    return -1

print(compareStr('ifpb', 'alic'))