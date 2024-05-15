#kelime oyunu
import random

sesli_harfler = "euoai"
sessiz_harfler = "wqrtypsdfghjklzxcvbnm"
Turkce_karakterler = "ığĞüÜşŞöÖçÇ"
Kelime_listesi = ["system", "data", "algorithm", "such", "base", "node", "model", "case", "program", "information",
                  "set", "code", "function", "process", "application", "software", "class", "point", "type", "network",
                  "tree", "object", "element", "input", "operation", "level", "memory", "table", "order", "file",
                  "variable", "language", "write", "list", "structure", "compute", "sequence", "computer", "bit",
                  "probability", "machine", "array", "page", "error", "step", "search", "most", "path", "graph", "web",
                  "length", "several", "security", "proof", "access", "obtain", "matrix", "task", "image", "form",
                  "return", "interface", "resource", "address", "implementation", "loop", "first", "read", "location",
                  "hardware", "behavior", "programming", "field", "key", "parameter", "distribution", "definition",
                  "instance", "interaction", "internet", "representation", "edge", "stack", "return", "procedure",
                  "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                  "detection", "write", "execute", "least", "key"]

secim = 1
yeni = ""
while secim == 1:
    puan = 0
    secilen_kelime = random.choice(Kelime_listesi)
    print("secilen kelime:", secilen_kelime)
    kelime_uzunlugu = len(secilen_kelime)

    if kelime_uzunlugu % 2 != 0:
        tahmin_hak = int((kelime_uzunlugu / 2) + 1)
    else:
        tahmin_hak = int(kelime_uzunlugu / 2)

    print("Tahmin hak:", tahmin_hak)
    print("Bulmanız gereken kelime:")

    degisken_kelime = "_" * kelime_uzunlugu
    print(degisken_kelime)

    while tahmin_hak != 0:

        harf = input("\nBir harf giriniz:")
        harf = harf.lower()
        if harf in Turkce_karakterler:
            harf = input("Turkce olmayan karakter giriniz!:")
            continue
        elif (harf not in sesli_harfler) and (harf not in sessiz_harfler):
            print("Lutfen bir harf giriniz:")
            continue
        a = 0

        for k in range(kelime_uzunlugu):
            if secilen_kelime[k] == harf:
                aranan_kelime = degisken_kelime
                degisken_kelime = aranan_kelime[0:k:1] + harf + aranan_kelime[k + 1:kelime_uzunlugu:1]
                a += 1

        if harf not in yeni:

            if harf in sesli_harfler:
                puan += 3 * a
            else:
                puan += 2 * a
        if harf not in secilen_kelime:
            puan -= 4
            tahmin_hak -= 1
            if tahmin_hak == 0:
                print("Kaybettiniz :(")
        yeni += harf

        print("Yeni puan:{}".format(puan))
        print("Kalan tahmin hakk:{}".format(tahmin_hak))
        print("Kelimenin son hali:{}".format(degisken_kelime))

        if degisken_kelime == secilen_kelime:
            print("\nKazandiniz!")
            tahmin_hak = 0
    secim = int(input("Yeni kelimeye gecmek icin 1 e bas!\nCikmak icin 2ye bas!"))
