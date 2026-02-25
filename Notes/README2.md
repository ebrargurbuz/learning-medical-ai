**numPy Notları**

# np.array ->  *listeler gibi veri saklar*

# np.arange(min,max+1) -> *minimum değerden maksimum değere kadar olan veriler basılır*

# np.arange(min,max,frekans) -> *minimum değerden maksimum değere kadar olan veriler, girilen frekansa göre basılır*

# np.zeros() -> *parantez içerisindeki sayı kadar liste içerisinde sıfır basılır*
### **örneğin** np.zeros(3) : array([0., 0., 0.])
### **örneğin** np.zeros(5,5): *5 satır 5 sütun şeklinde sıfırlar.*

# np.ones() -> *zerosla aynı mantıkla çalışır ama 1 basılır, 0 değil.*

# np.linspace(min,max,durak sayısı) -> *durak sayısı, minimumdan maksimum değere giderken kaç kez sıçrama yaptığını gösterir*

# np.eye() -> *parantez içerisindeki sayı **birim matrisin** boyutunu gösterir.*

# np.random.rand() -> *parantez içerisindeki sayı kadar random değer basar,matris şeklinde de kullanılabilir.(5,5) gibi*

# np.random.randint(min,max) -> *minimum ve maksimum sayı arasından bir rastgele değer basılır*

# np.random.randint(min,max,adet) -> *adet kadar rastgele sayı basar*

# ranarr.max() ve ranarr.min() -> *bir listeki maksimum ve minimum değerleri bulur.*

# ranarr.argmax() ve ranarr.argmin() -> *bir listedeli maksimum ve minmum değerlerin yerlerini gösterir.*


**numPy tekrar notları**

# Arange fonksiyonu, verdiğiniz 2 sayı arasını Array’e çevirir. 
# np.arange(0,100)  *bu fonk 0 ila 100 değerleri arasını array olarak depolar*
# np.arange(0,100,5)  *aynısı ama 5 er 5er atlayarak ilerler*

# Zeros Fonksiyonu, belirttiğiniz miktar kadar 0'lardan oluşan bir Array yaratacaktır.
# np.zeros(100) *100 adet 0'dan olusan array bastır*
# Ones Fonksiyonu, belirttiğiniz miktar kadar 1'lerden oluşan bir Array oluşturacaktır.
# np.ones(100) *100 adet 1 den olusan array bastır*
# np.eye(10) *10 satır 10 sutundan oluşan birim matristen oluşan array*

# Linspace Fonskiyonu: Bu fonksiyon, genel olarak 3 değer alır. İlk 2 değer arasında olan sayıları 3. sayıya eşit olarak dağıtır.
# np.linspace(0,100,5) *0 ve 100 arasını 5 eşit parçaya böl ve göster* # array([  0.,  25.,  50.,  75., 100.])

# np.random.randint(0,100) *0 ve 100 arasında ranstgele bir sayı üret*
# np.random.randint(0,100,5) *0 ve 100 arasında 5 tane rastgele sayı bastır*
# np.random.rand(5) *0 ve 1 arasında 5 değer bastır* 
# np.random.randn(5) *Bu dağılımdaki değerlerin büyük kısmı -1 ile 1 arasına düşer, ama daha küçük veya büyük değerler de olabilir. 5 tane rastgele sayı*

# reshape metodu datayı istediğimiz şekli vermemizi sağlar ve matrise çevirir. *Data1.reshape(15,15)*

# Data1.cumsum() *kümülatif olarak toplar*
# Data1.min() *en küçük değeri döndürür*
# Data1.max() *en buyuk değeri döndürür*
# Data1.sum() *tüm veriyi toplar*
# Data1.argmax() *en büyük sayının indexini verir*
# Data1.argmin() *en küçük sayının indexini verir*

# Data2 = np.array([[1,2],[3,4]])
# np.linalg.det(Data2) *bu fonksiyon determinantını alır*
# stddev = np.std(Data1) *Standart sapmayı bulur.*
# variance = np.var(Data1) *varyansını bulur*

