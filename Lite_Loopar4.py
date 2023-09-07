# while True:
#     tal1 = int(input("Mata in ett tal: "))
#     tal2 = int(input("Mat in ett till tal: "))

#     summan = tal1 + tal2
#     print(summan)
#     forstätta = input("Vill du fortsätta? (j/n)?: ").lower()

#     if forstätta == "j":
#         continue
#     else:
#         break
#------------------------------------------------------------
# 4. LOOP #4

# Be användaren mata in ett tal. Spara värdet i en variabel. 
# Upprepa detta 10 gånger. För varje gång lägg till det inmatade
# värdet till variabelns värde. När det är klart skriv ut-
# Summan av det du matat in är: summan.

# summa = 0

# for _ in range(10):
#     tal = int(input())
#     summa += tal
# print(summa)

#------------------------------------------------------------------
# 2. LOOP #2

# Skapa ett program där användaren får mata in två tal. 
# Låt sedan programmet skriva ut alla tal som finns mellan dessa två tal på skärmen. 
# Lös detta med en for-loop. Lös den igen med en While-loop

# tal1 = int(input('Skriv in ett heltal: '))
# tal2 = int(input('Skriv in ett till heltal: '))

# tal1 > tal2 ---->  tal1+1 , tal1+2,..., tal2-1
# exempel tal1 = 10, tal2 = 5 ---> 6,7,8,9
# if tal1 > tal2:
#     # range -> range(1, 10 - 5) == range(1,5) --> 1,2,3,4
#     for step in range(tal2+1,tal1):
#         print(step)
#     for neg in range(tal1-1,tal2, -1):
#         print(neg)

for i in range(1000,0, -10):
    print(i)


