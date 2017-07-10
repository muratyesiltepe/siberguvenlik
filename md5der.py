#-*- coding: utf-8 -*-
import hashlib
print ("""
###################################################
#        MD5 Encoder - MD5 Decoder                # 
#        Coded By Murat YEŞİLTEPE                 #
###################################################
""")
while(True):
        karakter = input("Encoder e, decoder d, çıkış c : ")
        if karakter == 'e':
                encod = input("Lütfen encod edilecek veriyi girin : ")
                encoded = hashlib.md5(encod.encode("utf-8"))
                print("Encod Edilmiş Hali : " , encoded.hexdigest())
        elif karakter == 'd':
                decod = input("Lütfen decod edilecek hash değerini girin : ")
                wordlist = open ("md5wordlist.txt", "r").readlines() #md5wordlist.txt isminde dosyanız olmalıdır.
                for kelime in wordlist:  #md5wordlist.txt dosyanız programla aynı dizinde yer almalıdır.
                    kelime = kelime.strip()
                    kir = hashlib.md5(kelime).hexdigest()
                    if kir == decod:
                        print("Decod Edilmiş Hali : ", decod)
        elif karakter == 'c':
            quit()
        else:
            print("Yanlış karakter girdiniz lütfen kontrol edin!")
