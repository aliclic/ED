# Um material radioativo denominado invictus, quando em contato com o oxigênio, perde metade de sua
# massa a cada 50 segundos. Faça um função recursiva que receba uma quantidade de massa do invictus,
# em gramas, e exiba o tempo (em segundos) necessário para que sua massa se torne menor que 0,8 g. A
# função também deve retornar o o valor da massa final.

def meiaVidaInvictus( massa ):
  if massa < 0.8:
    return 0
  return 50 + meiaVidaInvictus(massa / 2)

'''
massa            return
5.0              50 + meiaVidaInvictus(2.5)   => 50 + 100 = 150
2.5              50 + meiaVidaInvictus(1.25)  => 50 + 50 =  100 ^
1.25             50 + meiaVidaInvictus(0.625) => 50 + 0 =   50  ^
0,625            0 => 0 ^
'''

print(meiaVidaInvictus(5.0))