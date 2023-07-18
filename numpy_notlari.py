import numpy as np
#kütüphane

np.array([1,2,3,4,5,6])
#array oluşturdu

np.zeros(10,dtype=int)
#0'lardan oluşan integer bir array oluşturdu

np.random.randint(0,10,size=10)
#0 ile 10 arasında rastgele 10 integer

np.random.normal(10,4,(3,4))
#normal dağılım kitle ortalaması, standart sapma, kaça kaçlık bir array

a=np.random.randint(10,size=5)
#0 ile 10 arasında 5 sayı

a.ndim
#boyut sayısı 1

a.shape
#boyut bilgisi (5,)

a.size
#toplam eleman sayısı 5

a.dtype
#array veri tipi int64

np.random.randint(1,10,size=9).reshape(3,3)
#3'e 3'lük bir array'e çevirdi

a=np.random.randint(10,size=10)

a[0]
#0. indeksteki eleman

a[0:5]
#0'dan 5'e kadar 4 sayı

a[0]=999
#0. indeksteki eleman 999 oldu

m= np.random.randint(10,size=(3,5))

m[0,0]
#0. satır 0. sütundaki sayı, ilk bölüm satır için diğeri sütun

m[2,4]=99
#2. satır 4.sütundaki sayı 99 oldu

m[3,6]=3.9
#float değeri integer (2) olarak girer

m[:,0]
#tüm satırları seç, 0. indeksteki sütunu seç

m[1,:]
#1. indeksteki satırı seç, tüm sütunları seç

m[0:2, 0:3]
#satırlarda 0'dan 2'ye kadar git, sütunlarda 0'dan 3'e kadar git

v=np.arange(0,30,3)
#0'dan 30'a kadar(30 hariç) 3'er artacak şekilde array oluştur

catch=[1,2,3]

v[catch]
#catch değerlerine karşılık gelen v'deki değerleri alır

x=np.array([1,2,3,4,5,6])

#3'ten küçük olan sayılar

ab=[]
for i in v:
    if i<3:
        ab.append(i)

v<3
v[]
#boolean tipinde true false döndürür

v[v<3]
#true olanları alıp yazdırır, daha kısa yol

v/5
#bütün elemanları 5'e bölüp verir

np.subtract(v,1) #çıkarma
np.add(v,1) #toplama
np.mean(v) #ortalama
np.sum(v) #toplamı
np.min(v) #minimum
np.max(v) #maximum
np.var(v) #varyans

#işlemlerin kalıcı olması için bir değişkene atarız


5*x + y=12
x + 3y =10

a=np.array([5,1],[1,3]) #bilinmeyenlerin katsayıları
b=np.array([12,10]) #eşitliğin sağındaki sayılar

np.linalg.solve(a,b)
