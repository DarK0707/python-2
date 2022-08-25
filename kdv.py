urun_fiyati = float(input("Urun fiyatini giriniz :"))
kdv_tutari = int(input("Kdv tutarını giriniz :"))

toplam_fiyat = (urun_fiyati+(urun_fiyati*(kdv_tutari/100)))
kdvsiz_fiyat = urun_fiyati

print(f"Kdvli Fiyatınız {toplam_fiyat:.f} $\nKdvsiz Fiyatınız {kdvsiz_fiyat} $")



