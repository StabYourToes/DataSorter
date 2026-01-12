import program as val
import os
import razvrscanje as raz

def pridobi_txt(pot):
    txt_datoteke = []
    for element in os.listdir(pot):
        polna_pot = os.path.join(pot, element)
        if os.path.isdir(polna_pot):
            txt_datoteke.extend(pridobi_txt(polna_pot))
        elif element.endswith(".txt") and os.path.isfile(polna_pot):
            txt_datoteke.append(polna_pot)
    
    return txt_datoteke

def branjeTXT(datoteka):
    with open(datoteka, "r", encoding="utf-8") as dat:
        vsebina = dat.read()
    return vsebina

def pisanjePodatkov(polje, argument = "a"):
    with open("osebe.txt", argument, encoding="utf-8") as dat:
        for oseba in polje:
            niz = f"{oseba['id']}_{oseba['imePriimek']}_{oseba['ulica']}_{oseba['telefonska']}_{oseba['email']}\n"
            dat.write(niz)

def locenjePodatkov(vsebina):
    segments = vsebina.split('|')
    veljavneOsebe = []
    id = 0
    
    for segment in segments:
        informacije = segment.split('_')
        if len(informacije) < 3:
            continue
        
        imePriimek = informacije[0]
        ulica = informacije[1]
        telefosnka = informacije[2]
        email = informacije[3]
        
        if (len(val.validiraj_ime(imePriimek)) != 0 
            and len(val.validiraj_naslov(ulica)) != 0 
            and val.validiraj_telefonsko(telefosnka) != "False"
            and val.validiraj_email(email) != "False"):
            
            id += 1
            oseba = {
                "id": id,
                "imePriimek": imePriimek,
                "ulica": ulica,
                "telefonska": telefosnka,
                "email": email
            }
            veljavneOsebe.append(oseba)
    
    return veljavneOsebe



if __name__ == "__main__":
    mapa = "D:/Faks/data"
    datoteke = pridobi_txt(mapa)
 
    print("Seminarksa naloga - 2. del")
    print("Iskanje tekstovnih datotek...")
    print("Ločevanje podatkov...")
    #Izprazni datoteko osebe.txt
    polje = []
    pisanjePodatkov(polje,"w")

    for i in range(len(datoteke)):
        vsebina = branjeTXT(datoteke[i])
        polje = locenjePodatkov(vsebina)
        pisanjePodatkov(polje, "a")
    
    while True:
        print("Ločevanje končano! Podatki so zapisani v tekstovni datoteki osebe.txt!")
        print("Razvrščevanje po:")
        print("     1. Imenu in priimku")
        print("     2. Ulici")
        print("     3. Telefonski številki")
        print("     4. Email naslovu")
        print("     5. Končaj z programom")
        izibira = int(input("Po katere podatku želite razvrstiti podatke(vpišite številko): "))
        if izibira == 5:
            break
        DESC = bool(int(input("Želite da so podatki razvrščeni naraščajoče ali padajoce(1-padajoče/0-naraščajoče): ")))

        poljeSort = []
        match izibira:
            case 1:
                poljeSort = raz.preberiTXT("osebe.txt")
                raz.razvrscanjeIme(poljeSort, DESC)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 2:
                poljeSort = raz.preberiTXT("osebe.txt")
                raz.razvrscanjeUlice(poljeSort, DESC)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 3:
                poljeSort = raz.preberiTXT("osebe.txt")
                raz.razvrscanjeTelefonska(poljeSort, DESC)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 4:
                poljeSort = raz.preberiTXT("osebe.txt")
                raz.razvrscanjeEmail(poljeSort, DESC)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 5:
                break
            case _:
                print("Niste vnesli pravilno številko")
        
        print("Sortirani podatki so shranjeni v teskovni datoteki sortiraniPodatki.txt")




