import program
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
    with open(datoteka, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def pisanjePodatkov(podatki):
    with open("osebe.txt", "w", encoding="utf-8") as file:
        file.write(podatki)

def locenjePodatkov(vsebina):
    segments = vsebina.split('|')
    veljavneOsebe = []
    oseba = {
        "id": 0,
        "imePriimek": "",
        "ulica": "",
        "telefosnka": 0,
        "email": ""
    }
    id = 0

    for segment in segments:
        informacije = segment.split('_')
        if len(informacije) < 3:
            continue
        else:
            imePriimek = informacije[0]
            ulica = informacije[1]
            telefosnka = informacije[2]
            email = informacije[3]
            
            if len(program.validiraj_ime(imePriimek)) != 0 \
                and len(program.validiraj_naslov(ulica)) != 0 \
                and program.validiraj_telefonsko(telefosnka) \
                and program.validiraj_email(email):

                id += 1
                oseba["id"] = id
                oseba["imePriimek"] = imePriimek
                oseba["ulica"] = ulica
                oseba["telefosnka"] = telefosnka
                oseba["email"] = email
                veljavneOsebe.append(oseba)

    return veljavneOsebe



if __name__ == "__main__":
    pot = "D:/Faks/data"
    datoteke = pridobi_txt(pot)
    st = len(datoteke)
    print(st)
    vsebina = branjeTXT(datoteke[0])

    """
    a = program.validiraj_ime("W#4IIžhFu//gY17P7ž")
    print(a)
    b = program.validiraj_naslov("Majde Vrhovnikove ulica 1a8521 Šoštanj")
    print(b)
    c = program.validiraj_telefonsko("sdfsdfeewfwef")
    print(c)
    d = program.validiraj_email("asdasdasdasd")
    print(d)
    """

    array = locenjePodatkov(vsebina)
    #print(array)
    ste = len(array)
    print(ste)