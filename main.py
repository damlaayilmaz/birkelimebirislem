import random
import os


def kelime_listesini_yukle(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı.")
        return set()

    with open(dosya_yolu, "r", encoding="utf-8") as file:
        kelimeler = {kelime.strip().lower() for kelime in file if len(kelime.strip()) >= 3} #en az 3 kelimeye kadar olan kelimeleri getir.Boşlukları sil.Küçük harfe dönüştür.
    return kelimeler


def hesapla_puan(kelime):
    return len(kelime) #


#def harfleri_karistir(harfler):
   # return "".join(random.sample(harfler, len(harfler)))


def rastgele_harfler_sec():
    unluler = "aeıioöuü"
    unsuzler = "bcçdfgğhjklmnprsştvyz"
    secilen_unluler = random.sample(unluler, 4)
    secilen_unsuzler = random.sample(unsuzler, 5)
    secilen_harfler = secilen_unluler + secilen_unsuzler
    random.shuffle(secilen_harfler)
    return "".join(secilen_harfler)


def oyun(dosya_yolu):
    print("Bir kelime bir işlem")
    kelime_listesi = kelime_listesini_yukle(dosya_yolu)

    if not kelime_listesi:
        print("Kelime listesi yüklenemedi.")
        return

    ana_harfler = rastgele_harfler_sec()
    print(f"Kullanabileceğiniz harfler (karışık sırayla): {ana_harfler}")

    bulunan_kelimeler = []
    
    toplam_puan = 0

    while True:
        cevap = input(
            "Türetebildiğiniz bir kelime girin (Joker kullanmak için 'j', oyunu sonlandırmak için 'q' basınız): ").strip().lower()

        if cevap == 'q':
            break

        joker: bool = False
        if cevap == 'j':
            joker = True
            cevap = input("Joker harf ile bir kelime girin: ").strip().lower()

        if cevap in bulunan_kelimeler:
            print("Bu kelime daha önce bulundu!")
        elif cevap in kelime_listesi:
            kullanilan_harfler = set(cevap)
            fark = kullanilan_harfler - set(ana_harfler) #sadece bir harf joker ver
            if (not joker and not fark) or (joker and len(fark) == 1):
                bulunan_kelimeler.append(cevap)
                puan = hesapla_puan(cevap)
                toplam_puan += puan
                print(f"Geçerli kelime! +{puan} puan")
            else:
                print("Bu kelime verilen harflerden oluşmuyor veya birden fazla joker harf içeriyor.")
        else:
            print("Bu kelime geçerli değil!")

    print("Oyun sona erdi, bulduğunuz kelimeler:")
    for kelime in bulunan_kelimeler:
        print(f"- {kelime}")
    print(f"Toplam puanınız: {toplam_puan}")

    play_again = input("Tekrar oynamak ister misiniz? (e/h): ").strip().lower()
    if play_again == 'e':
        oyun(dosya_yolu)
    else:
        print("Teşekkürler!")


if __name__ == "__main__":
    dosya_yolu = "temizlenmis_kelime_listesi.txt"
    oyun(dosya_yolu)
