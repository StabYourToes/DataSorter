import validacija as val
import razvrscanje as raz
import os
import copy

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

def locenjePodatkov(vsebina, unikatneOsebe):
    segments = vsebina.split('|')
    veljavneOsebe = []

    for segment in segments:
        informacije = segment.split('_')
        if len(informacije) < 4:
            continue
        
        imePriimek = informacije[0]
        naslov = informacije[1]
        telefosnka = informacije[2]
        email = informacije[3]
        
        if len(val.validiraj_ime(imePriimek)) == 0:
            continue
        if len(val.validiraj_naslov(naslov)) == 0:
            continue
        if val.validiraj_email(email) == "False":
            continue
        if val.validiraj_telefonsko(telefosnka) == "False":
            continue

        imePriimek_arr = val.validiraj_ime(imePriimek)
        naslov_arr = val.validiraj_naslov(naslov)
            
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

        identitetaOsebe = (
            oseba["ime"], oseba["priimek"], oseba["ulica"],
            oseba["hisnaSt"], oseba["postnaSt"], oseba["posta"],
            oseba["telefonska"], oseba["email"]    
        )

        if identitetaOsebe in unikatneOsebe:
            continue
        else:
            unikatneOsebe.add(identitetaOsebe)
            veljavneOsebe.append(oseba)
    
    return veljavneOsebe



if __name__ == "__main__":
    mapeDjordje = ["D:/Faks/data", "D:/Faks/dataGen2"]
    mapeFilip = ["D:/Faks/Gracner/data","D:/Faks/Filip_data(2)/data", "D:/Faks/dataFilipNovo/dataFilipNovo"]
    unikatneOsebe = set()
    datoteke = pridobi_txt(mapeFilip[0])
    stDatotek = len(datoteke)
    print("Stevilo tekstovnih datotek:", stDatotek)

    vseOsebe = []
    for datoteka in datoteke:
        vsebina = branjeTXT(datoteka)
        osebe = locenjePodatkov(vsebina, unikatneOsebe)
        vseOsebe.extend(osebe)
    
    pisanjePodatkov(vseOsebe, "w")
    stOseb = len(vseOsebe)

    print("Ločevanje končano! Program je našel:", stOseb, "vseljavnih oseb. Podatki so zapisani v tekstovni datoteki osebe.txt!")

    print("Seminarksa naloga - 2. del")
    print("")
    while True:
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

        poljeSort = copy.deepcopy(vseOsebe)
        match izibira:
            case 1:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))
                raz.mergeSort(poljeSort, narascajoce, "ime", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 2:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))
                raz.mergeSort(poljeSort, narascajoce, "priimek", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 3:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))               
                raz.mergeSort(poljeSort, narascajoce, "ulica", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 4:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))                
                raz.mergeSort(poljeSort, narascajoce, "hisnaSt", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 5:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))                
                raz.mergeSort(poljeSort, narascajoce, "postnaSt", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 6:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))                
                raz.mergeSort(poljeSort, narascajoce, "posta", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 7:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))                
                raz.mergeSort(poljeSort, narascajoce, "telefonska", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 8:
                narascajoce = bool(int(input("Želite da so podatki sortirani naraščajoče ali padajoče(1/0): ")))                
                raz.mergeSort(poljeSort, narascajoce, "email", 0 , len(poljeSort) - 1)
                raz.pisanjeSortiranihPodatkov(poljeSort, "w")
            case 0:
                break
            case _:
                print("Niste vnesli pravilno številko")
        
        print("Sortirani podatki so shranjeni v teskovni datoteki sortiraniPodatki.txt")
        print("")




