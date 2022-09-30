Bir programın fonksiyonlar yoluyla oluşturulmasına 
 "prosedürel programlama tekniği" denilmektedir. Sınıflar (classes) "Nesne Yönelimli Programlama Tekniğini (NYPT)" 
    uygulamak için gereken yapı taşlarıdır. NYPT "sınıflar kullanarak program yazma" tekniğidir. Yani işin içine sınıflar 
    girdiğinde artık NYPT'den bahsederiz. 

    Sınıf tanımlamanın (sınıf oluşturmanın) genel biçimi şöyledir:

    class <isim>: <suite>

    Örneğin:

    class Sample:
        pass

 
    Sınıflar aynı zamanda birer tür de belirtmektedir. Oluşturduğumuz bir sınıf türünden nesneler yaratabiliriz. Bir sınıf türünden nesne yaratmanın genel biçimi şöyledir:

    sınıf_ismi([argüman listesi])

    Örneğin:

    s = Sample()

    Burada s artık Sample türünden bir nesnenin adresini tutmaktadır.
NYPT'de bir sınıf türünden nesneye o sınıf türünden bir "örnek (instance)" da denilmektedir. Yani "örnek (instance)" 
    sözcüğü sınıf türünden nesneler için kullanılmaktadır. Sınıflar elemanlara sahip olabilir. Sınıf nesneleri (yani örnekler)
    bileşik nesnelerdir. Yani parçalara sahiptir. Python'da bir sınıf nesnesinin elemanlarına yani parçalarına "öznitelik (attribute)"
    denilmektedir.
#------------------------------------------------------------------------------------------------------------------------
    Bir nesne yaratıldığında henüz nesnenin içi boştur. Örneğin:

    class Sample:
        pass

    s = Sample()

    Burada s değişkeninin gösterdiği yerdeki nesnenin içi henüz boştur. Yani s'in henüz bir özniteliği yoktur. 
#------------------------------------------------------------------------------------------------------------------------
Bir sınıf türünden birden fazla nesne (yani örnek) yaratabiliriz. Örneğin:

    class Sample:
        pass

    s = Sample()
    k = Sample()

    Burada s başka bir nesneyi k;'da başka bir nesneyi göstermektedir. Örneğin:

    >>> s = Sample()
    >>> k = Sample()
    >>> id(s)
    3104147128816
    >>> id(k)
    3104147434752
#------------------------------------------------------------------------------------------------------------------------

    Bir sınıf nesnesi yaratıldığında boştur demiştik. İşte bir nesnenin "öznitelikleri (attributes)" aşağıdaki sentaksla 
    yaratılmaktadır:

    <değişken_ismi>.<öznitelik_ismi> = değer

    Örneğin:

    s = Sample()
    s.a = 10
    s.b = 20
    s.c = 'ankara'

    Burada biz s nesnnesinin içerisinde üç tane öznitelik oluşturduk. Yani artık s'nin ü. elemanı bulunmaktadır. Tabii Pyton'da
    her zaman değişkenler adres tutarlar. s nesnesinin içerisindeki a, b, ve c'de aslında sırasıyşla int, int ve str nesnelerinin 
    adreslerini tutmaktadır. Başka bir deyişle s nesnesinin a, b ve c parçaları içerisinde adresler vardır. Bu adreslerde sırasıyla 
    int bir nesne, int bir nesne ve str türünden bir nesne bulunmaktadır. 

#------------------------------------------------------------------------------------------------------------------------
    Bir sınıf nesnesi için öznitelik yaratıldıktan sonra bu öznitelik istenildiği zaman <değişken_ismi>.<öznitelik_ismi> 
    sentaksıyla kullanılabilmektedir. Nesnenin özniteliklerini "nesnenin içerisindeki değişkenler" gibi düşünebilirsiniz. 
#------------------------------------------------------------------------------------------------------------------------

class Sample:
    pass

s = Sample()

s.a = 10
s.b = 'ankara'

print(s.a)      # 10
print(s.b)      # ankara

#------------------------------------------------------------------------------------------------------------------------
    Python'da sınıfların içerisinde fonksiyonlar olabilir. Sınıfların içerisindeki fonksiyonlara "metot (method)" denilmektedir. 
    Eğer fonksiyon sınıfların dışındaysa ona "fonksiyon", bir sınıfın içerisindeyse ona "metot" denilmektedir. 

    Python'da metotların en azından bir parametresi olur. Metotların ilk parametreleri özel bir anlama sahiptir. Programcılar genel olarak
    metotların bu ilk parametrelerini "self" biçiminde isimlendirirler. Amcak bu ilk parametrenin "self" biçiminde isimlendirilmesi zorunlu değildir. Örneğin:

Burada foo, bar ve tar Sample sınıfının metotlarıdır. zar şse sınıf içerisinde değildir. O halde zar bir fonksiyondur, metot değildir. 

    Bir metodun çağrılması için o metodun içinde bulunduğu sınıf türünden bir değişkenin olması gerekir. Metot çağırma işleminin genel 
    biçimi şöyledir:

    <değişken_ismi>.<metot_ismi>([argüman listesi])

    Örneğin:

    s = Sample()
    s.foo()
    s.bar(10)
    s.tar(10, 20)
 Metot bu biçimde çağrılırken birinci self parametresi için argüman girilmez. Metoda girilen argümanlar self parametresinden 
    sonraki parametrelere ilişkindir. Örneğin:

    s = Sample()
    s.tar(10, 20)

    Burada 10 tar metodunun a parametresine, 20 ise b parametresine aktarılmaktadır.

Metotların en azından bir parametresi olmak zorunda olduğunu belirtmiştik. Bu parametrenin de genellikle "self"
    biçiminde isimlendirildiğini söylemiştik. Pekiyi bu self parametresinin anlamı nedir? İşte metotlar ilgili sınıf türünden değişkenlerle 
    çağrılırlar. Her zaman self parametresine metodun çağrılmasında kullanılan değişken (yani onun içindeki adres) atanmaktadır. 
    Başka bir deyişle self metodun çağrılmasında kullanılan nesneyi belirtmektedir. Örneğin:

    class Sample:
        def foo(self, a, b):
            pass

    s = Sample()
    s.foo(10, 20)

    Burada s değişkeni (yani içindeki adres) self'e, 10 (yani 10 nesnesinin adresi) a, ya 20 de (yani 20 nesnesinin adresi) b'ye 
    atanmaktadır. Burada self tamamen s ile aynı nesneyi gösterir.
Bir metot çağrılırken her zaman metodun çağrılmasında kullanılan değişken (yani onun içerisindeki adres) metodun birinci parametresi 
    olan self parametresine atanktadır. Bu durumda self parametresi metodun çağrılmasında kullanılan değişken ile aynı nesneyi gösterir durumda olur. 
    Metotlar ilgili sınıf türünden bir değişkenle rçağrıldığına göre o değişkenin atanacağı metotta bir self parametresinin bulunması gerekmektedir. 
    Aşağıdaki örnekte self parametresi ile s aynı nesneyi göstermektedir. Dolayısıyla nesnenin a özniteliğine self parametresiyle de 
    erişilebilmiştir. 
#------------------------------------------------------------------------------------------------------------------------

class Sample:
    def foo(self):
        print(self.a)       # 10
        
s = Sample()
s.a = 10

s.foo()

