----------------------------------Pytest Decoratorleri---------------------------------------

@pytest.mark.skip: Uygulanan  testi atlar atlar.

@pytest.mark.parametrize: Bir test işlevi için bağımsız değişkenlerin parametreleştirilmesini sağlar

@pytest.mark.skipif: Koşullu olarak bir testi atlamak için kullanılır.

@pytest.mark.xfail: Bir testin başarısız olmasını beklediğinizi belirtmek için kullanılır.Bu test çalışacak, ancak başarısız olduğunda geri izleme bildirilmeyecek.Bunun yerine, terminal raporlaması bunu "başarısız olması bekleniyor" (XFAIL ) veya "beklenmedik bir şekilde başarılı" ( XPASS) bölümlerinde listeleyecektir . 

@pytest.mark.timeout: Temel düzeyde, test işlevleri, ihtiyaç duydukları fikstürleri argüman olarak bildirerek talep eder.pytest bir test yapmaya gittiğinde, o test fonksiyonunun imzasındaki parametrelere bakar ve ardından bu parametrelerle aynı ada sahip fikstürleri arar. pytest bunları bulduğunda, bu fikstürleri çalıştırır, döndürdüklerini (varsa) yakalar ve bu nesneleri argüman olarak test işlevine iletir.Testler ve fikstürler , bir defada tek bir fikstür talep etmekle sınırlı değildir . İstedikleri kadar talep edebilirler. 

@pytest.mark.filterwarnings Belirli test öğelerine uyarı filtreleri eklemek için kullanabilirsiniz , bu da test, sınıf ve hatta modül düzeyinde hangi uyarıların yakalanması gerektiğini daha iyi kontrol etmenizi sağlar.