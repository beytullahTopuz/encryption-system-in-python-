from json_islemler import JsonIslemler
import dbadapter

katman1=True
katman2=False
nesne=JsonIslemler()


def katmanInfo1():
    print("kayıt eski_parola")
    print("giriş mevcut_parola")
    a = input(">>>")
    if(a.split()[0]=='kayıt' and dbadapter.login(a.split()[1])):
        b = input("parola: ")
        c = input("parola (tekrar): ")
        if(b==c):
            if(dbadapter.register(a.split()[1],b)):
                dbadapter.register(a.split()[1],b)
                dbadapter.guncelle(a.split()[1],b)
                print("şifreniz değiştirildi ")
                return False

                
        else:
            print(b)
            print(c)
            print("şifreler uyuşmuyor ")
            return False
    if(a.split()[0]=="giriş" and dbadapter.login(a.split()[1])):
        dbadapter.login(a.split()[1])
        print("giriş başarılı")
        return True

def katmanInfo2():
    print("-"*100)
    print("yeni siteadı.com site_şifresi")
    print("göster siteadi.com")
    print("listele")
    a=input(">>>")
    if(a.split()[0]=="yeni"):
        parola=input("parolanızı girin: ")
        dbadapter.yeni(a.split()[1],a.split()[2],parola)
    if(a.split()[0]=="göster"):
        parola=input("parolanızı girin: ")
        dbadapter.goster(parola,a.split()[1])
    if(a.split()[0]=="listele"):
        parola=input("parolanızı girin: ")
        dbadapter.listele(parola)


while(katman1==True):
    katman1info=katmanInfo1()
    if(katman1info==True):
        katman2=True
    while(katman2==True):
        katmanInfo2()



        

    