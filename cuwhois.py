import whois
print("""
_______            _______ _________ ______   _______  _______ 
(  ____ \|\     /|(  ____\ \__   __/(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/   ) (   | (   ) )| (    \/| (    )|
| |      | |   | || (_____    | |   | (__/ / | (__    | (____)|
| |      | |   | |(_____  )   | |   |  __ (  |  __)   |     __)
| |      | |   | |      ) |   | |   | (  \ \ | (      | (\ (   
| (____/\| (___) |/\____) |___) (___| )___) )| (____/\| ) \ \__
(_______/(_______)\_______)\_______/|/ \___/ (_______/|/   \__/

                    CREATED BY : Murat YEŞİLTEPE
                    EXECUTE    : python cuwhois.py | py -3 -m cuwhois.py
                    USAGE      : h4cktimes.com
                    EXİT       : q 
""")
while True:
    domain = input("Domain Adresi : ")
    if domain == 'q':
        exit()
    w = whois.whois(domain)
    print("Firma : ", w.get('registrar'))
    print("Oluşturulma Tarihi : ", w.get('creation_date'))
    print("Bitiş Tarihi : ", w.get('expiration_date'))
    print("Güncelleme Tarihi : ", w.get('updated_date'))
    print("Statü Durumu : ", w.get('status'))
    print("Sahibinin Adı : ", w.get('registrant_name'))
    print("Telefon Numarası : ", w.get('phone'))
    print("Email Adresleri : ", w.get('emails'))
    print("Name Server Adresleri : ", w.get('name_servers'))