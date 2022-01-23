# Onur Akşen 1804107025

for atis in girdiler:
    for ordek in ordek_liste:
        if atis[0] == ordek["x"] and atis[1] == ordek["y"]:  # vuruş
            vurulanlar.append([atis])
            puan += ordek["puan"]
            ordek["vuruldu"] = True

print("Vurulan ördeklerin koordinatları: ", vurulanlar)

# Toplam puan ve vurulmayan sayısı
print("Toplam puan", puan)
print("Vurulmayan ördek sayısı: ", 10 - len(vurulanlar))