# Data1[:6] *0 dan 6. indexe kadar bastır*
# Data1[::3] *baştan sonra 3 atlaya atlaya ilerle*
# Data1[:1] = 10 *Data1 listesinin ilk 1 elemanını al ve o elemanı 10 ile değiştir.*

# Numpy Transpose Kullanımı: *Matrisin satırlarını sütun, sütunlarını satır yapma işlemi -> .T kullanılır*


**Pandas**


*‘.csv’ ve ‘.txt’ dosyalarını açmak ve içerisinde bulunan verileri okuyarak istenen sonuca kolayca ulaşmak için kullanılmaktadır.* 

### Seriler ###

data = np.array['a','b','c','d']
Series = pd.Series(data,[100,101,102,103])


dataIsim = {'Ebrarın sınav sonucu = ' 35 , 'Ayşenin sınav sonucu = ' 70}
A = pdSeries(dataIsim)

### DataFrameler ### 
df = pd.DataFrame(data = randn(5,5), index = ['A' ,'B', 'C', 'D' ,'E'])
columns = ['Columns1','Columns2','Columns3','Columns4','Columns5']

*output: A B C D E satır satır dizilirlem columnslar sütun sütun dizilir ve bu matrislerin içerisi rastgele -1 ile 1 arasında olan sayılarla doldurulur.*

**Sütun çekme**
*df['Columns4'] yazarsan 4.sutundaki veriler A B C D E satılarının karşısında belirir.*
*Ayrıca aynı yöntemle birden fazla sütunu da alabilirsin: df[['Columns1','Columns5']]*


**Sütun ekleme**
*df['Columns6'] = pd.Series(randn(5), ['A' ,'B', 'C', 'D' ,'E'])*


**İşlem**
*df['Columns7'] = (df['Columns6'] + df['Columns4'] - df['Columns1'] ) / df['Columns2'] * df['Columns3']*

**Sütun çıkarma**
*df.drop('Columns2', axis = 1, inplace = True)*
*Axis -> default değeri 0'dır, İnplace bir işlemin kalıcı olup olmadığını belirler, True ise kalıcı, False ise anlıktır.* 

**loc ve iloc kullanımı**
*df.loc['C'] -> C satırındaki değeleri bastırır. df.iloc[2] ise locla aynı çıktıyı verir. Anlayacağın üzerine birinde direkt stringi girerkenü diğerinde index sayısını giriyoruz. Loc başına i alması da oradan gelir.*


*df.loc['A','Columns5'] -> gibi kullanımlar direkt istediğimiz koordinatı verir.*
*df.loc[['A','Columns5'] and ['B','Columns4']] kullanımı yerine df.loc[['A','B'],['Columns5','Columns4']] kullanımı daha doğrudur*


### DataFrame Filtreleme işlemleri ###

*Öncesinde oluşturulmuş bir 5,5lik matris tablosu ve değerleri olsun.*

*df > 0.2 -> tablo uzerinde 0.2 den büyük değerler True dönerken şartı sağlamayanlar False döndürür.*
*df['Columns1'] > 0*

*df['Columns6'] = ['NewValue1','NewValue2','NewValue3','NewValue4','NewValue5'] -> Veriyi güncellerken verilen değer ‘String’ olsa bile direk atandığıdır.*


### Bozuk Ve Kayıp Verilerle Ugraşabilmek ### 

