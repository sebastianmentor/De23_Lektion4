# Utan lista
# summa = 0
# for _ in range(10):
#     tal = int(input('Skriv in en heltal: '))
#     summa = summa + tal 

# print(summa)

# Med lista

# lista_med_tal = []

# for _ in range(10):
#     lista_med_tal.append(int(input('Skriv in tal: ')))

# print('Summan av talen:', end="")
# for i in lista_med_tal:
#     print(i, end=' ')

# print('=', sum(lista_med_tal))

pengar = int(input('Skriv hur mycket pengar du har!'))
har_rabbat = input('Har du rabbat? (j/n)')

if (15<= pengar <= 25) and har_rabbat == 'n':
    print('liten burgare')
elif 15<= pengar and pengar <= 25 and har_rabbat == 'j':
    print('Du kan köpa en liten hamburgare och en pommes frites')
...