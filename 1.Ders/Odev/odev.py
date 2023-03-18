"""
string    => Tırnak içerisinde yazılan metinsel bir veri tipidir.
int       => Tamsayı türünde -2^31 ile +2^31-1 arasıda değerleri alabilen veri tipidir.
float     => Ondalıklı sayı türünde 32 bitlik değerleri alabilen veri tipidir.
boolean   => Karar yapılarında kullanılan, yalnızca True ve False değerlerini alan bir veri tipidir.
complex   => Karmaşık sayıları ifade eden veri tipidir.



---------VERİ TİPİ ÖRNEKLERİ-------------

LİSTE     => Anasayfada bulunan 7 adet eğitim programlama adlı listede tutulmaktadır.
int       => Yorum sayısı
boolean   => Önceki ders ,Bitir ve devam et butonları


---------ŞART BLOKLARI-----------------

İF-ELSE   => Bitir ve devam et butonu ile dersi tamamlama yüzdesi ilişkisi
FOR       => Eğitimlerin seçilmesi kısmında eğitmen isminin seçilmesiyle o eğitmene ait olan eğitinlerin listelenmesi


"""

Programlama =["Python&Selenium","JavaScript","Java+React","C#+Angular",".NET","JAVA","Programlamaya Giriş"]
egitmen =["Halit Enes Kalaycı","Engin Demiroğ"]
Halit = Programlama[0:1]
Engin = Programlama[1:7]
egitmenAdi=input(str("Eğitmen : "))
for program in Programlama:
    if egitmenAdi == egitmen[0]:
        print(Halit)
        break
    else:
        print(Engin)
        break


















