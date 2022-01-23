# Onur Akşen 1804107025

import random as rd


def randOrdek():
    puanlar = {"siyah": 500, "mavi": 1000, "yeşil": 5000, "kırmızı": 0}
    renk_listesi = list(puanlar.keys())
    liste = []
    bulundu = 0

    while len(liste) < 10:
        x = rd.randint(1, 10)
        y = rd.randint(1, 10)

        for ordek in liste:  # koordinat kontrol ediliyor
            if ordek["x"] == x and ordek["y"] == y:
                bulundu = 1
                break
        if bulundu:  # koordinat dolu
            continue

        else:  # koordinat boş
            renk = renk_listesi[rd.randint(0, 3)]
            puan = puanlar[renk]
            liste.append({"renk": renk, "puan": puan, "vuruldu": False, "x": x, "y": y})

    return liste
