# Utan lista
# summa = 0
# for _ in range(10):
#     tal = int(input('Skriv in en heltal: '))
#     summa = summa + tal 

# print(summa)

# Med lista

lista_med_tal = []

for _ in range(10):
    lista_med_tal.append(int(input('Skriv in tal: ')))

print('Summan av talen:', end="")
for i in lista_med_tal:
    print(i, end=' ')

print('=', sum(lista_med_tal))