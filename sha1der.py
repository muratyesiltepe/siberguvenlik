#-*- coding: utf-8 -*-
import hashlib
print ("""
###################################################
#        SHA1 Encoder - SHA1 Decoder              # 
#        Coded By Murat YEŞİLTEPE                 #
###################################################
""")
while(True):
        karakter = input("Encoder : e, Decoder : d, Quit : q : ")
        if karakter == 'e':
                encoder = input("Şifrelenecek veriyi giriniz : ")
                encode = hashlib.sha1(encoder.encode('utf-8'))
                print("Encod Edilmiştir : ",encode.hexdigest())
        elif karakter == 'd':
                decoder = input("Hash değerini giriniz : ")
                wordlist = open("sha1wordlist.txt","r").readlines() #sha1wordlist.txt aynı dizinde olmalıdır.
                for kelime in wordlist:
                    kelime = kelime.strip()
                    kir = hashlib.sha1(kelime).hexdigest()
                    if kir == decoder:
                            print("Decod Edilmiştir : ", kelime)
                    else:
                        print("Decod Edilememiştir")
        elif karakter == 'q':
            quit()
        else:
            print("Yanlış Karakter Girdiniz, Lütfen Düzeltin!")
