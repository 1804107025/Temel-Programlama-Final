# Onur Akşen 1804107025

import ordekmodul as om

ordek_liste = om.randOrdek()

vurulanlar = om.girdiAl(ordek_liste)
print("Vurulan ördeklerin koordinatları: ", vurulanlar)

puan = om.puanHesapla(ordek_liste)
print("Toplam puan: ", puan)
print("Vurulmayan ördek sayısı: ", 10-len(vurulanlar))
