import json

class JsonIslemler:
    f = open('VT.json',) 
    data = json.load(f) 
    

    def __init__(self):
        pass

    def jsonOku(self):
        print("null")
    

    def jsonVeriGuncelle(self, adres, new_sifre):
        try:
            jsonVeri = self.data
            index = -1
            for i in range(len(jsonVeri)):
                if jsonVeri[i]['link'] == adres:
                   index = i
            if(index != -1):
                jsonVeri[index] = {"link": adres, "sifre": new_sifre}
              #  print(" guncellendi: ",jsonVeri)
                with open('VT.json', 'w') as outfile:
                     json.dump(jsonVeri, outfile)
                print("güncellendi")
            else:
                print("Geücellenecek eleman bulunamadı")
        except:
            print("error")
        self.f.close


    def jsonYeniVeriEkle(self, adres , sifre):
        print(adres , sifre)
        print(type(self.data))
        new_veri = {'link':adres,'sifre': sifre}

        icerdekiVeri = self.data
       
      #  print( "icerdeki veri : ---------",icerdekiVeri)

        icerdekiVeri.append(new_veri)# ekleme işlemi
        print(icerdekiVeri)
        with open('C:\\Users\\beytu\OneDrive\\Masaüstü\\ÖDEV\VT.json', 'w') as outfile:
            json.dump(icerdekiVeri, outfile)
    def verileri_listele(self):
        try:
            return self.data
        except:
            print("error")

    def login(self, username, password):
        veri = self.data[0]
        if(veri['link'] == username and veri['sifre'] == password):
            return True
        else:
            return False
    def sistemUpdate(self, new_password, old_password):
        
        veri = self.data
        if (veri[0]['sifre'] == old_password):
            veri[0]['sifre'] = new_password
            with open('C:\\Users\\beytu\OneDrive\\Masaüstü\\ÖDEV\VT.json', 'w') as outfile:
                json.dump(veri, outfile)
            return True
        else:
            return False 
    

