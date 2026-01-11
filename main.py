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



if __name__ == "__main__":
    pot = "D:/Faks/data"
    datoteke = pridobi_txt(pot)
    st = len(datoteke)
    print(st)

    vsebina = branjeTXT(datoteke[0])
    print(vsebina)