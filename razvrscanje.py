import locale

#Rabimo zaradi sortiranja sumnikov
#Ker sumnike tretiral kot osnovno obliko crke č => c š => s
locale.setlocale(locale.LC_COLLATE, "sl_SI.UTF-8")

def preberiTXT(datoteka):
    polje = []

    with open(datoteka, "r", encoding="utf-8") as dat:
        for vrstica in dat:
            vrstica = vrstica.strip() 
            podatek = vrstica.split('_')
            if len(podatek) == 4:
                oseba = {
                "imePriimek": podatek[0],
                "ulica": podatek[1],
                "telefonska": podatek[2],
                "email": podatek[3]
                }

                polje.append(oseba)
    
    return polje

def pisanjeSortiranihPodatkov(polje, argument = "a"):
    with open("sortiraniPodatki.txt", argument, encoding="utf-8") as dat:
        for oseba in polje:
            niz = f"{oseba['imePriimek']}_{oseba['ulica']}_{oseba['telefonska']}_{oseba['email']}\n"
            dat.write(niz)

def razvrscanjeIme(polje, DESC):
    polje.sort(reverse = DESC, key=lambda o: locale.strxfrm(o["imePriimek"]))

    #oblika ce bi sori brez sumnikov
    # polje.sort(key=lambda o: o["imePriimek"])
    #Lamba - Za vsako osebo o vzemi o["imePriimek"] in po tem razvrsti.

def razvrscanjeUlice(polje, DESC):
    polje.sort(reverse = DESC, key=lambda o: locale.strxfrm(o["ulica"]))

def razvrscanjeTelefonska(polje, DESC):
    polje.sort(reverse = DESC, key=lambda o: o["telefonska"])

def razvrscanjeEmail(polje, DESC):
    polje.sort(reverse = DESC, key=lambda o: locale.strxfrm(o["email"]))