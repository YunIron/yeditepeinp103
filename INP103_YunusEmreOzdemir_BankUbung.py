kontoStand=1000
while True:
    name=input("Was ist dein Name?: ")
    passwort=input("Was ist dein Passwort?: ")
    if name=="deneme" and passwort=="123":
        print("Angemeldet!")
        break
    else:
        print("Der Name oder das Passwort ist falsch")
        continue

while True:
    print(f"Kontostand : {kontoStand}")
    choice=int(input("[1]Einzahlen\n[2]Auszahlen\n[3]Verlassen\n   :  "))
    if 0<choice<4:
        if choice==1:
            while True:
                menge=int(input("Wie viel mochten Sie einzahlen?: "))
                if type(menge)==int and menge>0:
                    kontoStand+=menge
                    print(f"{menge} ist eingezahlt.")
                    break
                else:
                    print("Schreiben Sie in richtige Form")
                    continue
        if choice==2:
            while True:
                menge=int(input("Wie viel mochten Sie auszahlen?: "))
                if type(menge)==int and menge>0:
                    if kontoStand>=menge:
                        kontoStand-=menge
                        print(f"{menge} ist ausgezahlt.")
                        break
                    else:
                        print("Es ist nicht genug.")
                        continue
                else:
                    print("Schreiben Sie in richtige Form")
                    continue
        if choice==3:
            print("Verlassen...")
            break
    else:
        print("Schreiben Sie in richtige Form")
        continue