while True:
    abschlussnote=int(input("Was ist ihre Abschluss Note?: "))
    if abschlussnote>100 or abschlussnote<0:
        print("Schreiben Sie Bitte in richtige Form")
        continue
    stufe=int(input("Was ist dein Programmiererfahrungen zwischen 1 und 5?: "))
    if stufe>5 or abschlussnote<1:
        print("Schreiben Sie Bitte in richtige Form")
        continue
    break

if abschlussnote>90:
    print("Sie sind eingestellt.")
else:
    if abschlussnote>=70 and stufe==5:
        print("Sie sind eingestellt.")
    else:
        if stufe==4 or abschlussnote>70:
            print("Wir laden Sie zum Gespraech ein. Kommen Sie bitte zum Gespraech.")
        else:
            print("Leider sind Sie abgelehnt.")