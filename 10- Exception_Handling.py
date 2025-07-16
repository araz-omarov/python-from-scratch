try:
    n = int(input("Zəhmət Olmasa Rəqəm Daxil Edin: "))
    print(10/n)
except ZeroDivisionError:
    print("Sıfıra Bölünə Bilməz !")
except ValueError:
    print("Rəqəm Yazmalısan !")
else:                                                         
    print("Hər Şey Qaydasındadır !")
finally:
    print("Program Bitdi")
    
#--------------------------------------------#

# try ---> Burada səhv ola bilər, məsələn: sıfıra bölmə və ya hərf daxil etmə
# except ---> Əgər try blokunda səhv olsa, burası işləyir
# else ---> Əgər heç bir səhv olmasa, burası işləyir
# finally ---> Nə olursa-olsun, bu blok mütləq işləyir
 