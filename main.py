import validacija as val
import razvrscanje as raz
import os


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
            niz = f"{oseba['ime']} {oseba['priimek']}_{oseba['ulica']} {oseba['hisnaSt']} {oseba['postnaSt']} {oseba['posta']}_{oseba['telefonska']}_{oseba['email']}\n"
            dat.write(niz)

def locenjePodatkov(vsebina):
    segments = vsebina.split('|')
    veljavneOsebe = []

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

            imePriimek_arr = val.validiraj_ime(imePriimek)
            naslov_arr = val.validiraj_naslov(ulica)
            

            oseba = {
                "ime": imePriimek_arr[0],
                "priimek": imePriimek_arr[1],
                "ulica": naslov_arr[0],
                "hisnaSt": naslov_arr[1],
                "postnaSt": naslov_arr[2],
                "posta": naslov_arr[3],
                "telefonska": telefosnka,
                "email": email 
            }
            veljavneOsebe.append(oseba)
    
    return veljavneOsebe



if __name__ == "__main__":
    mapa = "D:/Faks/data"
    datoteke = pridobi_txt(mapa)
 
    print("Seminarksa naloga - 2. del")

    vseOsebe = []
    for datoteka in datoteke:
        vsebina = branjeTXT(datoteka)
        osebe = locenjePodatkov(vsebina)
        vseOsebe.extend(osebe)
    
    pisanjePodatkov(vseOsebe, "w")
    
    while True:
        print("Ločevanje končano! Podatki so zapisani v tekstovni datoteki osebe.txt!")
        print("Razvrščevanje po:")
        print("     1. Imenu")
        print("     2. Priimku")
        print("     3. Ulici")
        print("     4. Hišni številki")
        print("     5. Poštni številki")
        print("     6. Pošti") 
        print("     7. Telefonski številki")
        print("     8. Email naslovu")
        print("     0. Končaj z programom")
        izibira = int(input("Po katere podatku želite razvrstiti podatke(vpišite številko): "))

        poljeSort = vseOsebe
        match izibira:
            case 1:
                raz.mergeSort(poljeSort, "ime", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 2:
                raz.mergeSort(poljeSort, "priimek", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 3:
                raz.mergeSort(poljeSort, "ulica", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 4:
                raz.mergeSort(poljeSort, "hisnaSt", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 5:
                raz.mergeSort(poljeSort, "postnaSt", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 6:
                raz.mergeSort(poljeSort, "posta", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 7:
                raz.mergeSort(poljeSort, "telefonska", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 8:
                raz.mergeSort(poljeSort, "email", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 0:
                break
            case _:
                print("Niste vnesli pravilno številko")
        
        print("Sortirani podatki so shranjeni v teskovni datoteki sortiraniPodatki.txt")




