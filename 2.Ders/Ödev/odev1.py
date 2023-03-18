liste = []

def ogrenciListele():
        for ogrenci in liste:
            print(ogrenci)

def ogrenciGiris():
    giris = input(str("Lütfen İsim Soyisim giriniz:"))
    liste.append(giris)
    print(giris, " kaydedilmiştir")
    ogrenciListele()

def ogrenciSilme():
    giris = input(str("Lütfen İsim Soyisim giriniz:"))
    
    for ogrenci in liste:
        if(ogrenci==giris):
            liste.remove(giris)
            print(ogrenci+" silindi")
            if(len(liste)==0):
                print("Liste Boş")
            else:
                ogrenciListele()
            break
        else:
            print(giris+" listede bulunmamaktadır")
            ogrenciListele()
            break

def cokluOgrenciEkleme():
    ogrenciSayisi=int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
    i=0
    while i < ogrenciSayisi:
        giris =input("öğrencinin ismi ve soyismi: ")
        liste.append(giris)
        i += 1
        print("Öğrenciler eklenmiştir.")
        ogrenciListele()



def cokluOgrenciSilme():
    # if len(liste) == 5:
    #     while len(liste) == 3:
    #         liste.pop()
    #         print(liste)

    i=0
    while i<liste:
         giris = input("  Silinecek olan ismi giriniz")         
         liste.remove(giris)
         print(giris ,"silinmiştir ")
         i+=1
         ogrenciListele()

def ogrenciSirasi():
    for ogrenci in enumerate(liste):
        print(ogrenci)

islem = int(input("Lütfen  yapmak istediğiniz işlem numarasını giriniz:"))

while islem ==True:                
    if islem == 1:
        ogrenciGiris()
        break
    elif islem == 2:
        ogrenciSilme()
        break
    elif islem == 3:
        cokluOgrenciEkleme()
        break
    elif islem == 4:
        cokluOgrenciSilme()
        break
    elif islem == 5:
        ogrenciSirasi()
        break
    elif islem == 6:
        ogrenciListele()
        break
    elif islem == 7:
        print("Çıkış yapılmıştır")
        break
    else:
        print("Girdiğiniz numara yanlıştır.")

