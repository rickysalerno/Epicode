#!/usr/bin/env python


pigreco  = 3.14


def perimetro_quadrato(lato):
    return lato * 4


def circonferenza_cerchio(raggio):
    return ((2 * pigreco) * raggio)


def perimetro_rettangolo(base, altezza):
    return ((base * 2) + (altezza *2) )


def lista_figure():
    print(f"Ciao, adesso dovrai scegliere una serie di figure a scelta.\n")
    scelta = str(input("Seleziona una figura tra quadrato, cerchio e rettangolo:   "))
    if (scelta == "quadrato"):
        print(f"Hai scelto -> {scelta}")
        lato = int(input("Inserisci il valore del lato:   "))
        print(f"Il risultato del perimetro del quadrato è:  {perimetro_quadrato(lato)}")
    elif (scelta == "cerchio"):
        print(f"Hai scelto -> {scelta}")
        raggio = int(input("Inserisci il valore del raggio:   "))
        print(f"Il risultato del perimetro del quadrato è:  {circonferenza_cerchio(raggio)}")
    elif (scelta == "rettangolo"):
        print(f"Hai scelto -> {scelta}")
        base = int(input("Inserisci il valore della base:   "))
        altezza = int(input("Inserisci il valore dell' altezza:   "))
        print(f"Il risultato del perimetro del rettangolo è:  {perimetro_rettangolo(base,altezza)}")
    else:
        print("Mi spiace, ma non ho capito cos'hai scelto.")


lista_figure()
