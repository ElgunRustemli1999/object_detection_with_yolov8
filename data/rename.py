import os
import glob

# Resimlerin bulunduğu klasörün yolu
klasor_yolu = "dataset/"

# Klasördeki tüm resim/txt dosyalarını bul
resimler_jpg = glob.glob(os.path.join(klasor_yolu, "*.jpg"))  
resimler_txt = glob.glob(os.path.join(klasor_yolu, "*.txt"))  
# print(resimler_txt)
for i, eski_ad_txt in enumerate(resimler_txt, start=1):
    yeni_ad = os.path.join(klasor_yolu, f"{i}.txt")  
    os.rename(eski_ad_txt, yeni_ad)
    print(f"{eski_ad_txt} dosyası {yeni_ad} olarak yeniden adlandırıldı.")

# Yeniden adlandırma işlemi
for i, eski_ad_jpg in enumerate(resimler_jpg, start=1):
    yeni_ad = os.path.join(klasor_yolu, f"{i}.jpg")  
    os.rename(eski_ad_jpg, yeni_ad)
    print(f"{eski_ad_jpg} dosyası {yeni_ad} olarak yeniden adlandırıldı.")
