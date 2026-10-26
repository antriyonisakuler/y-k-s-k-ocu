def saat_dakikaya_cevir(saat):
    saat = saat.strip().replace(".", ":")
    parcalar = saat.split(":")

    if len(parcalar) != 2:
        raise ValueError

    saat_degeri = int(parcalar[0])
    dakika_degeri = int(parcalar[1])

    if not (0 <= saat_degeri <= 23 and 0 <= dakika_degeri <= 59):
        raise ValueError

    return saat_degeri * 60 + dakika_degeri


def dakikayi_saate_cevir(dakika):
    saat = dakika // 60
    dakika = dakika % 60

    return "{:02d}:{:02d}".format(saat, dakika)


def saat_al(mesaj):
    while True:
        try:
            return saat_dakikaya_cevir(input(mesaj))
        except (ValueError, IndexError):
            print("Hatali saat! Ornek: 13:00 veya 13.00")


def sayi_al(mesaj, en_az, en_cok):
    while True:
        try:
            sayi = int(input(mesaj))

            if en_az <= sayi <= en_cok:
                return sayi

            print("Lutfen {} ile {} arasinda gir.".format(en_az, en_cok))

        except ValueError:
            print("Lutfen sayi gir.")


def haftalik_program():
    print("=== YKS DENGE - YKS KOCU ===")

    tyt_dersleri = [
        "TYT Turkce",
        "TYT Matematik",
        "TYT Fen",
        "TYT Sosyal"
    ]

    alanlar = {
        "1": {
            "ad": "Sayisal",
            "dersler": [
                "TYT Turkce",
                "TYT Matematik",
                "TYT Fen",
                "TYT Sosyal",
                "AYT Matematik",
                "Fizik",
                "Kimya",
                "Biyoloji"
            ]
        },
        "2": {
            "ad": "Esit Agirlik",
            "dersler": [
                "TYT Turkce",
                "TYT Matematik",
                "TYT Fen",
                "TYT Sosyal",
                "AYT Matematik",
                "Edebiyat",
                "Tarih-1",
                "Cografya-1"
            ]
        },
        "3": {
            "ad": "Sozel",
            "dersler": [
                "TYT Turkce",
                "TYT Matematik",
                "TYT Fen",
                "TYT Sosyal",
                "Edebiyat",
                "Tarih-1",
                "Cografya-1",
                "Tarih-2",
                "Cografya-2",
                "Felsefe",
                "Din Kulturu"
            ]
        },
        "4": {
            "ad": "Dil",
            "dersler": [
                "TYT Turkce",
                "TYT Matematik",
                "TYT Fen",
                "TYT Sosyal",
                "Ingilizce Kelime",
                "Ingilizce Dil Bilgisi",
                "Okuma",
                "YDT Soru Cozumu"
            ]
        },
        "5": {
            "ad": "TYT",
            "dersler": tyt_dersleri
        }
    }

    print("\nCalismak istedigin alanlari sec:")
    print("1 - Sayisal")
    print("2 - Esit Agirlik")
    print("3 - Sozel")
    print("4 - Dil")
    print("5 - TYT")

    while True:
        secimler = input(
            "Secimlerini virgulle ayirarak gir (Ornek: 1,5): "
        ).replace(" ", "").split(",")

        if (
    len(secimler) > 0
    and all(secim in alanlar for secim in secimler)
    and len(secimler) == len(set(secimler))
    ):
            break

        print("Hatali secim! Gecerli ve tekrarsiz secimler gir.")

    dersler = []

    for secim in secimler:
        for ders in alanlar[secim]["dersler"]:
            if ders not in dersler:
                dersler.append(ders)

    gunler = [
        "Pazartesi",
        "Sali",
        "Carsamba",
        "Persembe",
        "Cuma",
        "Cumartesi",
        "Pazar"
    ]

    program = {}

    for gun in gunler:
        print("\n--- {} ---".format(gun))

        # SADECE CUMARTESI VE PAZAR DURUMU DEGISTIRILDI
        if gun in ("Cumartesi", "Pazar"):
            okul = "h"
            calisma_baslangici = saat_dakikaya_cevir("10:00")

        else:
            while True:
                okul = input(
                    "Bugun okulun var mi? (e/h): "
                ).strip().lower()

                if okul in ("e", "h"):
                    break

                print("Lutfen e veya h gir.")

            if okul == "e":
                while True:
                    okul_baslangic = saat_al(
                        "Okul baslangic saati: "
                    )

                    okul_bitis = saat_al(
                        "Okul bitis saati: "
                    )

                    if okul_bitis > okul_baslangic:
                        break

                    print(
                        "Okul bitis saati, baslangic saatinden "
                        "sonra olmali. Tekrar gir."
                    )

                calisma_baslangici = okul_bitis

            else:
                calisma_baslangici = saat_al(
                    "Calismaya baslamak istedigin saat: "
                )

        while True:
            sure = sayi_al(
                "Bugun kac saat calismak istiyorsun? (0-12): ",
                0,
                12
            )

            if calisma_baslangici + sure * 60 <= 1440:
                break

            print(
                "Bu sure gece yarisi sonrasina tasiyor. "
                "Daha kisa bir sure veya daha erken baslangic sec."
            )

            if okul == "h" and gun not in ("Cumartesi", "Pazar"):
                calisma_baslangici = saat_al(
                    "Yeni calisma baslangic saatin: "
                )

        program[gun] = {
            "baslangic": calisma_baslangici,
            "sure": sure
        }

    print("\n\n========== HAFTALIK YKS PROGRAMIN ==========")

    ders_sayaci = 0

    for gun in gunler:
        print("\n{}".format(gun))
        print("-" * 30)

        baslangic = program[gun]["baslangic"]
        sure = program[gun]["sure"]

        if sure == 0:
            print("Bugun ders calismayacaksin.")
            continue

        for i in range(sure):
            ders = dersler[ders_sayaci % len(dersler)]

            ders_baslangici = baslangic + i * 60
            ders_bitisi = ders_baslangici + 60

            print(
                "{} - {} : {}".format(
                    dakikayi_saate_cevir(ders_baslangici),
                    dakikayi_saate_cevir(ders_bitisi),
                    ders
                )
            )

            ders_sayaci += 1


haftalik_program()