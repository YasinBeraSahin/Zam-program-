from Insan import Insan   # Insan dosyasını ekliyoruz...
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, maviYaka,beyazYakaa,yonetici):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__maviYaka=maviYaka
        self.__beyazYaka=beyazYakaa
        self.__yonetici=yonetici
        self.__statu = None

    def get_statu(self):
        return self.__statu
    def statu_bul(self):
        try:
            a=self.__maviYaka*0.20
            b=self.__beyazYaka*0.35       # Hesaplamaları yapıyoruz...
            c=self.__yonetici*0.45
            if a>b and a>c:
                aa="mavi yaka"
                self.__statu = aa
            elif b>a and b>c:
                bb="beyaz yaka"
                self.__statu=bb
            else :
                cc="yönetici"
                self.__statu=cc
            return self.__statu

        except ValueError as e:
            print(e)

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nEn Uygun Statü: {self.statu_bul()}"
