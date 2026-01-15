import re

email_rgx = re.compile(r"^[A-Za-z0-9._%&*+\-/=?^{|}~]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+){1,3}$")


def pisanjeSortiranihPodatkov(polje, argument):
    with open("sortiraniPodatki.txt", argument, encoding="utf-8") as dat:
        for oseba in polje:
            niz = f"{oseba['ime']} {oseba['priimek']}_{oseba['ulica']} {oseba['hisnaSt']} {oseba['postnaSt']} {oseba['posta']}_{oseba['telefonska']}_{oseba['email']}\n"
            dat.write(niz)

def validiraj_ime(ime_in_priimek):
    ime = ""
    priimek = ""
    index = 0
    
    ime_priimek_arr = []
    
    ime_in_priimek = ime_in_priimek.strip()
    ime_uppercase_counter = 0
    
    i = 0
    while i < len(ime_in_priimek):
        if ime_in_priimek[0].isupper() == False:
            return [] 
        if ime_in_priimek[i] != " ":
            if ime_in_priimek[i].isalpha():
                ime += ime_in_priimek[i]
            else:
                return []
            if ime_in_priimek[i].isupper():
                ime_uppercase_counter += 1    
        else:
            index = i
            break
        i += 1
    
    pri_wordcounter = 1
    pri_uppercase_counter = 0
    
    i += 1
    while i < len(ime_in_priimek):
        if ime_in_priimek[i].isupper() == False and ime_in_priimek[i].isalpha() and ime_in_priimek[i-1] == " ":
            return []
        if ime_in_priimek[i] != " ":
            if ime_in_priimek[i].isalpha():
                priimek += ime_in_priimek[i]
            else:
                return []
        else:
            priimek += ime_in_priimek[i]
        if ime_in_priimek[i] == " " and ime_in_priimek[i-1] != " ":
            pri_wordcounter += 1
        if ime_in_priimek[i].isupper():
            pri_uppercase_counter += 1
        
        i += 1
    
    if (any(c.isdigit() for c in ime) == False and any(c.isdigit() for c in priimek) == False and (ime_uppercase_counter == 1) and (pri_uppercase_counter == pri_wordcounter) and ime != "" and priimek != ""):
        ime_priimek_arr.append(ime)
        ime_priimek_arr.append(priimek.strip())
        
    return ime_priimek_arr    

def validiraj_naslov(naslov):
    ulica = ""
    hisna_st = ""
    postna_st = ""
    posta = ""
    naslov_arr = []
    
    naslov = naslov.strip()
    
    st = False
    index = 0
    
    for i in range(len(naslov)):
        if naslov[i].isdigit():
            index = i
            break
        else:
            if naslov[i] == " " and naslov[i+1].isdigit():
                continue
            ulica = ulica + naslov[i]
    
    presledek_index = 0
    temp = ""
    for i in range(index, len(naslov)):     #pridobi hišno, poštno številko 
        if naslov[i] == " ":
            presledek_index = i
            break
        else:
            temp += naslov[i]
    
    postna_st = temp[(len(temp)-4):len(temp)]
    
    hisna_st = temp[:(len(temp)-4)]
    
    for i in range(presledek_index+1, len(naslov)):
        posta += naslov[i]
    
    if naslov[len(naslov)-1].isdigit():
        return []
    
    naslov_arr.append(ulica.strip())
    naslov_arr.append(hisna_st)
    naslov_arr.append(postna_st)
    naslov_arr.append(posta)
    
    return naslov_arr
        
def validiraj_telefonsko(raw_tel_st):
    raw_tel_st = raw_tel_st.strip()
    tel_st = raw_tel_st[0]
    
    for i in range(1, len(raw_tel_st)):
        if raw_tel_st[i] == " ":
            if raw_tel_st[i-1] == " ":
                continue
            else:
                tel_st += raw_tel_st[i]
        else:
            tel_st += raw_tel_st[i]
    
    skupina = 0
    
    #Groba delitev po skupinah
    if tel_st[0] == "+":
        skupina = 2
    elif tel_st[0] == "0" and tel_st[1] == "0" and tel_st[5] == " ":
        skupina = 3
    elif tel_st[2] == " ":
        skupina = 4
    else:
        skupina = 1

    match skupina:
        case 1:
            if len(tel_st) != 11:
                return "False"
            if tel_st[3] != " " or tel_st[7] != " ":
                return "False"
            for i in range(len(tel_st)):
                if i in [3,7]:
                    continue
                elif tel_st[i].isdigit() == False:
                    return "False"
            return tel_st
        
        case 2:
            if len(tel_st) != 15:
                return "False"
            if tel_st[4] != " " or tel_st[7] != " " or tel_st[11] != " ":
                return "False"
            for i in range(1, len(tel_st)):
                if i in [4, 7, 11]:
                    continue
                elif tel_st[i].isdigit() == False:
                    return "False"
            return tel_st
        
        case 3:
            if len(tel_st) != 16:
                return "False"
            if tel_st[5] != " " or tel_st[8] != " " or tel_st[12] != " ":
                return "False"
            for i in range(len(tel_st)):
                if i in [5, 8, 12]:
                    continue
                elif tel_st[i].isdigit() == False:
                    return "False"
            return tel_st
        
        case 4:
            if len(tel_st) != 11:
                return "False"
            if tel_st[2] != " " or tel_st[7] != " ":
                return "False"
            for i in range(len(tel_st)):
                if i in [2, 7]:
                    continue
                elif tel_st[i].isdigit() == False:
                    return "False"
            return tel_st

def validiraj_email(email):
    email = email.strip()
    if email_rgx.fullmatch(email):
        return email
    return "False"

    
