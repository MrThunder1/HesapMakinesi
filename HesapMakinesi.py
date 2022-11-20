while True :
    birinci = int(input("Birinci sayıyı giriniz : "))
    ikinci = int(input("İkinci sayıyı giriniz : "))
    islem = input("Hangi işlemi yapmak istersiniz (+,-,/,*) : ")

    if (islem == "+") :
        sonuc = (birinci + ikinci)
        print(sonuc)
    elif (islem == "-") :
        sonuc = (birinci - ikinci)
        print(sonuc)
    elif (islem == "/" and ikinci != 0) :
        sonuc = (birinci / ikinci)
        print(sonuc)
    elif (islem == "*") :
        sonuc = (birinci * ikinci)
        print(sonuc)
    else :
        print("Lütfen doğru bir işlem giriniz ! ")
