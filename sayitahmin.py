import random
x = random.randint(0,10)
hak = int(input("Deneme hakkı: "))
sayac = 0

while hak>0:
    tahmin = int(input("Tahmin ettiğiniz sayı: "))
    hak = hak - 1
    if tahmin == x:
        print(f"Doğru sonucu buldunuz. Skorunuz {100 - (20 * (sayac))}.")
        break
    
    elif tahmin < x and  hak>0 :
        print("Gerçek değer tahmin ettiğiniz sayıdan büyük. Tekrar deneyiniz.")
    
    elif tahmin > x and hak>0:
        print("Gerçek değer tahmin ettiğiniz sayıdan küçük. Tekrar deneyiniz.")
        
    elif hak==0: 
        print(f"Deneme hakkınız doldu. Doğru cevap {x}.")
        
    sayac += 1
        