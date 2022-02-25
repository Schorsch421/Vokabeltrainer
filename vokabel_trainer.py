import random, os
from shutil import copyfile

class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch
    
    def toString(self):
        return self.deutsch + " - " + self.englisch

try:
    datei = open('vocabulary.txt', 'r+')
except FileNotFoundError:
    datei = open('vocabulary.txt', 'w+')
    datei.close()
    datei = open('vocabulary.txt', 'r+')
eintraege = [Entry("Hallo", "hello")]

try:
    line = datei.readlines()
    i = 1
    while True:
        eintraege.append(Entry(line[i].strip('\n'), line[i + 1].strip('\n')))
        i += 2
        if len(line) == i:
            break
except IndexError:
    pass

def eingabe():
    datei = open('vocabulary.txt', 'a')
    while True:
        deutsch = input("Deutsches Wort: ") #gegebenenfalls zuändern
        if deutsch == "#fertig":
            return
        englisch = input("Englisches Wort: ") #gegebenenfalls zuändern
        if englisch == "#fertig":
            return
        eintraege.append(Entry(deutsch, englisch))
        datei.write('\r' + deutsch)
        datei.write('\r' + englisch)

def abfrage():
    while True:
        i = random.randint(0, len(eintraege)-1)
        englisch = input("Englische Ubersetzung von " + str(eintraege[i].deutsch) + ": ") #gegebenenfalls zuändern
        if(englisch == "#fertig"):
            return
        if eintraege[i].englisch == englisch:
            print("korrekt!")
        else:
            print("leider falsch. Richtige Antwort: " + str(eintraege[i].englisch))

def printall():
    for eintrag in eintraege:
        print(eintrag.toString())

def löschen():
    i = 1
    try:
        while True:
            print(str(i) + ". " + str(eintraege[i].deutsch) + " - " +  str(eintraege[i].englisch))
            if i + 1 == len(eintraege):
                break
            i += 1
    except IndexError:
        print("noch nichts gespeichert")
        return
    try:
        zeile = int(input("Welche Vokabel soll gelöscht werden?"))
    except ValueError:
        print("bitte Zahl eingaben")
        return
    try:
        bestätig = input(eintraege[zeile].deutsch + " - " + eintraege[zeile].englisch + " wirklich löschen?(j = ja)")
    except IndexError:
        print("Nur zwichen 1 oder" + str(len(eintraege) - 1) + "eingeben!")
        zeile = int(input("Welche Vokabel soll gelöscht werden?"))
        bestätig = input(eintraege[zeile].deutsch + " - " + eintraege[zeile].englisch + " wirklich löschen?(j = ja)")
    if bestätig !=  'j':
        print("nicht gelöscht")
        return
    lös = int((zeile * (zeile + 1) /2) / zeile)
    copyfile('vocabulary.txt', 'vocabulary_cache.txt')
    datei = open('vocabulary.txt', 'w+')
    datei1 = open('vocabulary_cache.txt', 'r')
    lines = datei1.readlines()
    count = 0
    while True:
        if count == len(lines):
            break
        if count == lös or count == lös + 1:
            pass
        else:
            datei.write(str(lines[count]))
        count += 1
    datei1.close()
    datei.close()
    os.remove('vocabulary_cache.txt')
    datei = open('vocabulary.txt', 'r+')
    line = datei.readlines()
    c = 1
    eintraege.clear()
    eintraege.append(Entry("Hallo", "hello"))
    while True:
        eintraege.append(Entry(line[c].strip('\n'), line[c + 1].strip('\n')))
        c += 2
        if len(line) == c:
            break
    print("fertig")

while True:
    befehl = input("Befehl: ")
    if befehl == "eingabe":
        eingabe()
        datei.close()
    elif befehl == "abfrage":
        abfrage()
    elif befehl == "beenden":
        datei.close()
        break
    elif befehl == "ausgabe":
        printall()
    elif befehl == "löschen":
        datei.close()
        löschen()
    else:
        print("keine bekannte Ausgabe. Tippe eingabe, abfrage, ausgabe, löschen oder beenden.")