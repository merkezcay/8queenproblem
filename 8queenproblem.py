count = 0
vy = [] # yerleştirilen vezirin y koordinatı (x koordinatı vezirin indeksi ile eşit olarak seçilmiştir)
vx = ["A", "B", "C", "D", "E", "F", "G", "H"] # her zaman vx[i] = i olduğu için çözüm modelimizde vx değişkeni gereksiz
def tehdit_yok(x, y): # x. vezir x, y koordinatlarına yerleştirilirken bir tehdit olup olmadığını döner  
    for z in range(x): # x aynı zamanda yeni vezirin indeksidir: önceki vezirler yeniyi tehdit eder mi?
        if vy[z] == y or x - y == z - vy[z] or x + y == z + vy[z]: # x. vezir, z. vezirle tehdit edilir
            return False
    return True
def kismen_coz(x): # ilk x vezir için kısmi çözümü bulan fonksiyondur, x = 0 ilk çözümü ile işe başlanır.
    if x == 8: # ilk sekiz vezir için kısmi çözüm, yani tam çözüm! (öz yinelemeli fonksiyon çıkış koşulu)
        global count
        count += 1
        print(f"{count}. ", end = " ")
        for i in range (8):
            print(f"{vx[i]}{vy[i] + 1}", end=" ") # end varsayılan değeri /n alt satıra geç karakteridir. 
        print() # alt satıra geçmek için gerekli.
        return 1 # x == 8 aşamasındaki her çözüm, çözüm ağacın en uçtaki yaprağıdır, dolayısıyla 1 döner!
    adet = 0
    for y in range(8):
        if tehdit_yok(x, y): # bu koşul o aşamada hiç bir y için gerçekleşmemişse, sonraki aşama yoktur.
            vy.append(y) # tehdit yoksa bir aşama sonraki kısmi çözümü bulmak için vezir yerleştiriliyor
            adet += kismen_coz(x + 1) # bir aşama sonraki kısmi çözüm için fonksiyon kendisini çağırıyor
            vy.remove(y) # diğer y değerleri için de çözümleri aramak için veziri tahtadan geri alıyoruz
    return adet # kismen_coz, x == 8 aşamasına kadar ulaşmışsa geriye doğru toplamların sonucu dönülüyor
print(f'Sekiz vezir satranç tahtasına birbirlerini tehdit etmeyecek şekilde {kismen_coz(0)} farklı şekilde dizilebilir.')