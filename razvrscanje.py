import locale

#Rabimo zaradi sortiranja sumnikov
#Ker sumnike tretiral kot osnovno obliko crke č => c š => s
locale.setlocale(locale.LC_COLLATE, "sl_SI.UTF-8")

def pisanjeSortiranihPodatkov(polje, argument = "a"):
    with open("sortiraniPodatki.txt", argument, encoding="utf-8") as dat:
        for oseba in polje:
            niz = f"{oseba['ime']} {oseba['priimek']}_{oseba['ulica']} {oseba['hisnaSt']} {oseba['postnaSt']} {oseba['posta']}_{oseba['telefonska']}_{oseba['email']}\n"
            dat.write(niz)

def merge(polje, kljuc, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #To ustvari array L dolzine n, kjer je vsak element 0
    L = [None] * n1
    R = [None] * n2

    for i in range(n1):
        L[i] = polje[l + i]
    
    for j in range(n2):
        R[j] = polje[m + 1 + j]
    
    i = j = 0
    k = l

    while i < n1 and j < n2:
        if locale.strcoll(L[i][kljuc], R[j][kljuc]) <= 0:
            polje[k] = L[i]
            i += 1
        else:
            polje[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        polje[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        polje[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(polje, kljuc, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(polje, kljuc, l, m)
        mergeSort(polje, kljuc, m + 1, r)
        merge(polje, kljuc, l, m, r)


    


