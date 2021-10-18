def print_menu():
    print("1. Citire lista.")
    print("2. Afișarea listei după eliminarea duplicatelor.")
    print("3. Afișarea sumei primelor n numere pozitive din listă.")
    print("4. Afisare daca toate nr. pozitive din lista sunt in ordine crescatoare")
    print("5. Afișarea listei obținute din lista inițială"
          "în care numerele care apar doar o singură dată sunt"
          "înlocuite cu numărul de divizori proprii ai numărului.")
    print("a. Afisare lista")
    print("x. Iesire")


def citireLista():
    """
    citim lista
    :return: lista citita
    """
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l


def eliminare_dublicate(l: list[int]) -> list[int]:
    """elimina dublicatele din lista

    :param l:
    :return: rezultat: lista rezultata dupa eliminarea dublicatelor
    """
    rezultat = []
    for x in l:
        if x not in rezultat:
            rezultat.append(x)

    return rezultat


def test_eliminare_dublicate():
    assert eliminare_dublicate([10, 25, 13, 25, 48, 10, 25]) == [10, 25, 13, 48]


def suma_primelor_n_nr_pozitive(n,l):
    """
    calculaza suma primelor n nr pozitive din lista
    :param l: lista data
    :param n: nr dat
    :return: suma daca exista cel putin n nr pozitive in lista, “Dimensiunea listei este prea
    mică”. in caz contrar
    """
    suma=0
    contor=0
    for x in l:
        if x>0:
            suma+=x
            contor+=1
        if n == contor:
            return suma
    return "Dimensiunea listei este prea mica"


def test_suma_primelor_n_nr_pozitive():
    assert suma_primelor_n_nr_pozitive(3, [10, -3, 25, -1, 3, 25, 18]) == 38
    assert suma_primelor_n_nr_pozitive(12,[10, -3, 25, -1, 3, 25, 18]) == "Dimensiunea listei este prea mica"
    assert suma_primelor_n_nr_pozitive(4, [10, -3, 25, -1, 3, 2, 18]) == 40


def poz_crescatore(l):
    """
        verifica daca toate nr pozititve din lista se afla in ordine crescatoare
    :param l: lista verificate
    :return: bool: daca toate nr pozititve din lista se afla in ordine crescatoare, false contrar
    """
    ultim=-1
    for x in l:
        if x>0:
            if  x <ultim:
                return False
            else:
                ultim = x
    return True


def test_poz_crescatore():
    assert poz_crescatore([10, 13, -1, 24, 33, 45]) == True
    assert poz_crescatore([10, 13, -1, 24, 3, 45]) == False


def nr_divizori(x):
    """
    calculeaza nr de divizori proprii
    :param x: nr la care ii aflam divizorii
    :return:  nr de divizori proprii
    """
    nrdivi=0
    k=int(x)
    for i in range(2, k//2+1):
        if x%i == 0:
            nrdivi+=1
    return float(nrdivi)



def test_nr_divizori():
    assert nr_divizori(7) == 0
    assert nr_divizori(9) == 1
    assert nr_divizori(6) == 2

def div_proprii(l):
    ok=[]
    nok=[]
    for x in l:
        if x in ok:
            ok.remove(x)
            nok.append(x)
        elif x not in nok:
            ok.append(x)
    nr_div_lista=[]
    for x in l:
        if x not in ok:
            nr_div_lista.append(x)
        else:
            nr_div_lista.append(nr_divizori(x))
    return nr_div_lista

def test_div_proprii():
    assert div_proprii([25, 13, 26, 13, 19]) == [1, 13, 2, 13, 0]
    assert  div_proprii([6, 8, 7]) == [2, 2, 0]

def main():
    test_eliminare_dublicate()
    test_poz_crescatore()
    test_nr_divizori()
    test_suma_primelor_n_nr_pozitive()
    test_div_proprii()
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(eliminare_dublicate(l))
        elif optiune == "3":
            m = int(input("n="))
            print(suma_primelor_n_nr_pozitive(m,l))
        elif optiune == "4":
            ok=poz_crescatore(l)
            if ok:
                print("Da")
            else:
                print("Nu")
        elif optiune == "5":
            print(div_proprii(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()