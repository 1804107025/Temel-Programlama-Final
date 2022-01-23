# Onur Akşen 1804107025

import random as rd


def ordek_yarat():
    ordek_liste = \
        [
            {'renk': 'siyah', 'puan': 500, 'vuruldu': False, 'x': 9, 'y': 5},
            {'renk': 'siyah', 'puan': 500, 'vuruldu': False, 'x': 4, 'y': 1},
            {'renk': 'kırmızı', 'puan': 0, 'vuruldu': False, 'x': 6, 'y': 1},
            {'renk': 'mavi', 'puan': 1000, 'vuruldu': False, 'x': 10, 'y': 10},
            {'renk': 'yeşil', 'puan': 5000, 'vuruldu': False, 'x': 9, 'y': 4},
            {'renk': 'kırmızı', 'puan': 0, 'vuruldu': False, 'x': 7, 'y': 1},
            {'renk': 'yeşil', 'puan': 5000, 'vuruldu': False, 'x': 10, 'y': 8},
            {'renk': 'kırmızı', 'puan': 0, 'vuruldu': False, 'x': 10, 'y': 3},
            {'renk': 'mavi', 'puan': 1000, 'vuruldu': False, 'x': 6, 'y': 2},
            {'renk': 'mavi', 'puan': 1000, 'vuruldu': False, 'x': 7, 'y': 10},
        ]

    return ordek_liste


def girdiAl(liste):
    girdiler = []
    print("x y formatında 10 adet koordinat giriniz: \n")
    while len(girdiler) < 10:
        x, y = map(int, input().split())
        if (x < 1 or x > 10) or (y < 1 or y > 10):
            print("Geçersiz giriş \n")

        else:
            girdiler.append([x, y])

    vurulanlar = []

    for atis in girdiler:
        for ordek in liste:
            if atis[0] == ordek["x"] and atis[1] == ordek["y"] and not ordek["vuruldu"]:  # vuruş
                vurulanlar.append([atis])
                ordek["vuruldu"] = True
    return vurulanlar


def puanHesapla(liste):
    puan = 0
    for ordek in liste:
        if ordek["vuruldu"]:
            puan += ordek["puan"]

    return puan


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
