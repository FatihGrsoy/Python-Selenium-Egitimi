""""
-------------------------HTML-----------------------------
HTML(Hyper Text Markup Language) Web sayfalarını oluşturma aşamasında kullanılan  bir metin işaret dilidir.
Genel bilinen yanlış kanının aksine HTML bir programlama dili değildir. Daha açık anlatmak gerekirse, Chrome,
Firefox, Yandex gibi tarayıcıların okuyup anlamlandırdığı dil HTML dilidir. 

-----------------------HTML LOCATORS----------------------
Locators(Konumlandırıcı), Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir 
komuttur. Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur. Site üzerindeki bir elemente örneğin
giriş butonuna selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi locator’lar aracılığıyla yaparız.
Selenium ile geliştirmek istediğimiz test otomasyonlarında locator’ları kullanarak ilgili alanlara veri gönderebilir,
tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz. Bunlar ‘By’ objesi olarak oluşturulur.
Yaygın olarak kullanılan locator çeşitleri: ID, NAME, CLASS_NAME, TAG_NAME, LINK_TEXT, CSS_SELECTOR, XPATH.

------------------SELENİUM AKSİYONLARI-------------------
clear() => bir formun giriş alanı veya hatta bağlantı etiketi paragrafı vb. gibi herhangi bir alandaki metni temizlemek
           için kullanılır. İçeriğini tarayıcınızdaki web sayfasında değiştirir.
click() => sayfada, mouse üzerinde sol düğmeye tıklama işlemi yapar. Sağ düğmeye tıklama işlemi için "context_click()"
           metodu uygulanmaktadır.
find_element() => Selenium'daki findElement yöntemi, bir web öğesini tanımlamanıza yardımcı olan bir komuttur.
                FindElement'in Selenium'da ID, Ad, Sınıf Adı, Bağlantı Metni, Kısmi Bağlantı Metni, Etiket gibi
                web bulucuları kullanarak web sayfasındaki bir web öğesini benzersiz bir şekilde tanımlamanın
                sağladığı birden çok yol vardır. 

find_elements() => Selenium'daki findElements, yalnızca tek bir web öğesi döndüren findElement'in aksine size konumlandırıcı
                   değeriyle eşleşen web öğelerinin listesini döndürür. Web sayfasında eşleşen öğe yoksa findElements boş bir liste döndürür.

send_keys() => Verileri tarayıcıya göndermek ve bir otomasyon testi gerçekleştirmek için web sitesinin giriş alanıyla
               etkileşim kurmak için kullanılır.

get_attribute() => HTML ile ilgili özniteliklerin değerini almak için kullanılır. Bir web öğesinin String olarak döndürülen
                   herhangi bir özniteliğinin değerini almaya yardımcı olur. Bir özniteliğin bir Boole değeri varsa, yöntem
                   True veya null değerini döndürür. Ayrıca, öznitelik yoksa, yöntem null döndürür.



"""