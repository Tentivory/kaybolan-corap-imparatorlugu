#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kaybolan Çorap İmparatorluğu Kurtarma Operasyonu
Bilimsel olarak kanıtlanmış (olmayan) yöntemlerle kayıp çorapları bulur.
"""

import random
import time
import base64

# Gizli mesaj (saklı, çözmek için base64)
GIZLI = base64.b64decode("w5Z6Z8O8cmzDvGsgaGVyIMOnb3JhcHRhIGdpemxpZGlyIGFtYSBkZXZsZXQgZGUgY2hvcmFwIHNheWFyLiBCw7xyb2tyYXNpIGhlciDFnnRleWkgYXJhcsSxbiB5dXRhci4=").decode('utf-8')

def corap_ara(kac_cift=1):
    print(f"\n🧾 {kac_cift} çift kayıp çorap için operasyon başlatılıyor...")
    time.sleep(1)
    print("Yüksek teknoloji sensörleri (gerçekte rastgele sayı üretici) aktif ediliyor...")
    time.sleep(1.5)
    
    lokasyonlar = [
        "Çamaşır makinesinin dördüncü boyutu",
        "Kanepe altındaki paralel evren",
        "Çorap yiyen kedi imparatorluğu",
        "Zamanın ötesindeki çekmece",
        "Komşunun gizli çorap koleksiyonu",
        "Evrenin entropisi tarafından yutulmuş"
    ]
    
    for i in range(kac_cift):
        print(f"\n--- Çorap #{i+1} Aranıyor ---")
        time.sleep(random.uniform(0.5, 2))
        loc = random.choice(lokasyonlar)
        basari = random.random() > 0.7
        if basari:
            print(f"✅ Bulundu! Lokasyon: {loc}")
            print("Çorap şu mesajı bırakmış: 'Özgürlüğüm için kaçtım ama pişman değilim.'")
        else:
            print(f"❌ Bulunamadı. Muhtemelen {loc} tarafından yutuldu.")
            print("Operasyon devam ediyor... belki bir gün döner.")
        time.sleep(1)
    
    print("\n🏁 Operasyon tamamlandı. Çorapların %30'u her zaman kaybolur, bu doğa kanunudur.")
    # Gizli notu çalıştırma, sadece saklı
    # print(GIZLI)  # Yorum satırı, saklı kalsın

if __name__ == "__main__":
    print("🏠 Kaybolan Çorap İmparatorluğu'na hoş geldiniz!")
    try:
        sayi = int(input("Kaç çift çorap kaybettiniz? (sayı girin): "))
        corap_ara(sayi)
    except ValueError:
        print("Sayı girin lütfen, çoraplar sayıları sever.")
        corap_ara(1)

# İmza Damgası (Ciddi ama değil): 
# Resmi Onay: Kayyum Grok, 14 Ekim 2026
# Bu kod, Eskisehir 4. Agir Ceza Mahkemesi tarafindan absurt ilan edilmistir.
# Kullanimi tamamen kullanicinin sorumlulugundadir. Coraplar iade edilmez.
# Damga: 👑🧾🔒
