# Writing Basic Calculator in Python

def Topla(number1, number2):
    result = number1 + number2
    print(result)

def Cikar(number1, number2):
    result = number1 - number2
    print(result)

def Carp(number1, number2):
    result = number1 * number2
    print(result)

def Bol(number1, number2):
    result = number1 / number2

try: 
    number1 = int(input("Birinci Sayi: "))
    number2 = int(input("Ikinci Sayi: "))
    islem_secimi = int(input("1- Topla\n2- Cikar\n3- Carp\n4- Bol\nLutfen seciminizi yapin\n: "))
    
    if islem_secimi == 1:
        Topla(number1, number2)
        
    elif islem_secimi == 2:
        Cikar(number1, number2)
    
    elif islem_secimi == 3:
        Carp(number1, number2)
        
    elif islem_secimi == 4:
        try:
            Bol(number1, number2)
        except ZeroDivisionError:
            print(f"0 sayisi {number1} sayisini bolemez. Bu nedenle islem gecersizdir.")
    
except ValueError:
    print("Lutfen sayisal bir deger girmeye calisin.")
except KeyboardInterrupt:
    print("Programdan cikis yapildi!")
