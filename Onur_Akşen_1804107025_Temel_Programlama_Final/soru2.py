# Onur Akşen 1804107025

# kullanıcıdan girdi isteme
girdiler = []
print("x y formatında 10 adet koordinat giriniz: \n")
while len(girdiler) < 10:
    x, y = map(int, input().split())
    if (x < 1 or x > 10) or (y < 1 or y > 10):
        print("Geçersiz giriş \n")

    else:
        girdiler.append([x, y])

# vurulan ördekleri bulma
vurulanlar = []
puan = 0

for atis in girdiler:
    for ordek in ordek_liste:
        if atis[0] == ordek["x"] and atis[1] == ordek["y"]:  # vuruş
            vurulanlar.append([atis])
            puan += ordek["puan"]
            ordek["vuruldu"] = True

print("Vurulan ördeklerin koordinatları: ", vurulanlar)

# Döngüde sözlüğü yazdırma
print("Ördekler: \n")
for sozluk in ordek_liste:
    print(sozluk)