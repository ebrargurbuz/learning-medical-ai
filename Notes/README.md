# Python Notlarım

## map() fonksiyonu -> Bir fonksiyonu listedeki tüm elemanlara uygular.

**kullanımı**


map(fonksiyon, liste)

sayılar = [1, 2, 3]
print(list(map(lambda x: x**2, sayılar)))  
*[1, 4, 9]*

---

## lambda() fonksiyonu -> adı olmayan küçük fonksiyonları tanımlar.

**kullanımı**

kare = lambda x: x * x
print(kare(5))
*25*

--- 

## Fonksiyon,for,while Tanımı:

**for** 

for i in range(5):
    print(i)
*0,1,2,3,4*

**while**

sayi = 0
while sayi < 3:
    print(sayi)
    sayi +=1

**fonksiyon**

def selamla(isim):
    print(f"Merhaba {isim}")

**return**

def topla(x,y):
    return x + y

---

## Liste, Tuple, Set, Dictionary:

**Liste**

liste = [1,2,3]
liste.append(4)

**Tuple (Demet)**

# Birden fazla veriyi tek bir değişkende saklamak için kullanılır.Listeden farkı *değiştirilemez* olmasıdır. Bellek tasarrufu yapar.

kisi = ("Ebrar", 20)
print(kisi[0])
*Ebrar*

t = (1, 2, 3)

**Set**

s = {1, 2, 2, 3} 
*Tekrar edenleri siler*

**Dictionary**

kisi = {"isim" : "Ebrar", "yas": 20}
print(kisi["isim"])

ogrenci.keys()       # dict_keys(['isim', 'okul', 'bölüm'])
ogrenci.values()     # dict_values(['Ebrar', 'Karabük Üniversitesi', 'Bilgisayar Müh.'])
ogrenci.items()      # dict_items([('isim', 'Ebrar'), ('okul', ...)])


---

## Hata Yönetimi (try / except):

try:
    x = 5 / 0

except ZeroDivisionError:
    print("Sıfıra bölünemez")

---

## Dosya Okuma-Yazma:

with open("dosya.txt", "r") as f:
    içerik = f.read()

with open("dosya.txt", "w") as f:
    f.write("Merhaba Ebrar!")

---

## filter() fonksiyonu -> Bir koşula uyan elemanları **süzmek** için kullanılır.

**kullanımı**

nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even)) 
# [2, 4, 6]

*Unutma: filter() sonucu doğrudan liste değildir → list() ile çevrilmeli*

---

## zip() fonksiyonu -> iki listeyi indekslerine göre eşleştirir.

isimler = ["Ebrar","Eren"]
yaşlar = [20,21]
eşleşme = list(zip(isimler, yaslar))
print(eşleşme)

*[('Ebrar', 20), ('Eren', 21)]*


## enumerate() fonksiyonu -> listeyi döngüye sokarken indeks de verir.

for i, val in enumerate(["a","b","c"]):
    print(İ,val)

*0 a*
*1 b*
*2 c*

## Sınıflar (Classes) :

*Sınıf, nesneler oluşturmak için bir şablondur.*
*Sınıf -> Kalıp, Nesne -> o kalıptan çıkan gerçek örnek*

- `class` ile tanımlanır
- Nesneler bu sınıftan üretilir
- `__init__()` kurucu fonksiyondur
- `self` → nesnenin kendisini temsil eder

class Ogrenci:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def tanit(self):
        print(f"Benim adım {self.isim}, yaşım {self.yas}")

# Nesne oluşturalım

ebrar = Ogrenci("Ebrar", 20)
ebrar.tanit() 
*Benim adım Ebrar, yaşım 20*

