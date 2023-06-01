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