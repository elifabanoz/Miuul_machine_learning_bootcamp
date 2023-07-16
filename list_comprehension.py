#Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df= sns.load_dataset("car_crashes")
num_columns= [f"NUM{column.upper()}" for column in df.select_dtypes(include= 'number').columns]
print(num_columns)
"""
 seaborn kütüphanesini kullanarak verilen "car_crashes" veri setini yükledik.
 'df' adında bir DataFrame oluşturduk. 
 Numeric değişkenleri istediği için select_dtypes(include='number') kullanarak sadece sayısal değişkenlere sahip sütunlar seçtik.
 Ardından for ile tarayıp upper() methodunu kullanarak her bir sütunun adını büyük harfe çevirerek NUM ile birleştirdik.
 """

#Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns
df= sns.load_dataset("car_crashes")
columns= [f"{column.upper()}FLAG" for column in df.columns if "no" not in column]
print(columns)

"""
Bir önceki örnekte değişkenlerin başına NUM eklemek için f"NUM{item}" yapısını kullanmıştık.
Sonuna eklemek için ise istenilen kelimeyi yapının sonuna yazacağız. f"{item}FLAG"
DataFrame'imizdeki sütunları for döngüsü ile tarayarak (for column in df.columns)
 isminde "no" barındırmayan değişkenleri if yapısı ile seçtik. Eğer "no" yok ise (if "no" not in column) sonuna FLAG ekle.
upper() methodu ile de isimleri büyüttük.
"""
#Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]
new_cols = [column.upper() for column in df.columns if not any(item in column for item in og_list)]
new_df = df[new_cols]
print(new_df)

"""
og_list içinde her bir öğe(item), column adlı değişkenin içindeki sütun adları ile karşılaştırılır.
Eğer item sütun adında bulunuyorsa True, bulunmuyorsa False döndürür. 
Burada og_list içindeki öğelerin hiçbirinin column adlı sütun adında bulunmaması durumunu konrtol eder. 
Bulunmaması isteniliyor.
"""