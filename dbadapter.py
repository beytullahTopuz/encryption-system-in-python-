
from json_islemler import JsonIslemler
import hashlib
import simetrik
a=JsonIslemler()
def register(old_password,new_password):
    hashs= hashlib.sha1(new_password.encode())
    hashs=hashs.hexdigest()
    old_password=hashlib.sha1(old_password.encode())
    old_password=old_password.hexdigest()
    return a.sistemUpdate(hashs,old_password)
def login(parola):
    parola= hashlib.sha1(parola.encode())
    parola=parola.hexdigest()
   # print(parola)
    return a.login('SYSTEM',parola)
def yeni(sitead,siteparola,userparola):
    a.jsonYeniVeriEkle(sitead,simetrik.sifrele(siteparola,userparola))
def goster(parola,sitead):
    data=a.verileri_listele()
    for site in data:
        if(site['link']==sitead):
            print(site['link'] + " şifreniz : " + simetrik.coz(site['sifre'],parola))
def listele(parola):
    data=a.verileri_listele()
    del data[0]
    for site in data:
        sifre=simetrik.coz(site['sifre'],parola)
        print(site['link'] + " : " + sifre)
        #print(sifre)
def guncelle(eski_parola, yeni_parola):
    data=a.verileri_listele()
    
    for site in data:
        if(site['link']!='SYSTEM'):
            sifre=simetrik.coz(site['sifre'],eski_parola)
            
         #   print(sifre)
            sifre=simetrik.sifrele(sifre,yeni_parola)
         #   print(sifre)
            a.jsonVeriGuncelle(site['link'],sifre)



            

            

            



#print(login("ROOT"))
#hashs= hashlib.sha1("ROOT".encode())
#hashs=hashs.hexdigest()
#print(hashs)

 