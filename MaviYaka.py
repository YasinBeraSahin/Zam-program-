from Calisan import Calisan     # Calisan dosyasını ekliyoruz...
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                return self.__yipranma_payi * 10
            elif 24 <= self.get_tecrube() <= 48 and self.get_maas() < 15000:          # Hesaplamaları yapıyoruz...
                return (self.get_maas() * self.get_tecrube() / (24*200)) + (self.__yipranma_payi * 10)
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / (24*300)) + (self.__yipranma_payi * 10)
            else:
                return 0
        except Exception as e:
            print(e)

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {self.get_maas() + self.zam_hakki()}"

    def yeni_maas(self):           # Yeni maaş fonksiyonu oluşturuyoruz...
        yeni_maas= self.get_maas()+self.zam_hakki()
        return yeni_maas