*np.nan’ kodu veride ‘Not a Number’ oluşturuyor.*
*df.dropna() -> Index satırında en az bir 'NaN' var ise siler.*
*df.dropna(axis = 1) -> Axis’ parametresini ‘Column’a göre ayarladığımızda içinde hiç ‘NaN’ değeri olmayan ‘Column1’i bize döndürür ve diğerlerini siler. Aynı zamanda ‘inplace’ değerini ‘True’ vermediğiniz müddetçe kalıcı değildir.*
*df.dropna(thresh = 2) -> En az iki düzgün veri var ise silme’ anlamına gelmektedir. İstediğin sayı değerini verebilirsin.*
*df.fillna(value = 0) -> NaN değerleri yerine 0.0 yazılır*
*df.sum() -> Sütunlardaki index değerlerini toplar ve tek index şeklinde yazar.*
*df.sum().sum()-> Toplanan sütun değerlerinin hepsini toplar ve tek bir değer haline getirir.* 
*df.fillna(value = (df.sum().sum())/ 5) -> bu kodla birlikte az onceki NaN olan yerleri 0.0 yaptıktan sonra bulduğumuz ortalamayı NaN yerlerine atayabiliriz.*
*df.size -> kaç adet veri olduğunu verir*
*df.isnull() -> True olan değerler 'NaN'ı temsil  eder*
*df.isnull().sum() -> hangi sütunda kaç adet NaN var? sorusunun cevabını verir.*
*df.isnull().sum().sum() -> toplam kaç adet NaN var.*

*axis=0 → dikey yön (sütunlar boyunca)*

*axis=1 → yatay yön (satırlar boyunca)*
### GroupBy Operasyonları ###

*data = {'Job' : ['Data Mining','CEO','Lawyer','Lawyer','Data Mining','CEO'],'Labouring' : ['Immanuel','Jeff','Olivia','Maria','Walker','Obi-Wan'], 'Salary' : [4500,30000,6000,5250,5000,35000]}*

Veri oluşturulduktan sonra DataFrame'e atıyoruz.

*df = pd.DataFrame(data)* ve tablo oluşur.
*SalaryGroupBy = df.groupby('Salary')* Ve ‘Salary’ özelliğine göre gruplamış olduk. Başrol salary yani.
*SalaryGroupBy.sum()* = *df.groupby('Salary').sum()*
*SalaryGroupBy.min()* 
*SalaryGroupBy.max()*  
*df.groupby('Job').sum().loc['CEO']* -> Ceoların maaş toplamı
*df.groupby('Job').count()* -> hangi işten kaç tane var
*df.groupby('Job').min()* -> aynı mesleklerin minimum maaşı
*df.groupby('Job').min()['Salary']['Lawyer']* -> lawyerdaki min maaş
*df.groupby('Job').mean()['Salary']['CEO']* -> mesleğe göre sıralayıp Ceo’ların ortalama maaşını bulduk.


### Concatenate Merge  ###

*Concatenate* -> Temel olarak birleştirme işlemini bu fonksiyon ile yapmaktayız. Aynı listelerdeki ‘zip’ fonksiyonu gibidir. **örnek kod panda.py dosyasında mevcut,ordaki örneği hatırlamak için incele sonra burdan devam et**

*pd.concat([df1,df2])* -> iki veri setini birleştirir.
*pd.concat([df1,df2], axis = 1)* -> Burada olmayan veriler elbetteki ‘NaN’ olarak atanıyor. 

*Merge* -> iki farklı DataFrame’i ortak sütuna göre birleştirmeni sağlar.

*pd.merge(df1, df2, how="inner")* # Ortak olanları alır (default)
*pd.merge(df1, df2, how="left")*   # Sol tabloyu korur
*pd.merge(df1, df2, how="right")*  # Sağ tabloyu korur
*pd.merge(df1, df2, how="outer")*  # Hepsini alır, olmayan yerlere NaN koyar
*pd.merge(df1,df2, on = 'Key')*

### Join Fonksiyonları ### -> bir şey anlamadım, merge daha kullanışlı onu kullanırım



### DataFrame Operasyonları Ve Pivot Table ###

*df['Column2'].unique()* ->‘unique()’ verilen verinin kaç adet ‘eşşiz’ verisi olduğunu bize verir
*df['Column2'].value_counts()* -> ‘value_counts()’ ise hangi değerden kaç adet olduğunu veren bir fonksiyon.
*df.sort_values('Column2', ascending = True)* # Küçükten Büyüğe
*df.sort_values('Column2', ascending = False)* # Büyükten küçüğe
