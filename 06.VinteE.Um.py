from random import randrange, seed
seed()

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!''')

pontos = 0
jogando = True

while jogando == True:
 numero = randrange(10)
 pontos = numero + pontos
 print("\nSeu proximo número é", numero)
 print("Sua pontuação agora é", pontos)

 print("\nGostaria de somar mais um número (s/n)")
 resposta = input().lower()
 if resposta == "n" or resposta == "nao":
  jogando = False
  print("Sua pontuação final é", pontos)

if pontos == 21:
 print("Parabéns. VOCÊ VENCEU!!")
elif pontos > 21:
 print("Que pena!!")

