print(" - Hesap Makinesi - ")
while True :
    print(" ---------------- ")
    sayı1 = int(input("1.sayıyı giriniz : "))
    sayı2 = int(input("2.sayıyı giriniz : "))
    hesap = input("İşlem seçiniz (+,-,*,/) : ")
    if hesap == "+" :
        print("Sonuç : ", sayı1 + sayı2)
    elif hesap == "-" :
        print("Sonuç : ", sayı1 - sayı2)
    elif hesap == "*" :
        print("Sonuç : ", sayı1 * sayı2)
    elif hesap == "/" :
        print("Sonuç : ", sayı1 / sayı2)
    else:
        print("Hatalı işlem seçtiniz ! ( Tekrar Deneyiniz )")