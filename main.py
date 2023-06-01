import pandas as pd
from Insan import Insan
from Issiz import Issiz         # Diğer dosyaları main dosyasına ekliyoruz ve pandas kütüphanesini ekliyoruz...
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
    # İnsan sınıfı için 2 nesne oluşturuyoruz...
    insan1 = Insan("1234567890", "Veli", "Karatay", 18, "Erkek", "Türk")
    insan2 = Insan("0987654321", "İnci", "Koçoğlu",19 , "Kadın", "Türk")

    # İşsiz sınıfı için 3 nesne oluşturuyoruz...
    issiz1 = Issiz("11111111111", "Aykut", "Kocaman", 20, "Erkek", "Türk",3,  50,  6)
    issiz2 = Issiz("22222222222", "Aslı", "Türker", 21, "Kadın", "Türk", 20,  4, 8 )
    issiz3 = Issiz("33333333333", "Mehmet", "Öztürk", 22, "Erkek", "Türk",10,  12, 25 )
    issiz1.statu_bul()
    issiz2.statu_bul()
    issiz3.statu_bul()
    # Çalışan sınıfı için 3 nesne oluşturuyoruz...
    calisan1 = Calisan("44444444444", "Eda", "Çalışkan", 23, "Kadın", "Türk", "teknoloji", 30, 12000)
    calisan2 = Calisan("55555555555", "Yasin Bera", "Şahin", 24, "Erkek", "Türk", "muhaasebe", 20, 9000)
    calisan3 = Calisan("66666666666", "Cansu", "Kartal", 25, "Kadın", "Türk", "inşaat", 60, 20000)
    c1=calisan1.yeni_maas()
    c2=calisan2.yeni_maas()
    c3=calisan3.yeni_maas()
    # Mavi yaka sınıfı için 3 nesne oluşturuyoruz...
    mavi_yaka1 = MaviYaka("77777777777", "Ahmet", "Demir", 26, "Erkek", "Türk", "teknoloji", 60, 22000, 0.7)
    mavi_yaka2 = MaviYaka("88888888888", "Yunus", "Gökdağ", 27, "Erkek", "Türk", "muhaasebe", 30, 13000, 0.5)
    mavi_yaka3 = MaviYaka("99999999999", "Enes", "Kartop", 28, "Erkek", "Türk", "inşaat", 14, 8700, 0.3)
    m1=mavi_yaka1.yeni_maas()
    m2=mavi_yaka2.yeni_maas()
    m3=mavi_yaka3.yeni_maas()
    # Beyaz yaka sınıfı için 3 nesne oluşturuyoruz...
    beyaz_yaka1 = BeyazYaka("00000000000", "Egemen", "Akgün", 29, "Erkek", "Türk", "teknoloji", 40, 11000, 2000)
    beyaz_yaka2 = BeyazYaka("10101010101", "İrem", "Koç", 30, "Kadın", "Türk", "muhaasebe", 50, 23000, 3000)
    beyaz_yaka3 = BeyazYaka("01010101010", "Eylül", "Sabancı", 31, "Kadın", "Türk", "inşaat",10 , 10000, 1000)
    b1=beyaz_yaka1.yeni_maas()
    b2=beyaz_yaka2.yeni_maas()
    b3=beyaz_yaka3.yeni_maas()

# Nesnelerin bilgilerini __str__ metoduyla yazdırıyoruz...
    print("İnsan 1:")
    print(insan1)
    print("İnsan 2:")
    print(insan2)

    print("\nİşsiz 1:")
    print(issiz1)
    print("İşsiz 2:")
    print(issiz2)
    print("İşsiz 3:")
    print(issiz3)

    print("\nÇalışan 1:")
    print(calisan1)
    print("Çalışan 2:")
    print(calisan2)
    print("Çalışan 3:")
    print(calisan3)

    print("\nMavi Yaka 1:")
    print(mavi_yaka1)
    print("Mavi Yaka 2:")
    print(mavi_yaka2)
    print("Mavi Yaka 3:")
    print(mavi_yaka3)

    print("\nBeyaz Yaka 1:")
    print(beyaz_yaka1)
    print("Beyaz Yaka 2:")
    print(beyaz_yaka2)
    print("Beyaz Yaka 3:")
    print(beyaz_yaka3)

except Exception as e: #hatayı ekrana döndürüyoruz...
    print("Hata:", e)