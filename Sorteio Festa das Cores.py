import random

cores = []
nomes = []

print("Sorteio Festa das Cores V1.1")
print('''
#Só será sorteado a quantidade de cores digitadas.
#Se houver mais nomes do que cores será sorteado aleatóriamente dois nomes para uma cor.
#Se tiver mais cores do que nomes só será exibido a quantidade de nomes.
''')

print("Quais serão as cores?(Digite 'Continuar' após inserir as cores)")
while True:
  cor = input()
  if cor.upper() == "CONTINUAR":
    break
  cores.append(cor)
  print("Cores =", cores)
print()

print("Quais os nomes?(Digite 'Continuar' após inserir os nomes)")
while True:
  nome = input()
  if nome.upper() == "CONTINUAR":
    break
  nomes.append(nome)
  print("Nomes =", nomes)

print(f'''
Temos {len(cores)} Cores e {len(nomes)} Nomes

Hora do Sorteio
''')

while len(nomes) > len(cores):
  random.shuffle(nomes)
  random.shuffle(cores)
  print('-' * 20)
  print(nomes.pop(0), "e", nomes.pop(1))
  print("Cor =", cores.pop(0))
  print('-' * 20)

for i in range (len(cores)):
  if nomes == []:
    break
  random.shuffle(nomes)
  random.shuffle(cores)
  print('-' * 20)
  print(nomes.pop(0))
  print("Cor =", cores.pop(0))
  print('-' * 20)
