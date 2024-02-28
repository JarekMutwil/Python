import random

#Inicjalizacja pustej tablicy
tablica = [] 

# Wypełnienie tablicy liczbami losowymi
for _ in range(10):
    liczba_losowa = random.randint(1, 100)  # Generuje liczbę losową z zakresu 1-100
    tablica.append(liczba_losowa)
    
print("Tablica:", tablica)

for i in range(len(tablica)-1, 0, -1):
    czyPosortowane = True
    for j in range (0, i):
        if (tablica[j] > tablica[j+1]):
            tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
            czyPosortowane = False
            
    if (czyPosortowane == True):
        break
    
print("Tablica:", tablica)