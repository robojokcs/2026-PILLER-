# Tranzakciók beolvasása a fájlból
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok
            tranzakciok = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


# Tranzakciók mentése a fájlba
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            for i in range(len(tranzakciok)):
                f.write(f"{tranzakciok[i].rstrip()}\n")
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


# Számla egyenlegének kiszámítása
def egyenleg():
    szamla_egyenleg = 0
    
    for sz in tranzakciok:
        szamla_egyenleg += int(sz)
    
    print(f"\nAz egyenleged: {szamla_egyenleg} Ft")
    
    return szamla_egyenleg


# Pénz kivétele vagy átutalása
def utalas(osszeg):
    print("Utalás: ")
    
    osszeg += round(hasznalati_dij * 0.05)
    
    if osszeg > egyenleg():
        print("\nNem áll rendelkezésre a megfelelő összeg!")
    else:        
        tranzakciok.append(f"-{osszeg}")
    
    egyenleg()


# Pénz befizetése a számlára
def penzbetet(osszeg):
    print("Betét: ")
    tranzakciok.append(f"+{osszeg}")
    
    egyenleg()


# Tranzakciók történetének megjelenítése
def tortenet(darab):
    print("Tranzakciók: ")
    
    if darab == 0:
        kezdet = 0
    else:
        kezdet = len(tranzakciok)-darab
    
    for i in range(kezdet, len(tranzakciok)):
        print(f"\t{tranzakciok[i].rstrip()}")


# Összes költés kiszámítása
def koltes_osszeg():
    osszeg = 0
    
    for sz in tranzakciok:        
        if int(sz) < 0:
            osszeg += int(sz)
    
    return osszeg


# Összes befizetés kiszámítása
def betet_osszeg():
    osszeg = 0
    
    for sz in tranzakciok:        
        if int(sz) > 0:
            osszeg += int(sz)
    
    return osszeg   


# Legnagyobb kiadás megkeresése
def legnagyobb_kiadas():
    min_ertek = 0
    
    for sz in tranzakciok:
        if int(sz) < min_ertek:
            min_ertek = int(sz)
            
    return min_ertek
    






