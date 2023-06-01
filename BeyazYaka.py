from Calisan import Calisan  # Calisan dosyasını ekliyoruz...
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                return self.__tesvik_primi
            elif 24 <= self.get_tecrube() <= 48 and self.get_maas() < 15000:       ## Zam hakkını hesaplıyoruz...
                return (self.get_maas() * self.get_tecrube() / (100*24)) * 5 + self.__tesvik_primi
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / (100*24)) * 4 + self.__tesvik_primi
            else:
                return 0
        except Exception as e:
            print(e)

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {self.get_maas() + self.zam_hakki()}"

    def yeni_maas(self):         # Yeni maaş fonksiyonu oluşturuyoruz...
        yeni_maas= self.get_maas()+self.zam_hakki()
        return yeni_maas