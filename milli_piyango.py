import random
import os

def clear():
    os.system("clear")

clear()
sansli_sayilar = [1,2,3,4,5]
puan = 100
print("Milli Piyango: Şansli Sayi Secimi")
for sayilar in sansli_sayilar:
    print(sayilar)

print("Bu sayilardan sadece biri 7 milyon lira kazandiracak. Şansli olan kazansin.")
print("\n")

sansli_sayi = random.choice(sansli_sayilar)
while True:
    try:
        secim = int(input("Lutfen sansli sayiyi secin: "))
        if puan == 0:
            print("Uzgunuz. Puaniniz sifirlandi.")
            break
        if secim == sansli_sayi:
            print("Tebrikler! Sansli sayiyi buldunuz.")
            print(f"Sansli sayi: {sansli_sayi}")
            print(f"Elde edilen puan: {puan}")
            break
        elif secim != sansli_sayi:
            print("Uzgunuz. Sansli sayiyi bulamadiniz. Lutfen tekrar deneyin.")
            puan = puan - 20
    except KeyboardInterrupt:
        print("\nProgramdan cikis yapildi!")
        break
