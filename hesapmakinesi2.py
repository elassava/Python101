anahtar = 1
while (anahtar == 1) :
 islem = input("yapmak istediğiniz işlemi seçiniz (/, *, -, +, **, //, yuzde) (çıkmak için b): ")

 if (islem == "b"): 
    print("çıkılıyor...")
    anahtar = 0
    
 elif (islem == "/") : 
    num1 = input("ilk sayıyı giriniz: ")
    num2 = input("ikinci sayıyı giriniz: ")
    sonuc = float(num1) / float(num2)
    print(sonuc)

 elif (islem == "*") : 
    num1 = input("ilk sayıyı giriniz: ")
    num2 = input("ikinci sayıyı giriniz: ")
    sonuc = float(num1) * float(num2)
    print(sonuc)

 elif (islem == "-") : 
    num1 = input("ilk sayıyı giriniz: ")
    num2 = input("ikinci sayıyı giriniz: ")
    sonuc = float(num1) - float(num2)
    print(sonuc)

 elif (islem == "+") : 
    num1 = input("ilk sayıyı giriniz: ")
    num2 = input("ikinci sayıyı giriniz: ")
    sonuc = float(num1) + float(num2)
    print(sonuc)

 elif (islem == "**") : 
    num1 = input("sayınızı giriniz: ")
    num2 = input("üs değerini giriniz: ")
    sonuc = float(num1) ** float(num2)
    print(sonuc)

 elif (islem == "//") : 
    num1 = input("ilk sayıyı giriniz: ")
    num2 = input("ikinci sayıyı giriniz: ")
    sonuc = float(num1) // float(num2)
    print(sonuc)
    
 elif (islem == "yuzde"): 
    num1 = input("sayınızı giriniz: ")
    num2 = input("yüzde değerini giriniz: ")
    sonuc = float(num1) * float(num2) / 100
    print(sonuc)  
    
   

 
