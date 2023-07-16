#Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x=8
y= 3.2
z=8j+18
a= "Hello World"
b= True
c= 23<22
l = [1,2,3,4]
d= {"Name": "Jake",
    "Age":27,
    "Adress": "Downtown"}
t= ("Machine Learning", "Data Science")
s= {"Python", "Machine Learning", "Data Science"}

#type() metodu kullanılır.

"""
x=integer
y=float
z=complex
a=string 
b=boolean
c=boolean
l=list
d=dictionary
t=tuple
s=set
"""

#Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

#Beklenen çıktı: ['THE', 'GOAL','IS','TO','TURN','DATA','INTO','INFORMATION','AND','INFORMATION','INTO',INSIGHT']

text="The goal is to turn data into information, and information into insight."
new_text=text.upper().replace(","," ").replace("."," ").split()
print(new_text)
"""Burada replace() methodunu kullanacağız. Parantez içindeki ilk kısım neyi, ikinci kısım ise ne ile değiştirmek istediğimizi belirtir. 
Önce virgülleri boşluklar ile sonrasında ise noktayı boşluk ile değiştirdik.
split() fonksiyonu ise kelime kelime ayırmaya yarar.
"""

#Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

"""
Adım 1: Verilen listenin eleman sayısına bakınız.
Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım 3: Verilen liste  üzerinden ["D","A","T","A"] listesi oluşturunuz.
Adım 4: Sekizinci indeksteki elemanı siliniz.
Adım 5: Yeni bir eleman ekleyiniz.
Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
"""
lst= ["D","A","T","A","S","C","I","E","N","C","E"]

#Adım 1:
x=len(lst)
print(x)

#Adım 2:
y=lst[0]
z=lst[10]
print(y)
print(z)

#Adım 3:
new_list=lst[:4]
new_list = [f'"{harf}"' for harf in new_list]
new_list= "[" + ",".join(new_list) + "]"
print(new_list)
"""
Burada başlangıçtan 4. elemana kadar (0,1,2,3. elemanlar) yeni bir liste oluşturduk.
Eğer bu kısımda yazdırsaydık sonuç ['D','A','T','A'] şeklinde olacaktı. 
Ancak bizden istenen çift tırnak olduğundan bunu değiştirmek için şu aşamaları izliyoruz:

İlk aşama: 
f"{item}" kullanımını biliyoruz(bize çift tırnaksız halini verecek), burada çift tırnak ile değişim için ya f'"{item}'" ya da f"\"{item}\"" kullanacağız.
Ayrıca bu listedeki her elemanı taraması için bir for döngüsü içine aldık.

İkinci aşama:
Köşeli parantez eklemek için "[" ve "]" ve virgülleri eklemek için de ",".join() methodunu kullandık.
"""

#Adım 4:
a=lst.pop(8)
print(lst)

del lst[8]
print(lst)
"""
Burada göstermek istediğim özellik şu, a diye bir değişkene pop() methodu ile silinecek indeksteki elemanı atıyoruz, sonrasında listemizi olduğu gibi yazdırıyoruz.
Ancak del ile de bir değişken kullanmadan direkt istediğimiz indeksteki elemanı silip listeyi yazdırabiliriz.
"""
#Adım 5:
lst.append("Q")
print(lst)
"""
Eleman eklemek için append() methodu kullanılır.
"""
#Adım 6:
lst.insert(8,"N")
print(lst)
"""
insert() methodu ile istediğimiz indekse istediğimiz elemanı ekleyebiliriz. Parantez içindeki ilk kısım indeks, diğeri ise elemanı temsil eder.
"""

#Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

"""
Adım 1: Key değerlerine erişiniz.
Adım 2: Value'lara erişiniz.
Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım 5: Antonio'yu dictionary'den siliniz.
"""

dict= {'Christian': ["America",18],
       'Daisy': ["England",12],
       'Antonio': ["Spain", 22],
       'Dante': ["Italy",25]}

#Adım 1:
print(dict.keys())
#key değerlerine erişmek için keys() methodu kullanılır.

#Adım 2:
print(dict.values())
#value değerlerine erişmek için values() methodu kullanılır.

#Adım 3:
dict['Daisy'][1]=13
print(dict)
#Anahtar olarak Daisy kullanılır. England 0. indeks, 12 1. indeks.

#Adım 4:
dict['Ahmet']=["Turkey",24]
print(dict)

#Adım 5:
del dict['Antonio']
print(dict)
#Silmek için yukarıdaki örnekte yaptığımız gibi anahtarı girip del kullanabiliriz.

#Görev 5: Argüman olarak bir liste alan, liste içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonskiyon yazınız.
"""
Bir sayının tek mi çift mi olduğunu belirlemek için 2 ile modunun (2 ile bölümünden kalanının) 0'a eşit olup olmadığına bakmak gerekir.
"""

l= [2,13,18,93,22]

def func(list):
    even_list=[]
    odd_list=[]

    for number in list:
        if number %2==0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return even_list, odd_list

even_list, odd_list=func(l)

print(even_list)
print(odd_list)

#Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
ogrenciler= ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i, ogrenci in enumerate(ogrenciler, start=1):
    if i<=3:
        print(f"Mühendislik Fakültesi {i}. öğrenci: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {i-3}. öğrenci {ogrenci}")

""""
enumerate() fonksiyonu kullanarak ogrenciler listesindeki öğrencilerin indeksleri ve isimleri alınır.
start=1 parametresi, indekslerin 1'den başlamasını sağlar (normalde 0'dan başlayacaktı).
İlk 3 öğrenci mühendislik fakültesine aittir dediği için i<=3 koşulu ile 1'den başlayıp ilk 3 öğrenciyi alırız.
Kalan indekslerdeki öğrenciler ise else koşulu ile i'den ilk 3 öğrenci çıkarılarak yazdırılır.
"""

#Görev 7: Aşağıda 3 adet liste verilmiştir.Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu=["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi= [3,4,2,4]
kontenjan= [30,75,150,25]

ders_info=zip(ders_kodu,kredi,kontenjan)

for ders_kodu,kredi,kontenjan in ders_info:
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsıyor ise ortak elemanlarını eğer kapsamıyor ise 2.kümenin 1.kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1= set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])

"""
Kapsayıp kapsamadığını kontrol etmek için issuperset() methodu, 
farklı ve ortak elemanlar için ise intersection ve difference methodları kullanılır.
"""
if kume2.issuperset(kume1)== True:
    print(kume2.intersection(kume1))
else:
    print(kume2.difference(kume1))