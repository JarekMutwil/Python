import random

tablica = [] 

for _ in range(10):
  liczba_losowa = random.randint(1, 100)
  tablica.append(liczba_losowa)

print("Tablica:", tablica)
 
dolnaGranica = 0
gornaGranica = len(tablica) - 1

while True:
    pozycjaZmianyElementow = -1
    
    for i in range (dolnaGranica, gornaGranica):
        if (tablica[i] > tablica[i+1]):
            tablica[i], tablica[i+1] = tablica[i+1], tablica[i]
            if (pozycjaZmianyElementow < 0):
                dolnaGranica = i
            pozycjaZmianyElementow = i
      
    if (dolnaGranica):
      dolnaGranica -= 1
    gornaGranica = pozycjaZmianyElementow
        
    if pozycjaZmianyElementow < 0:
        break
    
print("Tablica 2:", tablica)