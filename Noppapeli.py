
'''
Created on 14.4.2016
@author: VsKatshuma

Pelin kulku:
1) Arvaa kahden nopan yhteenlaskettu silmäluku
2) Heitä noppaa
3) Näytä kahden nopan yhteenlaskettu tulos ja ilmoita pelaajalle osuiko arvaus oikein
4) Aloita uusi kierros tai lopeta ohjelma
'''

from random import randrange

def init():
    print("\n{:^39s}".format("* * * * * * * * * * * * * * * * * * * *"))
    print("{:^39s}".format("Noppapeli v1.0"))
    print("{:^39s}".format("(c) Jussi \"VsKatshuma\" Hirvonen"))
    print("{:^39s}\n".format("* * * * * * * * * * * * * * * * * * * *"))
    print("Arvaa kahden nopan yhteenlaskettu silmäluku:")
    guess(True)

def guess(ensimmäinen):
    rivi = input()
    if (rivi or ensimmäinen):
        try:
            arvaus = int(rivi)
            if (arvaus < 2 or arvaus > 12):
                print("Arvauksen on oltava väliltä 2-12.")
                guess(ensimmäinen)
            else:
                print("Arvasit tulokseksi {:d}.".format(arvaus))
                roll(arvaus)
        except ValueError:
            print("Arvauksen on oltava kokonaisluku.")
            guess(ensimmäinen)
    else:
        print("Noppapeli päättyy.")

def roll(arvaus):
    heitto1 = randrange(6) + 1
    print("Ensimmäisen nopan silmäluku on {:d}.".format(heitto1))
    heitto2 = randrange(6) + 1
    print("Toisen nopan silmäluku on {:d}.".format(heitto2))
    tulos = heitto1 + heitto2
    if (arvaus is tulos):
        print("Yhteenlaskettu silmäluku on {:d}. Arvauksesi osui oikein!".format(tulos))
    else:
        print("Yhteenlaskettu silmäluku on {:d}. Arvauksesi ei osunut oikein.".format(tulos))
    print("\nVoit pelata uudestaan arvaamalla uuden silmäluvun. Lopeta ohjelma tyhjällä rivillä.")
    guess(False)

init()
