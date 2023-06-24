#Ortalama Hesaplama

sayi = input("Virgül ile sayilari giriniz.: ")
 
print("Girdiginiz Sayilar: {0}".format(sayi))
 
ortalama=sayi.split(",")                                                                #split(",") komutu ile virgülleri sileriz.
toplam = 0 
for n in ortalama:
   toplam = toplam + int(n)                                                             #sayilarin toplamini hesaplar.
 
print("GIRDIGINIZ SAYILARIN NOT ORTALAMASI:{0:.2f} ".format(toplam / len(ortalama)))    #len(ortalama) ile kaç adet sayi olduğunu hesaplariz.
#format(toplam / len(ortalama)) ile sayilarin toplamini sayi adetine bölerek ortalamayi hesaplariz.
