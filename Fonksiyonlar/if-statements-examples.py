# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:38:42 2021

@author: Cem ATILGAN
"""
#%% Örnek-1
"""
Kullanıcıdan bir yaş girmesini isteyin. 
Kullanıcının girdiği yaş eğer 18’den büyükse ekrana Yetişkin, 
18’den küçükse ekrana Çocuk yazdıran programı Python dilinde kodlayalım. 
"""

yas=int(input("Yasi giriniz:"))

if(yas>=18):
    print("Yetiskin")
    
else:
    print("Cocuk")


    
#%% Örnek-2
"""
Kullanıcıdan bir sayı girmesini isteyiniz. 
Girilen sayının pozitif, negatif ve sıfıra eşit olma durumlarını
düşünerek girilen sayının pozitiflik- negatiflik durumunu ekrana yazdıralım.
"""


sayi=float(input("Bir sayi giriniz:"))

if(sayi==0):
    print("Sayi sifira esittir.")
    
elif(sayi<0):
    print("Sayi negatiftir.")
 
else:     
    print("Sayi pozitiftir.")
    

"""
else yerine aşağıdaki yapıda kullanılabilir.

elif (sayi>0):
    print("Sayi pozitiftir.")

"""

#%%Örnek-3

"""
Bir üniversitede öğrencilerin dersi geçme not ortalaması 60’tır. 
Öğrencinin vize notu ortalamaya %40, final notu %60 etki ettiğine göre
girilen vize ve final notlarına göre öğrencinin geçip kaldığını 
ekrana yazdıran program Python dilinde kodlayalım.
"""

vize=float(input("Vize notunu giriniz:"))
final=float(input("Final notunu giriniz:"))

ort=(vize*0.4)+(final*0.6)
print("Ogrenci ortalamasi:",ort)


if(ort<60): # 59'a kadar ortalamalar kalacak.
    print("Kaldi")

else:
    print("Gecti")
    

#%% Örnek-4

"""
Kullanıcıdan açı girmesini isteyelim. 
Kullanıcının girdiği açıya göre, açının dar, dik ve geniş açı olduğunu 
ekrana yazdıran programı kodlayalım.
"""

aci=float(input("Aciyi giriniz:"))

if(aci<90):
    print("Dar acidir")

elif(aci==90):
    print("Dik acidir")
    
elif(aci>90):
    print("Genis acidir")
    
#%% Örnek-5
    
"""
Öğrencinin vize notu ortalamaya %40, final notu %60 
etki ettiğine göre girilen vize ve final notlarının 
harf karşılıklarını ve geçip kalma durumunu yazdıran 
programı Python dilinde kodlayalım.

90-100  arası  AA
70-89 arası    BA
60-69 arası    BB
50-59 arası    CB
35-49 arası    CC
35 altı        FF


Not : Şart kontrolü (90 <= ort <= 100)
"""















