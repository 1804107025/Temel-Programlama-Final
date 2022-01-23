# Onur Akşen 1804107025

ordek_liste = [
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

puanlar = {"siyah": 500, "mavi": 1000, "yeşil": 5000, "kırmızı": 0}

# Döngüde sözlüğü yazdırma
print("Ördekler: \n")
for sozluk in ordek_liste:
    print(sozluk)

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

# Toplam puan ve vurulmayan sayısı
print("Toplam puan", puan)
print("Vurulmayan ördek sayısı: ", 10 - len(vurulanlar))
