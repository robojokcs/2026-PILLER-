pin_kod =1234
egyenleg=0
hasz_dij=1000
adatfajl="szamla.txt"
jogosult=False
hibas_belepesszam=3

pk=int(input("add meg a pin kodódat"))


if pk==pin_kod:
    jogosult=True
    print("Sikeres bejelentkezés")

while(jogosult==False and hibas_belepesszam>0):
    print("Hibás pin kód, próbálkozz újra!")
    pk=int(input("Add meg a pin kodódat"))
    hibas_belepesszam-=1
    
    if pk==pin_kod:
        jogosult=True
        print("Sikeres bejelentkezés")

    






